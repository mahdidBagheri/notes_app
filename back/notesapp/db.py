from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_USERNAME = "postgres"
DATABASE_PASSWORD = "pass"
DATABASE_HOST = "127.0.0.1:5431"
DATABASE_NAME = "notesapp-db"

URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if(__name__ == "__main__"):
    get_db()
