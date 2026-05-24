# Puutarhakanta API (PT2.4)

REST API for the Finnish botanical garden plant collection database (*puutarhakanta2005*).

## What It Does

Provides read-only access to a botanical garden's plant records:
- Taxa (species, varieties, cultivars)
- Acquisitions (how/when/from-whom plants were obtained)
- Physical garden locations and inspection records
- Taxonomic classification data
- Specimen and seed bank records
- International conservation agreement data

## Quick Start

```bash
cp .env.example .env
# Edit .env with your MySQL credentials

#create virtual environment and activate. Please make changes for Windows.
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
fastapi dev
```

## Docker MySQL

Use the bundled MySQL service for local development. Start the database container with:

```bash
docker compose up -d mysql
```

Mount a local directory `./db-backups` into the container and place any initial SQL dump (or init scripts) there. The container's initialization scripts will run files found in the init directory.

Recommended workflow:

- Create the backups folder (if missing):

```bash
mkdir -p ./db-backups
```

- Put your SQL dump(s) or initialization scripts into `./db-backups`. Typical names: `backup.sql`, `init.sql`, or `restore.sh` (make sure scripts are executable).
- Start the container: `docker compose up -d mysql`

The compose file exposes the database on localhost. Point the app at the container with these environment vars (example):

```bash
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=puutarhakanta2005
DB_USER=tarkastususer
DB_PASSWORD=tarkastususer
```

Quick verification (counts tables after a restore):

```bash
mysql -h127.0.0.1 -P3306 -utarkastususer -ptarkastususer -e "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='puutarhakanta2005';"
```

API docs: `http://localhost:8000/docs`

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DB_HOST` | `localhost` | MySQL host |
| `DB_PORT` | `3306` | MySQL port |
| `DB_NAME` | `puutarhakanta2005` | Database name |
| `DB_USER` | `tarkastususer` | MySQL user |
| `DB_PASSWORD` | `tarkastususer` | MySQL password |
| `DATABASE_URL` | _(computed)_ | Full SQLAlchemy URL (overrides above) |

## API Usage

All endpoints follow the same pattern:

```
GET /{resource}/                    → list (supports ?skip=&limit= and any column filter)
GET /{resource}/{primary_key}       → single record
```

### Example requests

```bash
# Get first 10 taxa
GET /taksoni/?limit=10

# Filter by genus
GET /taksoni/?suku=Rosa

# Get a specific acquisition
GET /hankintatiedot/12345

# Find senders by country
GET /lahettaja/?maa=Suomi
```

## Project Structure

```
app/
├── main.py          FastAPI app
├── database.py      DB session
├── core/config.py   Environment config
├── models/          SQLAlchemy ORM (89 tables)
├── schemas/         Pydantic response schemas
└── api/
    ├── api.py       Router registry
    ├── query.py     Generic filter utility
    └── endpoints/   Route handlers
```

## Database

MySQL 8 database `puutarhakanta2005`. Schema defined in `puutarhakanta2005_schema.sql`.
Approximately 89 tables, ~11,700 taxa, ~57,000 acquisition records.
