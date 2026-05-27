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

Edit `.env` with your database and authentication settings (see [Environment Variables](#environment-variables) section below).

### 3. Initialize Database

**Option A: Use Local SQLite (Default)**

SQLite is the default database. No additional setup required—just ensure the directory exists:

```bash
mkdir -p ./sqlite-backup
```

The app will automatically use `./sqlite-backup/puutarhakanta2005.sqlite`.

To load data into SQLite from a MySQL dump:

```bash
# Convert MySQL dump to SQLite (requires sqlite3 CLI installed)
sqlite3 ./sqlite-backup/puutarhakanta2005.sqlite < puutarhakanta2005_schema.sql
```

Or use Python to restore from backup:

```bash
python3 -c "
import sqlite3
from app.database import engine
conn = sqlite3.connect('./sqlite-backup/puutarhakanta2005.sqlite')
with open('puutarhakanta2005_schema.sql', 'r') as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
print('SQLite database initialized')
"
```

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

## Database Setup Details

### SQLite Setup

The default database is SQLite, which requires no separate server installation.

**Initialize from schema:**

```bash
mkdir -p ./sqlite-backup
sqlite3 ./sqlite-backup/puutarhakanta2005.sqlite < puutarhakanta2005_schema.sql
```

**Verify tables created:**

```bash
sqlite3 ./sqlite-backup/puutarhakanta2005.sqlite ".tables"
```

**Restore from existing backup:**

```bash
# If you have a .sqlite file, just copy it
cp /path/to/backup.sqlite ./sqlite-backup/puutarhakanta2005.sqlite
```

**Query the database directly:**

```bash
sqlite3 ./sqlite-backup/puutarhakanta2005.sqlite
sqlite> SELECT COUNT(*) FROM taksoni;
sqlite> .quit
```

### MySQL Setup

For Docker MySQL development:

```bash
mkdir -p ./db-backups
cp puutarhakanta2005_schema.sql ./db-backups/
docker compose up -d mysql
```

Restore schema after container starts:

```bash
mysql -h127.0.0.1 -P3306 -utarkastususer -ptarkastususer puutarhakanta2005 < puutarhakanta2005_schema.sql
```

```bash
mysql -h127.0.0.1 -P3306 -utarkastususer -ptarkastususer -e "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='puutarhakanta2005';"
```

### Connection Verification

Test your database connection before running the app:

```bash
python3 -c "from app.database import engine; print('Connection OK' if engine.connect() else 'Failed')"
```

## Environment Variables

### Database Connection

**For SQLite (Default):**
No database variables needed. The app automatically uses `./sqlite-backup/puutarhakanta2005.sqlite`.

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

MySQL 8 database `puutarhakanta2005`. Schema defined in `puutarhakanta2005_schema.sql`.
Approximately 89 tables, ~11,700 taxa, ~57,000 acquisition records.

## Troubleshooting

### SQLite Issues

**Error: "sqlite3: no such table"**
- Schema not initialized. Run: `sqlite3 ./sqlite-backup/puutarhakanta2005.sqlite < puutarhakanta2005_schema.sql`

**Error: "database is locked"**
- Another process is using the SQLite file
- Stop the app and any other processes accessing `./sqlite-backup/puutarhakanta2005.sqlite`
- Remove lock files: `rm ./sqlite-backup/puutarhakanta2005.sqlite-*`

**Large queries are slow**
- SQLite performs slower on large datasets. Consider switching to MySQL for production
- Add indexes: See `puutarhakanta2005_schema.sql` for index definitions

### MySQL Connection Errors

**Error: "Can't connect to MySQL server"**
- Ensure Docker container is running: `docker compose ps mysql`
- Check credentials in `.env` match container setup
- Verify MySQL is listening: `nc -zv 127.0.0.1 3306`

**Error: "Access denied for user"**
- Verify `DB_USER` and `DB_PASSWORD` in `.env`
- Check user exists in MySQL: `mysql -u root -p -e "SELECT user FROM mysql.user;"`

**Error: "Unknown database"**
- Restore schema: `mysql -h127.0.0.1 -utarkastususer -ptarkastususer < puutarhakanta2005_schema.sql`

### Application Startup Issues

**Error: "JWT token is invalid" or "SECRET_KEY not set"**
- Set `SECRET_KEY` in `.env` (minimum 32 characters)
- Restart the application after changing `.env`

**App defaults to SQLite instead of MySQL**
- Check that `DATABASE_URL` is not set (or contains SQLite path)
- Verify database connection vars in `.env` are being loaded: `python3 -c "from app.core.config import DB_HOST; print(DB_HOST)"`

## Switching Between SQLite and MySQL

### From SQLite to MySQL

```bash
# 1. Set MySQL credentials in .env
nano .env
# DB_HOST=127.0.0.1
# DB_PORT=3306
# DB_NAME=puutarhakanta2005
# DB_USER=tarkastususer
# DB_PASSWORD=tarkastususer

# 2. Initialize MySQL schema
docker compose up -d mysql
mysql -h127.0.0.1 -P3306 -utarkastususer -ptarkastususer puutarhakanta2005 < puutarhakanta2005_schema.sql

# 3. Restart the app (it will auto-detect MySQL credentials)
fastapi dev
```

### From MySQL to SQLite

```bash
# 1. Remove or comment out database vars in .env
nano .env
# DB_HOST=localhost  # Comment these out
# DB_PORT=3306

# 2. Initialize SQLite database
mkdir -p ./sqlite-backup
sqlite3 ./sqlite-backup/puutarhakanta2005.sqlite < puutarhakanta2005_schema.sql

# 3. Restart the app (it will use SQLite by default)
fastapi dev
```

### Testing

Run tests with:
```bash
pytest -v
```

Tests validate CRUD operations, auth flow, and OpenAPI contract.
