from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from Db.SQLAlchemy.Func import get_all_days, add_day, update_day, delete_day
from DTO.DTO import DTO

router = APIRouter()

@router.get("/")
def root():
    return FileResponse("Html/User.html", media_type="text/html")

@router.get("/user")
def user():
    return RedirectResponse("/", status_code=302)

@router.get("/authorization/{passw}")
def authorization(passw: int):
    if passw != 123:
        return JSONResponse(status_code=403, content={"detail": "Payment Required"})
    
    return RedirectResponse("/admin", status_code=302)

@router.get("/admin")
def admin():
    return FileResponse("Html/Admin.html", media_type="text/html")

@router.get("/days")
def read_days():
    days = get_all_days()
    return days

@router.post("/admin/day")
def create_day(dto: DTO):
    day = add_day(dto)
    return day

@router.put("/admin/day")
def chenge_day(dto: DTO):
    day = update_day(dto)
    if day == None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Day not found")
    return day

@router.delete("/admin/day/{id}")
def remove_day(id: int):
    day = delete_day(id)
    if day == None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Day not found")
    return day