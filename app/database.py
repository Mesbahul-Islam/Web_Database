from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import DATABASE_URL

# Optimize for large result sets with connection timeouts and query limits
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,                  # Reduced connection pool to prevent resource exhaustion
    max_overflow=2,               # Minimal overflow connections
    pool_recycle=1800,            # Recycle connections every 30 min
    echo=False,                   # Disable SQL logging for performance
    connect_args={
        "connect_timeout": 10,    # Connection timeout: 10 seconds
        "read_timeout": 30,       # Read timeout: 30 seconds
        "write_timeout": 30,      # Write timeout: 30 seconds
    }
)

# Set session-level timeout to kill slow queries
@event.listens_for(engine, "connect")
def set_mysql_timeout(dbapi_conn, connection_record):
    cursor = dbapi_conn.cursor()
    cursor.execute("SET SESSION max_execution_time=30000")  # 30 second hard limit per query
    cursor.execute("SET SESSION net_read_timeout=30")
    cursor.execute("SET SESSION net_write_timeout=30")
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
