from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

DB_URL = "mysql+pymysql://root:123456@localhost:3306/test"

engine = create_engine(DB_URL)

LocalSession = sessionmaker(
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
