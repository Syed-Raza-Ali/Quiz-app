from sqlmodel import Session, create_engine, SQLModel
from quiz_backend.setting import db_url, test_db_url

connection_string = str(db_url).replace("postgresql", "postgresql+psycopg2")

engine = create_engine(connection_string, echo=True) 

def create_table():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session