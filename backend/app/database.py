from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# banco SQLite
DATABASE_URL = "sqlite:///./educar.db"

# conexão
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# sessão
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# base dos models
Base = declarative_base()


# dependência para abrir sessão
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()