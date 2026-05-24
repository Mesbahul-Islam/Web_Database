from fastapi import APIRouter

api_router = APIRouter()

from app.api.endpoints.alkuperaa_koskevat_tiedot import router as alkuperaa_koskevat_tiedot_router  # alkuperaa_koskevat_tiedot: origin-related_data
api_router.include_router(alkuperaa_koskevat_tiedot_router, prefix="/alkuperaa_koskevat_tiedot", tags=["AlkuperaaKoskevatTiedot"])  # alkuperaa_koskevat_tiedot: origin-related_data
from app.api.endpoints.alkuperainen_kasvupaikka import router as alkuperainen_kasvupaikka_router  # alkuperainen_kasvupaikka: original growing site
api_router.include_router(alkuperainen_kasvupaikka_router, prefix="/alkuperainen_kasvupaikka", tags=["AlkuperainenKasvupaikka"])  # alkuperainen_kasvupaikka: original growing site
from app.api.endpoints.hankintanumero import router as hankintanumero_router  # hankintanumero: acquisition number
api_router.include_router(hankintanumero_router, prefix="/hankintanumero", tags=["Hankintanumero"])  # hankintanumero: acquisition number
from app.api.endpoints.hankintatiedot import router as hankintatiedot_router  # hankintatiedot: acquisition_data
api_router.include_router(hankintatiedot_router, prefix="/hankintatiedot", tags=["Hankintatiedot"])  # hankintatiedot: acquisition_data
from app.api.endpoints.heimo import router as heimo_router  # heimo: family
api_router.include_router(heimo_router, prefix="/heimo", tags=["Heimo"])  # heimo: family
from app.api.endpoints.huomioita import router as huomioita_router  # huomioita: notes
api_router.include_router(huomioita_router, prefix="/huomioita", tags=["Huomioita"])  # huomioita: notes
from app.api.endpoints.kansainvaliset_sopimukset import router as kansainvaliset_sopimukset_router  # kansainvaliset_sopimukset: international_agreements
api_router.include_router(kansainvaliset_sopimukset_router, prefix="/kansainvaliset_sopimukset", tags=["KansainvalisetSopimukset"])  # kansainvaliset_sopimukset: international_agreements
from app.api.endpoints.kasvatustietoja import router as kasvatustietoja_router  # kasvatustietoja: cultivation_data
api_router.include_router(kasvatustietoja_router, prefix="/kasvatustietoja", tags=["Kasvatustietoja"])  # kasvatustietoja: cultivation_data
from app.api.endpoints.kasvin_kayttotarkoitus import router as kasvin_kayttotarkoitus_router  # kasvin_kayttotarkoitus: plant_usage_purpose
api_router.include_router(kasvin_kayttotarkoitus_router, prefix="/kasvin_kayttotarkoitus", tags=["KasvinKayttotarkoitus"])  # kasvin_kayttotarkoitus: plant_usage_purpose
from app.api.endpoints.kayttajatiedot import router as kayttajatiedot_router  # kayttajatiedot: user_data
api_router.include_router(kayttajatiedot_router, prefix="/kayttajatiedot", tags=["Kayttajatiedot"])  # kayttajatiedot: user_data
from app.api.endpoints.lahettaja import router as lahettaja_router  # lahettaja: sender
api_router.include_router(lahettaja_router, prefix="/lahettaja", tags=["Lahettaja"])  # lahettaja: sender
from app.api.endpoints.lista_alkuperainen_kasvupaikka import router as lista_alkuperainen_kasvupaikka_router  # lista_alkuperainen_kasvupaikka: list original growing site
api_router.include_router(lista_alkuperainen_kasvupaikka_router, prefix="/lista_alkuperainen_kasvupaikka", tags=["ListaAlkuperainenKasvupaikka"])  # lista_alkuperainen_kasvupaikka: list original growing site
from app.api.endpoints.lista_alkuperainen_levinneisyys import router as lista_alkuperainen_levinneisyys_router  # lista_alkuperainen_levinneisyys: list original distribution
api_router.include_router(lista_alkuperainen_levinneisyys_router, prefix="/lista_alkuperainen_levinneisyys", tags=["ListaAlkuperainenLevinneisyys"])  # lista_alkuperainen_levinneisyys: list original distribution
from app.api.endpoints.lista_alkuperainen_vai_tulokas import router as lista_alkuperainen_vai_tulokas_router  # lista_alkuperainen_vai_tulokas: list native or introduced
api_router.include_router(lista_alkuperainen_vai_tulokas_router, prefix="/lista_alkuperainen_vai_tulokas", tags=["ListaAlkuperainenVaiTulokas"])  # lista_alkuperainen_vai_tulokas: list native or introduced
from app.api.endpoints.lista_alkuperatyyppi import router as lista_alkuperatyyppi_router  # lista_alkuperatyyppi: list origin type
api_router.include_router(lista_alkuperatyyppi_router, prefix="/lista_alkuperatyyppi", tags=["ListaAlkuperatyyppi"])  # lista_alkuperatyyppi: list origin type
from app.api.endpoints.lista_ei_kesta_seuraavia_torjunta_aineita import router as lista_ei_kesta_seuraavia_torjunta_aineita_router  # lista_ei_kesta_seuraavia_torjunta_aineita: list does not tolerate the following pesticides
api_router.include_router(lista_ei_kesta_seuraavia_torjunta_aineita_router, prefix="/lista_ei_kesta_seuraavia_torjunta_aineita", tags=["ListaEiKestaSeuraaviaTorjuntaAineita"])  # lista_ei_kesta_seuraavia_torjunta_aineita: list does not tolerate the following pesticides
from app.api.endpoints.lista_haku import router as lista_haku_router  # lista_haku: list search
api_router.include_router(lista_haku_router, prefix="/lista_haku", tags=["ListaHaku"])  # lista_haku: list search
from app.api.endpoints.lista_hyotykaytto import router as lista_hyotykaytto_router  # lista_hyotykaytto: list utilitarian use
api_router.include_router(lista_hyotykaytto_router, prefix="/lista_hyotykaytto", tags=["ListaHyotykaytto"])  # lista_hyotykaytto: list utilitarian use
from app.api.endpoints.lista_ilmastonkestavyys import router as lista_ilmastonkestavyys_router  # lista_ilmastonkestavyys: list climatic hardiness
api_router.include_router(lista_ilmastonkestavyys_router, prefix="/lista_ilmastonkestavyys", tags=["ListaIlmastonkestavyys"])  # lista_ilmastonkestavyys: list climatic hardiness
from app.api.endpoints.lista_isokoodi import router as lista_isokoodi_router  # lista_isokoodi: list iso code
api_router.include_router(lista_isokoodi_router, prefix="/lista_isokoodi", tags=["ListaIsokoodi"])  # lista_isokoodi: list iso code
from app.api.endpoints.lista_kasvinsaapuminen import router as lista_kasvinsaapuminen_router  # lista_kasvinsaapuminen: list plant arrival
api_router.include_router(lista_kasvinsaapuminen_router, prefix="/lista_kasvinsaapuminen", tags=["ListaKasvinsaapuminen"])  # lista_kasvinsaapuminen: list plant arrival
from app.api.endpoints.lista_kasvumuoto import router as lista_kasvumuoto_router  # lista_kasvumuoto: list growth form
api_router.include_router(lista_kasvumuoto_router, prefix="/lista_kasvumuoto", tags=["ListaKasvumuoto"])  # lista_kasvumuoto: list growth form
from app.api.endpoints.lista_kasvupaikka_suomessa import router as lista_kasvupaikka_suomessa_router  # lista_kasvupaikka_suomessa: list growing site in finland
api_router.include_router(lista_kasvupaikka_suomessa_router, prefix="/lista_kasvupaikka_suomessa", tags=["ListaKasvupaikkaSuomessa"])  # lista_kasvupaikka_suomessa: list growing site in finland
from app.api.endpoints.lista_kayttotarkoitus import router as lista_kayttotarkoitus_router  # lista_kayttotarkoitus: list_usage_purpose
api_router.include_router(lista_kayttotarkoitus_router, prefix="/lista_kayttotarkoitus", tags=["ListaKayttotarkoitus"])  # lista_kayttotarkoitus: list_usage_purpose
from app.api.endpoints.lista_kestaa_seuraavia_torjunta_aineita import router as lista_kestaa_seuraavia_torjunta_aineita_router  # lista_kestaa_seuraavia_torjunta_aineita: list tolerates following pesticide agents
api_router.include_router(lista_kestaa_seuraavia_torjunta_aineita_router, prefix="/lista_kestaa_seuraavia_torjunta_aineita", tags=["ListaKestaaSeuraaviaTorjuntaAineita"])  # lista_kestaa_seuraavia_torjunta_aineita: list tolerates following pesticide agents
from app.api.endpoints.lista_kieli import router as lista_kieli_router  # lista_kieli: list language
api_router.include_router(lista_kieli_router, prefix="/lista_kieli", tags=["ListaKieli"])  # lista_kieli: list language
from app.api.endpoints.lista_koristekaytto import router as lista_koristekaytto_router  # lista_koristekaytto: list ornamental use
api_router.include_router(lista_koristekaytto_router, prefix="/lista_koristekaytto", tags=["ListaKoristekaytto"])  # lista_koristekaytto: list ornamental use
from app.api.endpoints.lista_laakekaytto import router as lista_laakekaytto_router  # lista_laakekaytto: list medicinal use
api_router.include_router(lista_laakekaytto_router, prefix="/lista_laakekaytto", tags=["ListaLaakekaytto"])  # lista_laakekaytto: list medicinal use
from app.api.endpoints.lista_lahettajantyyppi import router as lista_lahettajantyyppi_router  # lista_lahettajantyyppi: list sender type
api_router.include_router(lista_lahettajantyyppi_router, prefix="/lista_lahettajantyyppi", tags=["ListaLahettajantyyppi"])  # lista_lahettajantyyppi: list sender type
from app.api.endpoints.lista_levinneisyysalue_maailmalla import router as lista_levinneisyysalue_maailmalla_router  # lista_levinneisyysalue_maailmalla: list distribution area worldwide
api_router.include_router(lista_levinneisyysalue_maailmalla_router, prefix="/lista_levinneisyysalue_maailmalla", tags=["ListaLevinneisyysalueMaailmalla"])  # lista_levinneisyysalue_maailmalla: list distribution area worldwide
from app.api.endpoints.lista_lisaystapa import router as lista_lisaystapa_router  # lista_lisaystapa: list propagation method
api_router.include_router(lista_lisaystapa_router, prefix="/lista_lisaystapa", tags=["ListaLisaystapa"])  # lista_lisaystapa: list propagation method
from app.api.endpoints.lista_luonnonsuojeluarvo_muualla import router as lista_luonnonsuojeluarvo_muualla_router  # lista_luonnonsuojeluarvo_muualla: list_nature_conservation_value_elsewhere
api_router.include_router(lista_luonnonsuojeluarvo_muualla_router, prefix="/lista_luonnonsuojeluarvo_muualla", tags=["ListaLuonnonsuojeluarvoMuualla"])  # lista_luonnonsuojeluarvo_muualla: list_nature_conservation_value_elsewhere
from app.api.endpoints.lista_luonnonsuojeluarvo_suomessa import router as lista_luonnonsuojeluarvo_suomessa_router  # lista_luonnonsuojeluarvo_suomessa: list_nature_conservation_value_in_finland
api_router.include_router(lista_luonnonsuojeluarvo_suomessa_router, prefix="/lista_luonnonsuojeluarvo_suomessa", tags=["ListaLuonnonsuojeluarvoSuomessa"])  # lista_luonnonsuojeluarvo_suomessa: list_nature_conservation_value_in_finland
from app.api.endpoints.lista_luonnonvarainen_levinneisyys import router as lista_luonnonvarainen_levinneisyys_router  # lista_luonnonvarainen_levinneisyys: list wild distribution
api_router.include_router(lista_luonnonvarainen_levinneisyys_router, prefix="/lista_luonnonvarainen_levinneisyys", tags=["ListaLuonnonvarainenLevinneisyys"])  # lista_luonnonvarainen_levinneisyys: list wild distribution
from app.api.endpoints.lista_maarittaja import router as lista_maarittaja_router  # lista_maarittaja: list identifier / determiner
api_router.include_router(lista_maarittaja_router, prefix="/lista_maarittaja", tags=["ListaMaarittaja"])  # lista_maarittaja: list identifier / determiner
from app.api.endpoints.lista_maaritysmerkinta import router as lista_maaritysmerkinta_router  # lista_maaritysmerkinta: list identification_entry
api_router.include_router(lista_maaritysmerkinta_router, prefix="/lista_maaritysmerkinta", tags=["ListaMaaritysmerkinta"])  # lista_maaritysmerkinta: list identification_entry
from app.api.endpoints.lista_millaisenasaatu import router as lista_millaisenasaatu_router  # lista_millaisenasaatu: list received as
api_router.include_router(lista_millaisenasaatu_router, prefix="/lista_millaisenasaatu", tags=["ListaMillaisenasaatu"])  # lista_millaisenasaatu: list received as
from app.api.endpoints.lista_naytteensijainti import router as lista_naytteensijainti_router  # lista_naytteensijainti: list specimen location
api_router.include_router(lista_naytteensijainti_router, prefix="/lista_naytteensijainti", tags=["ListaNaytteensijainti"])  # lista_naytteensijainti: list specimen location
from app.api.endpoints.lista_naytteentyyppi import router as lista_naytteentyyppi_router  # lista_naytteentyyppi: list specimen type
api_router.include_router(lista_naytteentyyppi_router, prefix="/lista_naytteentyyppi", tags=["ListaNaytteentyyppi"])  # lista_naytteentyyppi: list specimen type
from app.api.endpoints.lista_neuvoisuus_kotisuus import router as lista_neuvoisuus_kotisuus_router  # lista_neuvoisuus_kotisuus: list nativeness nativeness
api_router.include_router(lista_neuvoisuus_kotisuus_router, prefix="/lista_neuvoisuus_kotisuus", tags=["ListaNeuvoisuusKotisuus"])  # lista_neuvoisuus_kotisuus: list nativeness nativeness
from app.api.endpoints.lista_osasto import router as lista_osasto_router  # lista_osasto: list section
api_router.include_router(lista_osasto_router, prefix="/lista_osasto", tags=["ListaOsasto"])  # lista_osasto: list section
from app.api.endpoints.lista_polytystapa import router as lista_polytystapa_router  # lista_polytystapa: list pollination method
api_router.include_router(lista_polytystapa_router, prefix="/lista_polytystapa", tags=["ListaPolytystapa"])  # lista_polytystapa: list pollination method
from app.api.endpoints.lista_puutarhanerikoiskokoelma import router as lista_puutarhanerikoiskokoelma_router  # lista_puutarhanerikoiskokoelma: list garden special collection
api_router.include_router(lista_puutarhanerikoiskokoelma_router, prefix="/lista_puutarhanerikoiskokoelma", tags=["ListaPuutarhanerikoiskokoelma"])  # lista_puutarhanerikoiskokoelma: list garden special collection
from app.api.endpoints.lista_puutarhanomakokoelma import router as lista_puutarhanomakokoelma_router  # lista_puutarhanomakokoelma: list garden own collection
api_router.include_router(lista_puutarhanomakokoelma_router, prefix="/lista_puutarhanomakokoelma", tags=["ListaPuutarhanomakokoelma"])  # lista_puutarhanomakokoelma: list garden own collection
from app.api.endpoints.lista_rauhoitukset import router as lista_rauhoitukset_router  # lista_rauhoitukset: list protections
api_router.include_router(lista_rauhoitukset_router, prefix="/lista_rauhoitukset", tags=["ListaRauhoitukset"])  # lista_rauhoitukset: list protections
from app.api.endpoints.lista_siemenia_jaljella import router as lista_siemenia_jaljella_router  # lista_siemenia_jaljella: list seeds left
api_router.include_router(lista_siemenia_jaljella_router, prefix="/lista_siemenia_jaljella", tags=["ListaSiemeniaJaljella"])  # lista_siemenia_jaljella: list seeds left
from app.api.endpoints.lista_sopimukset import router as lista_sopimukset_router  # lista_sopimukset: list agreements
api_router.include_router(lista_sopimukset_router, prefix="/lista_sopimukset", tags=["ListaSopimukset"])  # lista_sopimukset: list agreements
from app.api.endpoints.lista_status import router as lista_status_router  # lista_status: list status
api_router.include_router(lista_status_router, prefix="/lista_status", tags=["ListaStatus"])  # lista_status: list status
from app.api.endpoints.lista_tarkastaja import router as lista_tarkastaja_router  # lista_tarkastaja: list inspector
api_router.include_router(lista_tarkastaja_router, prefix="/lista_tarkastaja", tags=["ListaTarkastaja"])  # lista_tarkastaja: list inspector
from app.api.endpoints.lista_tarkastajanimi import router as lista_tarkastajanimi_router  # lista_tarkastajanimi: list_inspector_names
api_router.include_router(lista_tarkastajanimi_router, prefix="/lista_tarkastajanimi", tags=["ListaTarkastajanimi"])  # lista_tarkastajanimi: list_inspector_names
from app.api.endpoints.lista_tuulenkestavyys import router as lista_tuulenkestavyys_router  # lista_tuulenkestavyys: list wind hardiness
api_router.include_router(lista_tuulenkestavyys_router, prefix="/lista_tuulenkestavyys", tags=["ListaTuulenkestavyys"])  # lista_tuulenkestavyys: list wind hardiness
from app.api.endpoints.lista_varsi import router as lista_varsi_router  # lista_varsi: list stem
api_router.include_router(lista_varsi_router, prefix="/lista_varsi", tags=["ListaVarsi"])  # lista_varsi: list stem
from app.api.endpoints.lista_viherrakentamiskaytto import router as lista_viherrakentamiskaytto_router  # lista_viherrakentamiskaytto: list landscape use
api_router.include_router(lista_viherrakentamiskaytto_router, prefix="/lista_viherrakentamiskaytto", tags=["ListaViherrakentamiskaytto"])  # lista_viherrakentamiskaytto: list landscape use
from app.api.endpoints.lista_viljelyn_tarkoitus import router as lista_viljelyn_tarkoitus_router  # lista_viljelyn_tarkoitus: list cultivation purpose
api_router.include_router(lista_viljelyn_tarkoitus_router, prefix="/lista_viljelyn_tarkoitus", tags=["ListaViljelynTarkoitus"])  # lista_viljelyn_tarkoitus: list cultivation purpose
from app.api.endpoints.lista_ymparistoindikaattoriluonne import router as lista_ymparistoindikaattoriluonne_router  # lista_ymparistoindikaattoriluonne: list environmental indicator trait
api_router.include_router(lista_ymparistoindikaattoriluonne_router, prefix="/lista_ymparistoindikaattoriluonne", tags=["ListaYmparistoindikaattoriluonne"])  # lista_ymparistoindikaattoriluonne: list environmental indicator trait
from app.api.endpoints.lukitut_taulut import router as lukitut_taulut_router  # lukitut_taulut: locked_tables
api_router.include_router(lukitut_taulut_router, prefix="/lukitut_taulut", tags=["LukitutTaulut"])  # lukitut_taulut: locked_tables
from app.api.endpoints.maailman_levinneisyysalue import router as maailman_levinneisyysalue_router  # maailman_levinneisyysalue: world_distribution_area
api_router.include_router(maailman_levinneisyysalue_router, prefix="/maailman_levinneisyysalue", tags=["MaailmanLevinneisyysalue"])  # maailman_levinneisyysalue: world_distribution_area
from app.api.endpoints.maaritysmerkinta import router as maaritysmerkinta_router  # maaritysmerkinta: identification_entry
api_router.include_router(maaritysmerkinta_router, prefix="/maaritysmerkinta", tags=["Maaritysmerkinta"])  # maaritysmerkinta: identification_entry
from app.api.endpoints.muunkielinen_nimi import router as muunkielinen_nimi_router  # muunkielinen_nimi: foreign_language_name
api_router.include_router(muunkielinen_nimi_router, prefix="/muunkielinen_nimi", tags=["MuunkielinenNimi"])  # muunkielinen_nimi: foreign_language_name
from app.api.endpoints.naytetieto import router as naytetieto_router  # naytetieto: specimen_data
api_router.include_router(naytetieto_router, prefix="/naytetieto", tags=["Naytetieto"])  # naytetieto: specimen_data
from app.api.endpoints.naytetietoja import router as naytetietoja_router  # naytetietoja: specimen_information
api_router.include_router(naytetietoja_router, prefix="/naytetietoja", tags=["Naytetietoja"])  # naytetietoja: specimen_information
from app.api.endpoints.osastopaikka import router as osastopaikka_router  # osastopaikka: section_location
api_router.include_router(osastopaikka_router, prefix="/osastopaikka", tags=["Osastopaikka"])  # osastopaikka: section_location
from app.api.endpoints.puutarhassa_viljelyn_tarkoitus import router as puutarhassa_viljelyn_tarkoitus_router  # puutarhassa_viljelyn_tarkoitus: garden cultivation purpose
api_router.include_router(puutarhassa_viljelyn_tarkoitus_router, prefix="/puutarhassa_viljelyn_tarkoitus", tags=["PuutarhassaViljelynTarkoitus"])  # puutarhassa_viljelyn_tarkoitus: garden cultivation purpose
from app.api.endpoints.sijoituspaikka import router as sijoituspaikka_router  # sijoituspaikka: placement location
api_router.include_router(sijoituspaikka_router, prefix="/sijoituspaikka", tags=["Sijoituspaikka"])  # sijoituspaikka: placement location
from app.api.endpoints.suomalainen_kasvupaikka import router as suomalainen_kasvupaikka_router  # suomalainen_kasvupaikka: finnish_growing_site
api_router.include_router(suomalainen_kasvupaikka_router, prefix="/suomalainen_kasvupaikka", tags=["SuomalainenKasvupaikka"])  # suomalainen_kasvupaikka: finnish_growing_site
from app.api.endpoints.suomalainen_levinneisyysalue import router as suomalainen_levinneisyysalue_router  # suomalainen_levinneisyysalue: finnish_distribution_area
api_router.include_router(suomalainen_levinneisyysalue_router, prefix="/suomalainen_levinneisyysalue", tags=["SuomalainenLevinneisyysalue"])  # suomalainen_levinneisyysalue: finnish_distribution_area
from app.api.endpoints.suunniteltu_kasvupaikka import router as suunniteltu_kasvupaikka_router  # suunniteltu_kasvupaikka: planned_growing_site
api_router.include_router(suunniteltu_kasvupaikka_router, prefix="/suunniteltu_kasvupaikka", tags=["SuunniteltuKasvupaikka"])  # suunniteltu_kasvupaikka: planned_growing_site
from app.api.endpoints.synonyymi import router as synonyymi_router  # synonyymi: synonym
api_router.include_router(synonyymi_router, prefix="/synonyymi", tags=["Synonyymi"])  # synonyymi: synonym
from app.api.endpoints.taksoni import router as taksoni_router  # taksoni: taxon
api_router.include_router(taksoni_router, prefix="/taksoni", tags=["Taksoni"])  # taksoni: taxon
from app.api.endpoints.taksonin_lappu import router as taksonin_lappu_router  # taksonin_lappu: taxon_label
api_router.include_router(taksonin_lappu_router, prefix="/taksonin_lappu", tags=["TaksoninLappu"])  # taksonin_lappu: taxon_label
from app.api.endpoints.taksonin_viljelytiedot import router as taksonin_viljelytiedot_router  # taksonin_viljelytiedot: taxon_cultivation_data
api_router.include_router(taksonin_viljelytiedot_router, prefix="/taksonin_viljelytiedot", tags=["TaksoninViljelytiedot"])  # taksonin_viljelytiedot: taxon_cultivation_data
from app.api.endpoints.tarkastusmerkinta import router as tarkastusmerkinta_router  # tarkastusmerkinta: inspection_entry
api_router.include_router(tarkastusmerkinta_router, prefix="/tarkastusmerkinta", tags=["Tarkastusmerkinta"])  # tarkastusmerkinta: inspection_entry
from app.api.endpoints.toimenpide import router as toimenpide_router  # toimenpide: action
api_router.include_router(toimenpide_router, prefix="/toimenpide", tags=["Toimenpide"])  # toimenpide: action
from app.api.endpoints.viite import router as viite_router  # viite: reference
api_router.include_router(viite_router, prefix="/viite", tags=["Viite"])  # viite: reference
from app.api.endpoints.ymparistoindikaattoriluonne import router as ymparistoindikaattoriluonne_router  # ymparistoindikaattoriluonne: environmental indicator trait
api_router.include_router(ymparistoindikaattoriluonne_router, prefix="/ymparistoindikaattoriluonne", tags=["Ymparistoindikaattoriluonne"])  # ymparistoindikaattoriluonne: environmental indicator trait
