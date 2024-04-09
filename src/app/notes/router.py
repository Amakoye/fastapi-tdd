from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.core.db import get_db_session
from .schemas import NoteSchema, NoteBaseSchema
from .services.crud import post, get, get_all, put, delete


notes_router = APIRouter(prefix="/notes", tags=["Notes Endpoint"])


@notes_router.post("/", response_model=NoteSchema, status_code=201)
async def create_note(payload: NoteBaseSchema, db: Session = Depends(get_db_session)):
    response_object = await post(payload, db=db)

    return response_object


@notes_router.get("/{id}/", response_model=NoteSchema, status_code=200)
async def read_note(id: int, db: Session = Depends(get_db_session)):
    note = await get(id=id, db=db)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@notes_router.get("/", response_model=List[NoteSchema], status_code=200)
async def read_all_notes(db: Session = Depends(get_db_session)):
    notes = await get_all(db=db)
    return notes


@notes_router.put("/{id}/", response_model=NoteSchema)
async def update_note(
    id: int, payload: NoteBaseSchema, db: Session = Depends(get_db_session)
):
    print("NOTE ID", id)
    note = await get(id=id, db=db)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    response_object = await put(id, payload=payload, db=db)

    return response_object


@notes_router.delete("/{id}/", response_model=NoteSchema)
async def delete_note(id: int, db: Session = Depends(get_db_session)):
    note = await get(id=id, db=db)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    await delete(id, db=db)

    return note
