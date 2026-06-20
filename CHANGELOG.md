# Changelog & Features

This document outlines the recent features, architectural changes, and improvements made to the Puutarhakanta API.

## Recent Features & Architectural Upgrades

### 1. Universal Database Compatibility (Alembic)
- **Seamless SQLite & PostgreSQL Support:** The API can now perfectly toggle between SQLite (for local development) and PostgreSQL (for production) just by changing the `DATABASE_URL` in the `.env` file.
- **Alembic Migrations:** Database schemas are now strictly managed by Alembic (`alembic upgrade head`). 
- **Dynamic Constraint Handling:** Alembic dynamically uses `render_as_batch=True` for SQLite and turns it off for PostgreSQL, ensuring schema constraints (like Foreign Keys) are perfectly preserved in both environments.
- **Explicit SQLAlchemy Naming Conventions:** Added explicit constraint naming conventions to SQLAlchemy metadata so PostgreSQL doesn't generate random constraint names that break future Alembic migrations.

### 2. Robust Application Configuration (`pydantic-settings`)
- **Strict Startup Validation:** Migrated configuration from `os.getenv` to `pydantic-settings`. The application will now refuse to start up if critical environment variables (like `DATABASE_URL` or `SECRET_KEY`) are missing, instantly catching deployment misconfigurations.
- **Unified Config Model:** All constants (JWT settings, DB config) are now safely type-checked and routed through `app.core.config.settings`.

### 3. Production Security & Stability
- **Global Exception Handlers:** Intercepts raw database crashes (like `sqlalchemy.exc.IntegrityError` when someone tries to create a duplicate user) and transforms them into clean, descriptive `409 Conflict` JSON responses.
- **API Rate Limiting (`slowapi`):** Integrated a strict `@limiter.limit("5/minute")` decorator onto the `POST /api/auth/token` endpoint. This permanently prevents automated brute-force attacks against user accounts.
- **Built-in Endpoint Pagination:** Ensured all `GET` endpoints utilize slicing (`page`, `page_size`) to prevent massive payloads from crashing Vercel's serverless edge functions.

### 4. Vercel Serverless Optimization
- Intentionally maintained synchronous SQLAlchemy. In a Vercel deployment where every HTTP request spins up an isolated serverless function instance, synchronous connection behavior is significantly more stable than async poolers.

## Developer Experience
- **Dependency Management:** Upgraded instructions to use `uv` for near-instant package installation.
- **Auto-Increment Repairs:** Standardized how `Integer, primary_key=True` models behave. When Alembic runs `upgrade head`, they flawlessly map to `AUTOINCREMENT` in SQLite and `IDENTITY` sequences in PostgreSQL.
