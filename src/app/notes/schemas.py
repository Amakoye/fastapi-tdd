from pydantic import BaseModel


class NoteBaseSchema(BaseModel):
    title: str
    description: str


class NoteSchema(NoteBaseSchema):
    id: int
