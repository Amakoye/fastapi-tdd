from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db_session
from .schemas import NoteSchema, NoteBaseSchema
from .services.crud import post


notes_router = APIRouter(prefix="/notes", tags=["Notes Endpoint"])


@notes_router.post("/", response_model=NoteSchema, status_code=201)
async def create_note(payload: NoteBaseSchema, db: Session = Depends(get_db_session)):
    response_object = await post(payload, db=db)

    return response_object
