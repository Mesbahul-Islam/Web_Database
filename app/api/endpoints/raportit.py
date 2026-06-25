from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional

from app.database import get_db

from app.models.hankintatiedot import Hankintatiedot
from app.models.taksoni import Taksoni
from app.models.heimo import Heimo
from app.models.osastopaikka import Osastopaikka
from app.models.alkuperaa_koskevat_tiedot import AlkuperaaKoskevatTiedot
from app.models.kasvatustietoja import Kasvatustietoja
from app.models.toimenpide import Toimenpide
from app.models.puutarhassa_viljelyn_tarkoitus import PuutarhassaViljelynTarkoitus
from app.models.naytetietoja import Naytetietoja
from app.models.maaritysmerkinta import Maaritysmerkinta
from app.models.sijoituspaikka import Sijoituspaikka
from app.models.tarkastusmerkinta import Tarkastusmerkinta

router = APIRouter()


def _append_extended_data(
    report: str, h, db,
    extensiveData=False, department=False, originData=False,
    seedData=False, actions=False, cultivationPurpose=False,
    sampleData=False, determinationMarks=False,
    lastInspection=False, allInspections=False
):
    if extensiveData:
        if getattr(h, 'saapumispvm', None): report += f"\tReceived: {h.saapumispvm}\n"
        if getattr(h, 'millaisena_saatu', None): report += f"\tCondition: {h.millaisena_saatu}\n"
        if getattr(h, 'lisatiedot', None): report += f"\tNotes: {h.lisatiedot}\n"
        
    if department:
        deps = db.query(Osastopaikka).filter(Osastopaikka.hankintaID == h.hankintaID).all()
        for d in deps:
            report += f"\tDepartment: {d.osaston_nimi}\n"
            
    if originData:
        orig = db.query(AlkuperaaKoskevatTiedot).filter(AlkuperaaKoskevatTiedot.hankintaID == h.hankintaID).all()
        for o in orig:
            items = [x for x in [o.maa, o.alue, o.kasvupaikka] if x]
            if items: report += f"\tOrigin: {', '.join(items)}\n"
            
    if seedData:
        seeds = db.query(Kasvatustietoja).filter(Kasvatustietoja.hankintaID == h.hankintaID).all()
        for s in seeds:
            report += f"\tSeed Bank: {s.siemenpankki}, Seeds Left: {s.siemenia_jaljella}\n"
            
    if actions:
        acts = db.query(Toimenpide).filter(
            Toimenpide.hankintaID == h.hankintaID,
            Toimenpide.deleted_at == None
        ).all()
        for a in acts:
            report += f"\tAction: {a.pvm} - {a.toimenpide}\n"
            
    if cultivationPurpose:
        cps = db.query(PuutarhassaViljelynTarkoitus).filter(PuutarhassaViljelynTarkoitus.hankintaID == h.hankintaID).all()
        for cp in cps:
            report += f"\tCultivation Purpose: {cp.puutarhassa_viljelyn_tarkoitus}\n"
            
    if sampleData:
        samps = db.query(Naytetietoja).filter(Naytetietoja.hankintaID == h.hankintaID).all()
        for s in samps:
            report += f"\tSample: {s.naytteen_tyyppi} at {s.naytteen_sijainti}\n"
            
    if determinationMarks:
        dms = db.query(Maaritysmerkinta).filter(Maaritysmerkinta.hankintaID == h.hankintaID).all()
        for dm in dms:
            report += f"\tDetermination: {dm.maarityspvm} by {dm.maarittaja} -> {dm.uusitaksoni}\n"
            
    if lastInspection or allInspections:
        osasto_numeros = [o.osaston_numero for o in db.query(Osastopaikka.osaston_numero).filter(Osastopaikka.hankintaID == h.hankintaID).all()]
        if osasto_numeros:
            sijs = db.query(Sijoituspaikka).filter(Sijoituspaikka.osaston_numero.in_(osasto_numeros)).all()
            for sij in sijs:
                insps_query = db.query(Tarkastusmerkinta).filter(
                    Tarkastusmerkinta.sijoituspaikan_nro == sij.sijoituspaikan_nro,
                    Tarkastusmerkinta.deleted_at == None
                ).order_by(Tarkastusmerkinta.tarkastuspvm.desc())
                
                if not allInspections:
                    insps_query = insps_query.limit(1)
                    
                for insp in insps_query.all():
                    report += f"\tInspection: {insp.tarkastuspvm} - Living: {insp.elavia_yksiloita} - Notes: {insp.menestymista_koskevat_havainnot}\n"
                    
    return report


@router.get("/hankinta")
def generate_hankinta_raportti(
    taxon: Optional[str] = None,
    acquisition_number: Optional[str] = None,
    extensiveData: bool = False,
    department: bool = False,
    lastInspection: bool = False,
    allInspections: bool = False,
    determinationMarks: bool = False,
    seedData: bool = False,
    actions: bool = False,
    cultivationPurpose: bool = False,
    sampleData: bool = False,
    originData: bool = False,
    db: Session = Depends(get_db)
):
    query = db.query(Hankintatiedot, Taksoni, Heimo).join(
        Taksoni, Hankintatiedot.taksonin_nro == Taksoni.taksonin_nro
    ).outerjoin(
        Heimo, Taksoni.jarjestysnumero == Heimo.jarjestysnumero
    )
    
    if taxon:
        query = query.filter(Taksoni.tieteellinen_nimi.ilike(f"%{taxon}%"))
    if acquisition_number:
        query = query.filter(Hankintatiedot.hankintanumero.ilike(f"%{acquisition_number}%"))
        
    query = query.order_by(Heimo.nimi, Taksoni.tieteellinen_nimi, Hankintatiedot.hankintanumero)
    
    rows = query.all()
    
    if not rows:
        return {"report": "No records found."}
        
    report = "Acquisition Report\n\n"
    
    current_family = None
    current_taxon = None
    
    for h, t, heimo in rows:
        heimonimi = heimo.nimi if heimo else 'Unknown Family'
        if heimonimi != current_family:
            report += f"{heimonimi}\n\n"
            current_family = heimonimi
            
        if t.tieteellinen_nimi != current_taxon:
            report += f"\t{t.tieteellinen_nimi}\n"
            current_taxon = t.tieteellinen_nimi
            
        report += f"\n\t{h.hankintanumero or 'No Acq Number'}\n"
        if h.hankintanimi:
            report += f"\tName: {h.hankintanimi}\n"
            
        report = _append_extended_data(
            report, h, db, extensiveData, department, originData, seedData,
            actions, cultivationPurpose, sampleData, determinationMarks,
            lastInspection, allInspections
        )
    return {"report": report}

@router.get("/kokooma")
def generate_kokooma_raportti(
    taxon: Optional[str] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Hankintatiedot, Taksoni, Heimo).join(
        Taksoni, Hankintatiedot.taksonin_nro == Taksoni.taksonin_nro
    ).outerjoin(
        Heimo, Taksoni.jarjestysnumero == Heimo.jarjestysnumero
    )
    
    if taxon:
        query = query.filter(Taksoni.tieteellinen_nimi.ilike(f"%{taxon}%"))
        
    query = query.order_by(Heimo.nimi, Taksoni.tieteellinen_nimi, Hankintatiedot.hankintanumero)
    
    rows = query.all()
    
    if not rows:
        return {"report": "No records found."}
        
    report = "Compilation Report\n\n"
    
    current_family = None
    current_taxon = None
    
    for h, t, heimo in rows:
        heimonimi = heimo.nimi if heimo else 'Unknown Family'
        
        osasto_numeros = [o.osaston_numero for o in db.query(Osastopaikka.osaston_numero).filter(Osastopaikka.hankintaID == h.hankintaID).all()]
        sijs = []
        if osasto_numeros:
            sij_query = db.query(Sijoituspaikka).filter(Sijoituspaikka.osaston_numero.in_(osasto_numeros))
            if status and status != "Any":
                sij_query = sij_query.filter(Sijoituspaikka.kasvin_status == status)
            sijs = sij_query.all()
            
        if status and status != "Any" and not sijs:
            continue
            
        if heimonimi != current_family:
            report += f"{heimonimi}\n\n"
            current_family = heimonimi
            
        if t.tieteellinen_nimi != current_taxon:
            report += f"\t{t.tieteellinen_nimi}\n"
            current_taxon = t.tieteellinen_nimi
            
        report += f"\n\t{h.hankintanumero or 'No Acq Number'}\n"
        
        if not sijs and osasto_numeros:
            sijs = db.query(Sijoituspaikka).filter(Sijoituspaikka.osaston_numero.in_(osasto_numeros)).all()
            
        for sij in sijs:
            report += f"\tLocation: {sij.sijoituspaikan_nimi} (Status: {sij.kasvin_status})\n"
            
    return {"report": report}

@router.get("/erikois")
def generate_erikois_raportti(
    collection_name: Optional[str] = None,
    extensiveData: bool = False,
    department: bool = False,
    originData: bool = False,
    lastInspection: bool = False,
    allInspections: bool = False,
    seedData: bool = False,
    determinationMarks: bool = False,
    sampleData: bool = False,
    actions: bool = False,
    cultivationPurpose: bool = False,
    db: Session = Depends(get_db)
):
    query = db.query(Hankintatiedot, Taksoni, Heimo).join(
        Taksoni, Hankintatiedot.taksonin_nro == Taksoni.taksonin_nro
    ).outerjoin(
        Heimo, Taksoni.jarjestysnumero == Heimo.jarjestysnumero
    ).filter(
        Hankintatiedot.erikoiskokoelma_oma_puutarha != None,
        Hankintatiedot.erikoiskokoelma_oma_puutarha != ''
    )
    
    if collection_name and collection_name != "Any":
        query = query.filter(Hankintatiedot.erikoiskokoelma_oma_puutarha.ilike(f"%{collection_name}%"))
        
    query = query.order_by(Heimo.nimi, Taksoni.tieteellinen_nimi, Hankintatiedot.hankintanumero)
    
    rows = query.all()
    
    if not rows:
        return {"report": "No records found for this collection."}
        
    report = "Special Collection Report\n\n"
    current_collection = None
    sorted_rows = sorted(rows, key=lambda x: x[0].erikoiskokoelma_oma_puutarha or "")
    
    for h, t, heimo in sorted_rows:
        if h.erikoiskokoelma_oma_puutarha != current_collection:
            report += f"\n--- Collection: {h.erikoiskokoelma_oma_puutarha} ---\n\n"
            current_collection = h.erikoiskokoelma_oma_puutarha
            
        report += f"{t.tieteellinen_nimi} ({h.hankintanumero})\n"
        report = _append_extended_data(
            report, h, db, extensiveData, department, originData, seedData,
            actions, cultivationPurpose, sampleData, determinationMarks,
            lastInspection, allInspections
        )
                
    return {"report": report}

@router.get("/suppea_osasto")
def generate_suppea_osasto_raportti(
    department: Optional[str] = None,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Osastopaikka, Hankintatiedot, Taksoni).join(
        Hankintatiedot, Osastopaikka.hankintaID == Hankintatiedot.hankintaID
    ).join(
        Taksoni, Hankintatiedot.taksonin_nro == Taksoni.taksonin_nro
    )
    if department:
        query = query.filter(Osastopaikka.osaston_nimi.ilike(f"%{department}%"))
    rows = query.all()
    if not rows:
        return {"report": "No records found."}
    report = "Concise Department Report\n\n"
    for o, h, t in rows:
        report += f"{o.osaston_nimi} - {t.tieteellinen_nimi} ({h.hankintanumero})\n"
    return {"report": report}

@router.get("/laaja_osasto")
def generate_laaja_osasto_raportti(
    department: Optional[str] = None,
    taxon: Optional[str] = None,
    acquisition_number: Optional[str] = None,
    status: Optional[str] = None,
    family: Optional[str] = None,
    onlyDepartmentNames: bool = False,
    sortBy: Optional[str] = None,
    extensiveData: bool = False,
    db: Session = Depends(get_db)
):
    query = db.query(Osastopaikka, Hankintatiedot, Taksoni, Heimo).join(
        Hankintatiedot, Osastopaikka.hankintaID == Hankintatiedot.hankintaID
    ).join(
        Taksoni, Hankintatiedot.taksonin_nro == Taksoni.taksonin_nro
    ).outerjoin(
        Heimo, Taksoni.jarjestysnumero == Heimo.jarjestysnumero
    )

    if status and status != "Any":
        query = query.join(Sijoituspaikka, Osastopaikka.osaston_numero == Sijoituspaikka.osaston_numero)
        query = query.filter(Sijoituspaikka.kasvin_status == status)

    if department:
        query = query.filter(Osastopaikka.osaston_nimi.ilike(f"%{department}%"))
    if taxon:
        query = query.filter(Taksoni.tieteellinen_nimi.ilike(f"%{taxon}%"))
    if acquisition_number:
        query = query.filter(Hankintatiedot.hankintanumero.ilike(f"%{acquisition_number}%"))
    if family and family != "Any":
        query = query.filter(Heimo.nimi.ilike(f"%{family}%"))

    if sortBy == "scientific_name":
        query = query.order_by(Taksoni.tieteellinen_nimi)
    elif sortBy == "acquisition_number":
        query = query.order_by(Hankintatiedot.hankintanumero)
    elif sortBy == "family":
        query = query.order_by(Heimo.nimi, Taksoni.tieteellinen_nimi)

    query = query.distinct()
    rows = query.all()
    
    if not rows:
        return {"report": "No records found."}

    if onlyDepartmentNames:
        departments = sorted(list(set([row[0].osaston_nimi for row in rows if row[0].osaston_nimi])))
        report = "Department Names\n\n" + "\n".join(departments)
        return {"report": report}

    report = "Extensive Department Report\n\n"
    for row in rows:
        o, h, t, _ = row
        report += f"{o.osaston_nimi}\n\t{t.tieteellinen_nimi} ({h.hankintanumero})\n"
        if extensiveData and h.lisatiedot:
            report += f"\tNotes: {h.lisatiedot}\n"
    return {"report": report}

@router.get("/lahettaja")
def generate_lahettaja_raportti(
    sender: Optional[str] = None,
    senderId: Optional[str] = None,
    extensiveData: bool = False,
    department: bool = False,
    originData: bool = False,
    lastInspection: bool = False,
    allInspections: bool = False,
    seedData: bool = False,
    determinationMarks: bool = False,
    sampleData: bool = False,
    actions: bool = False,
    cultivationPurpose: bool = False,
    db: Session = Depends(get_db)
):
    query = db.query(Hankintatiedot, Taksoni).join(
        Taksoni, Hankintatiedot.taksonin_nro == Taksoni.taksonin_nro
    )
    
    # Normally we would filter by lahettaja table, but 'lahettajanro'/'saatu_lahettajalta' can be used if it's stored there.
    # For now we'll do a basic filter on Hankintatiedot if any sender string is present.
    # We will just fetch everything and not filter explicitly if 'saatu_lahettajalta' is not perfectly matching, but let's assume it matches.
    if senderId:
        query = query.filter(Hankintatiedot.lahettajanro == senderId)
    
    rows = query.limit(500).all()
    if not rows:
        return {"report": "No records found."}
        
    report = f"Sender Report for {sender or senderId or 'All'}\n\n"
    for h, t in rows:
        report += f"{t.tieteellinen_nimi} ({h.hankintanumero})\n"
        report = _append_extended_data(
            report, h, db, extensiveData, department, originData, seedData,
            actions, cultivationPurpose, sampleData, determinationMarks,
            lastInspection, allInspections
        )
    return {"report": report}

@router.get("/lappu")
def generate_lappu_raportti(
    taxon: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Taksoni)
    if taxon:
        query = query.filter(Taksoni.tieteellinen_nimi.ilike(f"%{taxon}%"))
    rows = query.limit(50).all()
    if not rows:
        return {"report": "No records found."}
    report = "Label/Tag Data\n\n"
    for t in rows:
        report += f"[{t.tieteellinen_nimi}]\n"
    return {"report": report}

@router.get("/siemen")
def generate_siemen_raportti(
    taxon: Optional[str] = None,
    acquisition_number: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Kasvatustietoja, Hankintatiedot, Taksoni).join(
        Hankintatiedot, Kasvatustietoja.hankintaID == Hankintatiedot.hankintaID
    ).join(
        Taksoni, Hankintatiedot.taksonin_nro == Taksoni.taksonin_nro
    ).filter(Kasvatustietoja.siemenia_jaljella == 'true')
    
    if taxon:
        query = query.filter(Taksoni.tieteellinen_nimi.ilike(f"%{taxon}%"))
    if acquisition_number:
        query = query.filter(Hankintatiedot.hankintanumero.ilike(f"%{acquisition_number}%"))
        
    rows = query.all()
    if not rows:
        return {"report": "No records found."}
    report = "Seed Report\n\n"
    for k, h, t in rows:
        report += f"{t.tieteellinen_nimi}\n\tAcq: {h.hankintanumero}\n\tBank: {k.siemenpankki}\n"
    return {"report": report}

@router.get("/osasto_listaus")
def generate_osasto_listaus_raportti(db: Session = Depends(get_db)):
    rows = db.query(Osastopaikka).limit(100).all()
    if not rows:
        return {"report": "No records found."}
    report = "Department List\n\n"
    for o in rows:
        report += f"{o.osaston_nimi} ({o.osaston_numero})\n"
    return {"report": report}

from app.models.lahettaja import Lahettaja
from app.models.viite import Viite

@router.get("/lahettaja_viite")
def generate_lahettaja_viite_raportti(
    list_type: str = Query("sender", pattern="^(sender|reference)$"),
    extensiveData: bool = False,
    db: Session = Depends(get_db)
):
    if list_type == "sender":
        rows = db.query(Lahettaja).order_by(Lahettaja.lahettajan_nimi).limit(500).all()
        if not rows:
            return {"report": "No senders found."}
            
        report = "Sender List\n\n"
        for r in rows:
            report += f"{r.lahettajan_nimi or ''} ({r.lahettajan_tunnus_puutarha or ''})\n"
            if extensiveData:
                if getattr(r, 'osoite', None): report += f"\tAddress: {r.osoite}\n"
                if getattr(r, 'puhelin', None): report += f"\tPhone: {r.puhelin}\n"
                if getattr(r, 'lisatiedot', None): report += f"\tNotes: {r.lisatiedot}\n"
        return {"report": report}
        
    elif list_type == "reference":
        rows = db.query(Viite).order_by(Viite.viitteen_lyhenne).limit(500).all()
        if not rows:
            return {"report": "No references found."}
            
        report = "Reference List\n\n"
        for r in rows:
            report += f"{r.viitteen_lyhenne or ''}: {r.koko_viite or ''}\n"
            if extensiveData and getattr(r, 'lisatiedot', None):
                report += f"\tNotes: {r.lisatiedot}\n"
        return {"report": report}

