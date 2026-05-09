from fastapi import HTTPException,APIRouter,Query,Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Note
from dependencies import get_current_user


router= APIRouter(prefix="/notes", tags=["Notes"])


@router.get("/")
def get_notes(
    search:str |None=Query(None,description="Search notes"),
    limit:int =Query(10,ge=1, le=100),
    offset:int =Query(10,ge=1,le=100),
    db:Session= Depends(get_db),
    user= Depends(get_current_user)

):
    query=db.query(Note).filter(Note.owner_id==user.id)

    if search:
        query=query.filter(Note.title.ilike(f"%{search}%"))

    notes= query.offset(offset).limit(limit).all()


    return {
        "count":len(notes),
        "data":notes
    }
