from ..schemas import NoteBaseSchema
from ..models import Notes
from sqlalchemy.orm import Session


async def post(payload: NoteBaseSchema, db: Session):
    note = Notes(title=payload.title, description=payload.description)
    db.add(note)
    db.commit()
    return note
