from fastapi import APIRouter,Depends
from dependencies import admin_only

router=APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard")
def admin_dashboard(admin= Depends(admin_only)):
    return{
        "message":"Welcome Admin",
        "admin_email":admin.email
    }
