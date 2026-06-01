# Puutarhakanta API (PT2.4)

REST API for the Finnish botanical garden plant collection database (*puutarhakanta2005*).

## What It Does

Provides full access to a botanical garden's plant records:
- Taxa (species, varieties, cultivars) with scientific names, genus, and species
- Acquisitions (how/when/from-whom plants were obtained)
- Physical garden locations and inspection records
- Taxonomic classification data
- Specimen and seed bank records
- International conservation agreement data

**Read operations (GET)** are public and require no authentication. **Write operations (POST/PUT/DELETE)** require JWT bearer token authentication.

## Quick Start

### 1. Set Up Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your database and authentication settings (see [Environment Variables](#environment-variables) section below).

### 3. Initialize Database

**Option A: Use Local SQLite (Default & Recommended)**

SQLite is the default database with no separate server required:

```bash
mkdir -p ./sqlite-backup
sqlite3 ./sqlite-backup/puutarhakanta2005.sqlite < puutarhakanta2005_schema.sql
```

Verify the tables were created:

```bash
sqlite3 ./sqlite-backup/puutarhakanta2005.sqlite ".tables"
```

The app will automatically use `./sqlite-backup/puutarhakanta2005.sqlite` when you run it.

**Option B: Use Docker MySQL**

```bash
mkdir -p ./db-backups
cp puutarhakanta2005_schema.sql ./db-backups/
docker compose up -d mysql
```

Then configure `.env`:
```
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=puutarhakanta2005
DB_USER=tarkastususer
DB_PASSWORD=tarkastususer
```

**Option C: Use External MySQL**

Configure `.env` with your server details:
```
DB_HOST=your-mysql-host
DB_PORT=3306
DB_NAME=puutarhakanta2005
DB_USER=your_user
DB_PASSWORD=your_password
```

### 4. Run the Application

```bash
fastapi dev
```

API will be available at `http://localhost:8000`

- **Interactive Docs**: `http://localhost:8000/docs` (Swagger UI)
- **Alternative Docs**: `http://localhost:8000/redoc` (ReDoc)
- **OpenAPI Schema**: `http://localhost:8000/openapi.json`

## Environment Variables

### Database Connection

**For SQLite (Default):**
- No database variables needed. The app automatically uses `./sqlite-backup/puutarhakanta2005.sqlite`

**For MySQL:**
Set these variables in `.env`:

| Variable | Default | Description |
|----------|---------|----------|
| `DB_HOST` | `localhost` | MySQL host |
| `DB_PORT` | `3306` | MySQL port |
| `DB_NAME` | `puutarhakanta2005` | Database name |
| `DB_USER` | `tarkastususer` | MySQL user |
| `DB_PASSWORD` | `tarkastususer` | MySQL password |
| `DATABASE_URL` | _(none)_ | **Optional**: Full SQLAlchemy URL to override above vars (e.g., `mysql+pymysql://user:pass@host:3306/db`) |

### Authentication

| Variable | Default | Description |
|----------|---------|----------|
| `JWT_SECRET_KEY` | _(required for auth)_ | Secret key for signing JWT tokens (min 32 characters) |
| `JWT_ALGORITHM` | `HS256` | JWT signing algorithm |
| `JWT_EXPIRATION_HOURS` | `24` | JWT token expiration time in hours |

Generate a secure secret key:
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

## API Usage

### Endpoint Patterns

All endpoints follow a consistent two-route pattern where both trailing-slash and no-slash variants work:

**Read (Public - No Authentication Required)**:
```
GET /{resource}           → list all items
GET /{resource}/          → list all items (equivalent to above)
GET /{resource}/{pk}      → single record by primary key
```

**Write (Authentication Required - Bearer Token)**:
```
POST /{resource}          → create new record
POST /{resource}/         → create new record (equivalent to above)
PUT /{resource}/{pk}      → update record
DELETE /{resource}/{pk}   → delete record
```

### Query Parameters

All list endpoints accept query parameters for filtering and pagination:

#### Free-Text Search

Use the `search=` parameter to search across searchable columns:

```bash
# Search taksoni by scientific name, genus, or species
GET /taksoni/?search=Rosa&page=1&page_size=25

# Search any list endpoint  
GET /lahettaja/?search=Botanicus

# Case-insensitive substring matching
GET /hankintatiedot/?search=helsinki
```

**Searchable Fields by Endpoint:**
- `/taksoni`: `tieteellinen_nimi` (scientific name), `suku` (genus), `laji` (species)
- Other endpoints: all text columns are searchable by default

#### Exact-Match Filtering

Filter by any column using exact match:

```bash
# Single filter
GET /taksoni/?suku=Rosa&laji=canina

# Multiple filters (AND logic)
GET /lahettaja/?maa=Suomi&lahettajatyyppi=BG

# Combine with search (search OR exact filters)
GET /taksoni/?search=Rosa&suku=Rosa&page=1
```

#### Pagination

```bash
# Skip and limit (legacy style)
GET /taksoni/?skip=100&limit=50

# Page-based pagination (taksoni endpoint)
GET /taksoni/?page=2&page_size=25
```

### Authentication

To access write operations, include a JWT bearer token in the `Authorization` header:

```bash
Authorization: Bearer <jwt_token>
```

Obtain a token by logging in:

```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin"}'
```

Response:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer"
}
```

### Example Requests

**Read operations (no authentication):**

```bash
# Get first 25 taxa
curl http://localhost:8000/taksoni/?page=1&page_size=25

# Search for taxa matching "Rosa" in scientific name, genus, or species
curl http://localhost:8000/taksoni/?search=Rosa&page=1&page_size=25

# Filter by genus
curl http://localhost:8000/taksoni/?suku=Rosa&page=1&page_size=25

# Get taxa matching both genus and species
curl http://localhost:8000/taksoni/?suku=Rosa&laji=canina&page=1

# Get a specific taxon by ID
curl http://localhost:8000/taksoni/12345

# Find senders by country
curl http://localhost:8000/lahettaja/?maa=Suomi

# Search for acquisitions
curl http://localhost:8000/hankintatiedot/?search=Helsinki&skip=0&limit=50

# Count matching items
curl http://localhost:8000/lahettaja/count?maa=Suomi
```

**Write operations (authentication required):**

```bash
# Create new taxon (requires Bearer token)
curl -X POST http://localhost:8000/taksoni/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "taksonin_nro": 9999,
    "tieteellinen_nimi": "Rosa acicularis",
    "suku": "Rosa",
    "laji": "acicularis"
  }'

# Update taxon record
curl -X PUT http://localhost:8000/taksoni/9999 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "suku": "Rosa",
    "laji": "acicularis",
    "tieteellinen_nimi": "Rosa acicularis Lindl."
  }'

# Delete taxon record
curl -X DELETE http://localhost:8000/taksoni/9999 \
  -H "Authorization: Bearer $TOKEN"
```

## Core Endpoints

### Main Tables

| Prefix | Primary Key | Description | Example Search |
|--------|------------|-------------|---|
| `/taksoni` | `taksonin_nro` | Taxa (species, varieties) | `?search=Rosa` |
| `/hankintatiedot` | `hankintaID` | Acquisition records | `?search=Helsinki` |
| `/lahettaja` | `lahettajanro` | Senders/source organizations | `?search=Botanicus` |
| `/heimo` | `jarjestysnumero` | Taxonomic families | `?suku=Ranunculaceae` |
| `/viite` | `viitenro` | Bibliographic references | `?search=Journal` |
| `/kayttajatiedot` | `id` | User accounts | `?search=admin` |

### Taxon-Related Endpoints (Reference taksoni)

| Prefix | FK Field | Description |
|--------|----------|-------------|
| `/alkuperainen_kasvupaikka` | `taksonin_nro` | Original growing sites |
| `/kasvin_kayttotarkoitus` | `taksonin_nro` | Plant usage purposes |
| `/kansainvaliset_sopimukset` | `taksonin_nro` | International agreements |
| `/maailman_levinneisyysalue` | `taksonin_nro` | World distribution areas |
| `/suomalainen_levinneisyysalue` | `taksonin_nro` | Finnish distribution areas |
| `/muunkielinen_nimi` | `taksonin_nro` | Foreign-language names |
| `/synonyymi` | `taksonin_nro` | Synonyms |
| `/taksonin_lappu` | `taksonin_nro` | Taxon labels |

### List/Lookup Endpoints

All lookup tables follow the pattern `/lista_<name>/`:

| Prefix | Description | Searchable |
|--------|-------------|-----------|
| `/lista_alkuperatyyppi` | Origin types | `?search=wild` |
| `/lista_hyotykaytto` | Utilitarian use types | `?search=medicinal` |
| `/lista_kasvumuoto` | Growth forms | `?search=shrub` |
| `/lista_kayttotarkoitus` | Usage purposes | `?search=food` |
| `/lista_kieli` | Languages | `?search=English` |

**See `/docs` for complete endpoint list.**

## Testing

Run the test suite:

```bash
# All tests
pytest

# Only integration tests
pytest tests/test_get_endpoints_integration.py

# Only taksoni-specific tests
pytest tests/test_get_endpoints_integration.py -k taksoni

# With verbose output
pytest -v

# Coverage report
pytest --cov=app tests/
```

Key test files:
- `tests/test_get_endpoints_integration.py` — Integration tests for all endpoints, including search functionality
- `tests/test_endpoint_model_fields.py` — Field mapping validation
- `tests/test_openapi_contract.py` — OpenAPI schema validation

## Caching

The API implements automatic **5-minute TTL caching** for high-read tables to reduce database load and improve response times.

### Cached Endpoints

The following endpoints cache their list responses:
- **Core tables**: `taksoni`, `hankintatiedot`, `heimo`, `lahettaja`, `osastopaikka`, `sijoituspaikka`
- **Acquisition-related**: `alkuperaa_koskevat_tiedot`, `kasvatustietoja`, `tarkastusmerkinta`, `toimenpide`
- **Lookup/reference lists**: All `lista_*` endpoints (70+ reference tables)

### How Caching Works

1. **Query-based keys**: Each unique query (including search parameters, filters, pagination) gets its own cache entry
2. **Automatic expiration**: Cache entries expire after 5 minutes (TTL)
3. **Invalidation on write**: POST/PUT/DELETE operations automatically clear the endpoint's cache
4. **Query consistency**: Different query parameters generate different cache keys, so filters always work correctly

### Example

```bash
# First request: hits database, caches result
curl http://localhost:8000/taksoni/?search=Rosa&page=1&page_size=25

# Second request (within 5 min): returns from cache (fast!)
curl http://localhost:8000/taksoni/?search=Rosa&page=1&page_size=25

# After POST/PUT/DELETE on taksoni: cache cleared, next request hits database again
curl -X POST http://localhost:8000/taksoni/ -H "Authorization: Bearer $TOKEN" ...
```

### Cache Monitoring

Check cache statistics:

```bash
curl http://localhost:8000/cache-stats
```

Response:
```json
{
  "size": 42,
  "maxsize": 512,
  "ttl": 300,
  "keys": ["taksoni:a1b2c3d4...", "hankintatiedot:e5f6g7h8...", ...]
}
```

### Performance Impact

- **Read performance**: ~10-100x faster for cached queries (depending on database load)
- **Memory usage**: ~512 max cache entries × ~10KB avg = ~5MB max
- **Consistency**: Always consistent with 5-minute TTL; instant consistency on data mutations

### Cache Invalidation Strategy

| Operation | Cache Behavior |
|-----------|----------------|
| GET (search/filter) | Cached for 5 minutes |
| GET (by ID) | Not cached (single-record lookups typically fast) |
| POST (create) | Clears all cache for that endpoint |
| PUT (update) | Clears all cache for that endpoint |
| DELETE | Clears all cache for that endpoint |

### Disabling Cache (for development)

To disable caching temporarily, comment out the `@cached_list()` decorator in endpoint files:

```python
@router.get("/", response_model=List[Schema])
# @cached_list("taksoni")  # Commented out to disable caching
def read_all(...):
    ...
```

Or modify `CACHE_TTL_SECONDS` in `app/cache.py`:
```python
CACHE_TTL_SECONDS = 0  # Set to 0 to disable all caching
```

## Architecture

### Project Structure

```
app/
├── main.py                 # FastAPI app initialization, middleware setup
├── database.py             # SQLAlchemy engine and session management
├── cache.py                # TTL caching utilities and monitoring
├── api/
│   ├── api.py             # Central router registration
│   ├── query.py           # Shared filter logic (handles search, exact matching)
│   ├── crud.py            # Create, update, delete operations
│   ├── dependencies.py    # JWT authentication dependencies
│   └── endpoints/         # One file per entity (taksoni.py, hankintatiedot.py, etc.)
├── models/                # SQLAlchemy ORM models (one per table)
├── schemas/               # Pydantic request/response schemas
├── core/                  # Configuration and security
└── security/              # JWT token utilities

tests/                      # pytest test suite
docs/                       # Architecture and conventions documentation
```

### Search Implementation

The shared filter helper (`app/api/query.py`) provides free-text search:

1. **By default**: Searches all text columns with case-insensitive substring matching
2. **Per-model override**: Models can define `__searchable_columns__` to limit search scope

Example (taksoni):
```python
class Taksoni(Base):
    __tablename__ = 'taksoni'
    __searchable_columns__ = ('tieteellinen_nimi', 'suku', 'laji')  # Scientific name, genus, species
```

### Caching Layer

The caching implementation (`app/cache.py`) provides:

1. **TTL-based cache**: Uses `cachetools.TTLCache` with 5-minute expiration
2. **Query-aware keys**: Generates consistent hash from endpoint + query parameters
3. **Automatic invalidation**: Clears endpoint cache on any write operation
4. **Statistics endpoint**: Exposes cache state for monitoring

Cached endpoints register in `CACHEABLE_ENDPOINTS` set and use the `@cached_list()` decorator.


### Query Filter Flow

```
1. Parse search= parameter
2. Apply case-insensitive LIKE to searchable string columns
3. Parse all other query params (exact column matches)
4. Combine with OR for search, AND for exact filters
5. Apply pagination (page/page_size or skip/limit)
```

## Routing

### Trailing Slash Handling

FastAPI normalizes routes to include trailing slashes. This API supports both variants:

```bash
GET /taksoni                # Works (no redirect)
GET /taksoni/               # Works (equivalent)

POST /taksoni               # Works
POST /taksoni/              # Works
```

Both resolve to the same handler with no redirection overhead.

## Database Configuration

### SQLite (Default)

- **Location**: `./sqlite-backup/puutarhakanta2005.sqlite`
- **Setup**: Run schema SQL file directly
- **Advantages**: No external dependencies, perfect for development
- **Driver**: Python sqlite3 (built-in)

### MySQL

- **Driver**: PyMySQL
- **Versions**: MySQL 5.7+ or 8.0+
- **Connection**: Via docker-compose or external server
- **Setup**: Use `docker-compose.yml` or configure `.env`

## Common Issues & Troubleshooting

### "Database file not found"

**Problem**: SQLite database missing
```
FileNotFoundError: [Errno 2] No such file or directory
```

**Solution**:
```bash
mkdir -p ./sqlite-backup
sqlite3 ./sqlite-backup/puutarhakanta2005.sqlite < puutarhakanta2005_schema.sql
```

### "Search returns everything"

**Problem**: Search parameter isn't filtering
**Solution**: Ensure model has searchable columns (taksoni includes `tieteellinen_nimi`, `suku`, `laji`)

### "Unknown query parameter X"

**Expected behavior**: Unknown query parameters are silently ignored (per API design)
```bash
# Unknown param is ignored
GET /taksoni/?unknown_field=value  # No error, just ignored
```

### "Authentication failed"

**Problem**: Bearer token invalid or missing
```bash
# Set token variable
TOKEN=$(curl -s -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin"}' | jq -r '.access_token')

# Use token
curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/taksoni/
```

## API Contract

- **Request Format**: JSON (`Content-Type: application/json`)
- **Response Format**: JSON
- **Search Matching**: Case-insensitive substring (ILIKE in SQL)
- **Pagination**: `page` (1-indexed) / `page_size` or `skip` / `limit`
- **Error Responses**: Standard HTTP status codes (200, 201, 400, 401, 404, 500)

## Development

### Adding a New Search Field

To make a model searchable in specific fields:

```python
# In app/models/example.py
class ExampleModel(Base):
    __tablename__ = 'example'
    __searchable_columns__ = ('name', 'description', 'code')  # Only these fields searched
    
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    code: Mapped[Optional[str]] = mapped_column(String(50))
```

The shared filter helper will respect this declaration automatically.

### Running Tests

```bash
# Setup
python -m pytest --collect-only  # List all tests

# Run specific test
pytest tests/test_get_endpoints_integration.py::test_taksoni_search_filters_results -v

# Run with coverage
pytest --cov=app --cov-report=html tests/
```

## Performance Notes

- **Relationships disabled by default**: To prevent N+1 queries, all ORM relationships are loaded with `noload()`. Specify eager loading in endpoint if needed.
- **Pagination recommended**: Large result sets can degrade performance; use `page_size` to limit
- **Search is indexed**: Text columns are indexed for faster LIKE queries (depends on database)

## License

See LICENSE file for details.

## Support

For issues or questions:
1. Check the API docs at `/docs`
2. Review test examples in `tests/`
3. Check model definitions in `app/models/`
