from . import models
from . import schema

from sqlalchemy import update
from typing import List

async def create_new_note(request: schema.Note, database) -> models.Note:
    new_note = models.Note(title=request.title, body=request.body)
    database.add(new_note)
    database.commit()
    database.refresh(new_note)
    return new_note

async def get_all_notes(database) -> List[models.Note]:
    notes = database.query(models.Note).all()
    return notes

async def get_note_by_id(id, database) -> models.Note:
    note = database.query(models.Note).get(id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="note not found")
    
    return note

async def delete_note_by_id(id, database):
    database.query(models.Note).filter(models.Note.id == id).delete()
    database.commit()

async def update_note(id, note, database):
    q = database.query(models.Note)
    f = q.filter(models.Note.id == id)
    u = f.update(values={models.Note.title:note.title,models.Note.body:note.body})
    database.commit()
