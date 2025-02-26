'''
Configuration module for connecting to the database.
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:alexfango04@localhost:3309/bd_prueba"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()
def get_db():
    """
    Establishes a connection to the database and ensures it gets closed once the operation is completed.
    """
    db = config.db.SessionLocal()
    try:
        print("Conectando a la base de datos...")
        yield db
    finally:
        db.close()
        print("Conexión cerrada.")