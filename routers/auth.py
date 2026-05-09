from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import models,note_schemas
from auth import verify_password,create_access_token,hash_password

router= APIRouter()


@router.post("/login",response_model=note_schemas.Token)
def login(
    form_data:OAuth2PasswordRequestForm=Depends(),
    db:Session=Depends(get_db)

):
    user=db.query(models.User).filter(
        models.User.email==form_data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    if not verify_password(form_data.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    token= create_access_token({"sub":user.email})

    return{
        "access_token":token,
        "token_type": "bearer"

    }


@router.post("/register", status_code=201)
def register(
    user: note_schemas.UserCreate,
    db: Session=Depends(get_db)
):
      
#check if the user already exists
    existing_user=db.query(models.User).filter(models.User.email==user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )
    
    
    new_user=models.User(email=user.email,password=hash_password(user.password),role="user"
    )
   

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    


    return{"message":"user registered successfully"}

