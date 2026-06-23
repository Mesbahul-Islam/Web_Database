import sys
import os
import datetime

# Add the current directory to the path so we can import the app modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app.models.toimenpide import Toimenpide

def main():
    db = SessionLocal()
    try:
        print("Fetching toimenpide records from the database...")
        records = db.query(Toimenpide).filter(Toimenpide.uus_pvm.isnot(None)).all()
        
        updates = []
        for record in records:
            raw_date = str(record.uus_pvm).strip()
            if not raw_date or raw_date == "0000-00-00" or raw_date == "0" or raw_date == "None":
                continue
                
            parsed_date = None
            try:
                parsed_date = datetime.datetime.fromisoformat(raw_date)
            except ValueError:
                # Handle edge cases where the date is just a 4-digit year like "2005"
                if len(raw_date) == 4 and raw_date.isdigit():
                    try:
                        parsed_date = datetime.datetime(int(raw_date), 1, 1)
                    except ValueError:
                        pass

            if parsed_date:
                updates.append({
                    "toimenpide_nro": record.toimenpide_nro,
                    "created_at": parsed_date,
                    "updated_at": parsed_date
                })

        total = len(updates)
        print(f"Found {total} records with valid uus_pvm dates. Beginning bulk update...")
        
        if updates:
            # We batch the updates in chunks of 2000 to prevent locking the database
            batch_size = 2000
            for i in range(0, total, batch_size):
                batch = updates[i:i+batch_size]
                # SQLAlchemy's bulk_update_mappings is highly optimized for PostgreSQL
                db.bulk_update_mappings(Toimenpide, batch)
                db.commit()
                print(f"-> Updated {min(i+batch_size, total)} / {total} records...")
                
        print("\nMigration completely successful!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()
