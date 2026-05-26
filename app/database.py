from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import DATABASE_URL

# Configure engine differently depending on the URL/dialect.
# Avoid passing MySQL-specific `connect_args` to SQLite (which raises
# TypeError: Connection() got an unexpected keyword argument 'connect_timeout').
is_sqlite = DATABASE_URL.startswith("sqlite:")

if is_sqlite:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        echo=False,
    )
else:
    # MySQL (or other) connection options
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=2,
        pool_recycle=1800,
        echo=False,
        connect_args={
            "connect_timeout": 10,
            "read_timeout": 30,
            "write_timeout": 30,
        },
    )


# Set session-level timeout to kill slow queries (MySQL-specific)
if not is_sqlite:
    @event.listens_for(engine, "connect")
    def set_mysql_timeout(dbapi_conn, connection_record):
        cursor = dbapi_conn.cursor()
        try:
            cursor.execute("SET SESSION max_execution_time=30000")  # 30s limit per query
            cursor.execute("SET SESSION net_read_timeout=30")
            cursor.execute("SET SESSION net_write_timeout=30")
        finally:
            cursor.close()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
