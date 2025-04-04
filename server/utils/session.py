import urllib.parse
from typing import Any
from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from .settings import get_settings

class DBSession:
    engine: Engine
    session: Session
  
    def __init__(self):
        settings = get_settings()
        
        connect_str = f"postgresql://{settings.db_username}:{urllib.parse.quote(settings.db_password)}@{settings.db_url}:{settings.db_port}/{settings.db_database}"
        self.engine = create_engine(connect_str)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        
        
    def get_db(self):
        db = self.session()
        try:
            yield db
        finally:
            db.close()
