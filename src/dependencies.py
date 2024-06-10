

from src.database import engine, session_local
from sqlalchemy.orm import Session
from typing import List , Annotated
from fastapi import  Depends
from src import models

def set_up_migrations():
    models.Base.metadata.create_all(bind=engine)
   

def get_db():
    db= session_local()
    try:
        yield db
    finally:
        db.close()

database=Annotated[Session,Depends(get_db)]
