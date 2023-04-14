from sqlalchemy import String, Column, Integer, DateTime
from sqlalchemy.orm import relationship
from notesapp import db
from datetime import datetime

class Note(db.Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    body = Column(String)
    datetime = Column(DateTime, default=datetime.now)

    def __init__(self, title, body) -> None:
        self.title = title
        self.body = body

