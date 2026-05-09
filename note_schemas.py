from pydantic import BaseModel
from typing import Optional
from pydantic import EmailStr


class NoteCreate(BaseModel):
    title: str
    content:str

class NoteResponse(NoteCreate):
    id:int


    class Config:
        from_attributes=True

class Noteupdate(BaseModel):
    title: Optional[str]=None
    content:Optional[str]=None


class Token(BaseModel):
    access_token:str
    token_type:str

class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserResponse(BaseModel):
    id: int
    email:EmailStr
    role:str

    class config:
        from_attributes=True

