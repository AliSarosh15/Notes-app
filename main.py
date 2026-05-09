from fastapi import FastAPI,Depends,status
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional,List
from sqlalchemy.orm import Session
from database import engine,get_db,Base
import models
import note_schemas
from routers import auth,users,admin
# print("SCHEMAS FILE:",note_schemas.__file__)
# print("SCHEMAS CONTENTS:",dir(note_schemas))



app=FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(admin.router)

Base.metadata.create_all(bind=engine)





notes=[]


class Note(BaseModel):
    title:str
    content:str


class NoteUpdate(BaseModel):
    title:Optional[str]=None
    content:Optional[str]=None


#Creating a new note





@app.post("/notes",response_model=note_schemas.NoteResponse)
def create_note(note:note_schemas.NoteCreate,db:Session=Depends(get_db)):
    new_note=models.Note(
        title=note.title,
        content=note.content
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


    # note_id=len(notes)+1
    # new_note={
    #     "id":note_id,
    #     "title":note.title,
    #     "content":note.content
    # }
    # notes.append(new_note)
    # return new_note




#reading all the notes 


@app.get("/notes",response_model=list[note_schemas.NoteResponse])
def get_notes(db:Session=Depends(get_db)):
    return db.query(models.Note).all()


#reading only single note


@app.get("/notes/{id}")
def get_note(id:int,db:Session=Depends(get_db)):
    note=db.query(models.Note).filter(models.Note.id==id).first()

    if note is None:
        raise HTTPException(
        status_code=404,
        detail="Note NOT Found"
    )

    return note


# #updating a note (only specific feilds)--PATCH

@app.patch("/notes/{id}")
def update_note(id:int,note_data:note_schemas.Noteupdate,db:Session=Depends(get_db)):
    note=db.query(models.Note).filter(models.Note.id==id).first()


    update_data=note_data.model_dump(exclude_unset=True)

    for key,value in update_data.items():
        setattr(note,key,value)
    
    db.commit()
    db.refresh(note)


    return note


    


    # if note is None:
    #     raise HTTPException(
    #     status_code=404,
    #     detail="Note Not Found"
    # )

    # #partial update
    # if note_data.title is not None:
    #     note.title=note_data.title


    # if note_data.content is not None:
    #     note.content=note_data.content

    # db.commit()
    # db.refresh(note)


    # return note


# #deleting a note

@app.delete("/notes/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_note(id:int,db:Session=Depends(get_db)):
    note= db.query(models.Note).filter(models.Note.id==id).first()
    if note is None:
        raise HTTPException(
        status_code=404,
        detail="Note Not Found"
    )
    db.delete(note)
    db.commit()

    return None

#PUT
@app.put("/notes/{id}")
def update_note_put(
    id:int,
    note_data:note_schemas.Noteupdate,
    db:Session=Depends(get_db)

):
    note=db.query(models.Note).filter(models.Note.id==id).first()

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note Not Found"
            )
    
    #full replacement
    note.title=note_data.title
    note.content=note_data.content

    db.commit()
    db.refresh(note)

    return note





