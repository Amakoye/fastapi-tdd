from ..schemas import NoteBaseSchema, NoteSchema
from ..models import Notes
from sqlalchemy.orm import Session


async def post(payload: NoteBaseSchema, db: Session):
    note = Notes(title=payload.title, description=payload.description)
    db.add(note)
    db.commit()
    return note


async def get(id: int, db: Session):
    note = db.query(Notes).filter(Notes.id == id).first()
    return note


async def get_all(db: Session):
    notes = db.query(Notes).all()
    return notes


async def put(id: int, payload: NoteBaseSchema, db: Session):
    note = db.query(Notes).filter(Notes.id == id).first()

    if not note:
        return None

    note.title = payload.title
    note.description = payload.description

    db.commit()
    return note


async def delete(id: int, db: Session):
    db.query(Notes).filter(Notes.id == id).delete()
    db.commit()
    return
