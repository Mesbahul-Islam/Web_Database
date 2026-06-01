"""
Caching utilities for high-read tables.

Provides TTL-based caching for frequently-read endpoints to reduce database load.
Cache is automatically invalidated on data mutations (POST, PUT, DELETE).
"""

from functools import wraps
from typing import Any, Callable, Dict, Tuple
from cachetools import TTLCache
import hashlib
import json

# 5-minute TTL for cached responses
CACHE_TTL_SECONDS = 300

# Cache for list endpoints (key: (endpoint, query_string) → value: response)
list_cache: TTLCache = TTLCache(maxsize=512, ttl=CACHE_TTL_SECONDS)

# Track which endpoints have active caches for invalidation
CACHEABLE_ENDPOINTS = {
    'taksoni',
    'hankintatiedot',
    'heimo',
    'lahettaja',
    'viite',
    'kayttajatiedot',
    'osastopaikka',
    'sijoituspaikka',
    'alkuperaa_koskevat_tiedot',
    'alkuperainen_kasvupaikka',
    'kasvin_kayttotarkoitus',
    'kansainvaliset_sopimukset',
    'maailman_levinneisyysalue',
    'suomalainen_levinneisyysalue',
    'suomalainen_kasvupaikka',
    'muunkielinen_nimi',
    'synonyymi',
    'taksonin_lappu',
    'taksonin_viljelytiedot',
    'maaritysmerkinta',
    'kasvatustietoja',
    'tarkastusmerkinta',
    'toimenpide',
    'naytetieto',
    'naytetietoja',
    'ymparistoindikaattoriluonne',
    # Lookup/reference lists - frequently read, rarely changed
    'lista_alkuperainen_kasvupaikka',
    'lista_alkuperainen_levinneisyys',
    'lista_alkuperainen_vai_tulokas',
    'lista_alkuperatyyppi',
    'lista_ei_kesta_seuraavia_torjunta_aineita',
    'lista_haku',
    'lista_hyotykaytto',
    'lista_ilmastonkestavyys',
    'lista_isokoodi',
    'lista_kasvinsaapuminen',
    'lista_kasvumuoto',
    'lista_kasvupaikka_suomessa',
    'lista_kayttotarkoitus',
    'lista_kestaa_seuraavia_torjunta_aineita',
    'lista_kieli',
    'lista_koristekaytto',
    'lista_laakekaytto',
    'lista_lahettajantyyppi',
    'lista_levinneisyysalue_maailmalla',
    'lista_lisaystapa',
    'lista_luonnonsuojeluarvo_muualla',
    'lista_luonnonsuojeluarvo_suomessa',
    'lista_luonnonvarainen_levinneisyys',
    'lista_maarittaja',
    'lista_maaritysmerkinta',
    'lista_millaisenasaatu',
    'lista_naytteensijainti',
    'lista_naytteentyyppi',
    'lista_neuvoisuus_kotisuus',
    'lista_osasto',
    'lista_polytystapa',
    'lista_puutarhanerikoiskokoelma',
    'lista_puutarhanomakokoelma',
    'lista_rauhoitukset',
    'lista_siemenia_jaljella',
    'lista_sopimukset',
    'lista_status',
    'lista_tarkastaja',
    'lista_tarkastajanimi',
    'lista_tuulenkestavyys',
    'lista_varsi',
    'lista_viherrakentamiskaytto',
    'lista_viljelyn_tarkoitus',
    'lista_ymparistoindikaattoriluonne',
}


def _get_cache_key(endpoint: str, query_params: Dict[str, Any]) -> str:
    """Generate a cache key from endpoint and query parameters."""
    # Sort params for consistent key generation
    sorted_params = sorted(query_params.items())
    params_str = json.dumps(sorted_params)
    params_hash = hashlib.md5(params_str.encode()).hexdigest()
    return f"{endpoint}:{params_hash}"


def cached_list(endpoint: str) -> Callable:
    """
    Decorator to cache list endpoint responses.
    
    Usage:
        @router.get("/")
        @cached_list("taksoni")
        def read_all(...):
            ...
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Extract query params from request
            # Request can be in args or kwargs
            request = None
            
            # Check kwargs first (FastAPI dependency injection)
            for key, value in kwargs.items():
                if hasattr(value, 'query_params'):
                    request = value
                    break
            
            # Check args if not found in kwargs
            if not request:
                for arg in args:
                    if hasattr(arg, 'query_params'):
                        request = arg
                        break
            
            if not request:
                # Can't cache without request object, call directly
                return func(*args, **kwargs)
            
            query_dict = dict(request.query_params)
            cache_key = _get_cache_key(endpoint, query_dict)
            
            # Return cached result if available
            if cache_key in list_cache:
                return list_cache[cache_key]
            
            # Call function and cache result
            result = func(*args, **kwargs)
            list_cache[cache_key] = result
            return result
        
        return wrapper
    
    return decorator


def invalidate_endpoint_cache(endpoint: str) -> None:
    """
    Invalidate all cache entries for a specific endpoint.
    Called after POST/PUT/DELETE operations.
    """
    keys_to_delete = [key for key in list_cache.keys() if key.startswith(f"{endpoint}:")]
    for key in keys_to_delete:
        del list_cache[key]


def invalidate_all_cache() -> None:
    """Clear all caches (use sparingly)."""
    list_cache.clear()


def get_cache_stats() -> Dict[str, Any]:
    """Return cache statistics for monitoring."""
    return {
        "size": len(list_cache),
        "maxsize": list_cache.maxsize,
        "ttl": CACHE_TTL_SECONDS,
        "keys": list(list_cache.keys()),
    }
