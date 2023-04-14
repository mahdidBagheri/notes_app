from fastapi import APIRouter, Depends, status, Response, HTTPException

from sqlalchemy.orm import session
from typing import List

from . import schema
from . import services

from notesapp import db

router = APIRouter(tags=["notes"], prefix="/notes")

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_note(request:schema.Note, database: session = Depends(db.get_db)):
    new_note = await services.create_new_note(request, database)
    return new_note

@router.get('/', response_model=List[schema.NoteDisp])
async def get_all_notes(database: session = Depends(db.get_db)):
    return await services.get_all_notes(database)

@router.get('/{id}', response_model=schema.NoteDisp)
async def get_note_by_id(id: int, database: session = Depends(db.get_db)):
    return await services.get_note_by_id(id, database)

@router.delete('/{note_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_note_by_id(id: int, database: session = Depends(db.get_db)) -> None:
    return await services.delete_note_by_id(id, database)

@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def update_note(id:int, note:schema.Note, database: session = Depends(db.get_db)) -> None:
    return await services.update_note(id, note, database)