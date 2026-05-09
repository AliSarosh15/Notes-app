from fastapi import APIRouter,Depends
from dependencies import get_current_user


router = APIRouter()


@router.get("/profile")
def profile(current_user=Depends(get_current_user)):
    return{
        "id":current_user.id,
        "email":current_user.email
    }

