from pydantic import BaseModel, constr
from datetime import datetime

class Note(BaseModel):
    title: str
    body: str
    

class NoteDisp(BaseModel):
    id: int
    title: str
    body: str 
    datetime: datetime

    class Config:
        orm_mode = True
