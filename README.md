# Puutarhakanta API (PT2.4)

REST API for the Finnish botanical garden plant collection database (*puutarhakanta2005*).

## What It Does

Provides full CRUD access to a botanical garden's plant records:
- Taxa (species, varieties, cultivars)
- Acquisitions (how/when/from-whom plants were obtained)
- Physical garden locations and inspection records
- Taxonomic classification data
- Specimen and seed bank records
- International conservation agreement data

Read (GET) operations are public. Write operations (POST/PUT/DELETE) require JWT authentication.

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

Edit `.env` with your database and authentication settings. The app uses `DATABASE_URL` directly, so set it to a SQLAlchemy-compatible connection string for the database you want to use.

### 3. Load the PostgreSQL Dump

The repository includes a PostgreSQL-ready dump at `db-backups/puutarhakanta2005_postgres_data.sql`.

Import it with `psql` using the same `DATABASE_URL` value from `.env`:

```bash
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -f db-backups/puutarhakanta2005_postgres_data.sql
```

If you need to regenerate the dump from the SQLite backup, run:

```bash
python migrate_sqlite_to_pg.py
```

### 4. Run the Application

```bash
fastapi dev
```

API will be available at `http://localhost:8000`

## Database Setup Details

The runtime reads a single database setting: `DATABASE_URL`.

Use a PostgreSQL SQLAlchemy URL for Prisma Postgres or any other compatible PostgreSQL instance:

```bash
postgresql+psycopg2://USER:PASSWORD@HOST:5432/postgres?sslmode=require
```

The application does not branch on `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, or `DB_PASSWORD` at runtime. Keep them out of your local setup unless another tool in your workflow still needs them.

To check the configured database URL, run:

```bash
python3 -c "from app.core.config import DATABASE_URL; print(DATABASE_URL)"
```

## Environment Variables

### Database Connection

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | _(required)_ | Full SQLAlchemy URL for the database connection (for example, `postgresql+psycopg2://user:pass@host:5432/postgres?sslmode=require`) |

### Authentication

| Variable | Default | Description |
|----------|---------|----------|
| `SECRET_KEY` | _(required for auth)_ | Secret key for signing JWT tokens (min 32 characters) |
| `ALGORITHM` | `HS256` | JWT signing algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `15` | JWT token expiration time in minutes |

## API Usage

### Endpoint Patterns

**Read (Public)**:
```
GET /{resource}/                    → list all (supports ?skip=&limit= and any column filter)
GET /{resource}/{primary_key}       → single record
```

**Write (Authentication Required)**:
```
POST /{resource}/                   → create new record (requires Bearer token)
PUT /{resource}/{primary_key}       → update record (requires Bearer token)
DELETE /{resource}/{primary_key}    → delete record (requires Bearer token)
```

### Authentication

To access write operations, include a JWT bearer token in the request header:
```bash
Authorization: Bearer <jwt_token>
```

Obtain a token by logging in:
```bash
POST /auth/token
Content-Type: application/x-www-form-urlencoded

username=<user>&password=<password>
```

### Example Requests

**Read operations (no auth required)**:
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

**Write operations (auth required)**:
```bash
# Create new taxa (requires Bearer token)
POST /taksoni/
Authorization: Bearer <token>
Content-Type: application/json

{"suku": "Rosa", "laji": "canina"}

# Update record
PUT /taksoni/{id}
Authorization: Bearer <token>
Content-Type: application/json

{"suku": "Rosa", "laji": "acicularis"}

# Delete record
DELETE /taksoni/{id}
Authorization: Bearer <token>
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

PostgreSQL database loaded from `db-backups/puutarhakanta2005_postgres_data.sql`.
The dump was generated from the bundled SQLite backup and is intended for Prisma Postgres or any other PostgreSQL-compatible server.

## Troubleshooting

### Database Connection Errors

**Error: "NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres.psycopg2"**
- Make sure `DATABASE_URL` starts with `postgresql+psycopg2://`.

**Error: `psql` import fails on the dump**
- Rebuild the dump with `python migrate_sqlite_to_pg.py` and import the regenerated file.
- Make sure the connection string in `.env` points to the target PostgreSQL database.

### Application Startup Issues

**Error: "JWT token is invalid" or "SECRET_KEY not set"**
- Set `SECRET_KEY` in `.env` (minimum 32 characters)
- Restart the application after changing `.env`

### Testing

Run tests with:
```bash
pytest -v
```

Tests validate CRUD operations, auth flow, and OpenAPI contract.
