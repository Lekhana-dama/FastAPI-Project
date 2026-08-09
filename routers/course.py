from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from dependencies import get_current_user,get_current_admin
from pydantic_models.course_model import Course
from services import course_service
router=APIRouter(prefix="/courses",tags=["Course"])
@router.get("/")
def course(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return course_service.get_all_courses(db)

@router.get("/{id}")
def get_course_by_id(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return course_service.get_course_by_id(id,db)

@router.post("/")
def add_course(course:Course,db:Session=Depends(get_db), current_user=Depends(get_current_admin)):
    return course_service.create_course(course,db)

@router.put("/{id}")
def update_course(id:int,course:Course,db:Session=Depends(get_db),
    current_user=Depends(get_current_admin)):
    return course_service.update_course(id,course,db)

@router.delete("/{id}")
def delete_course(id:int,db:Session=Depends(get_db),
    current_user=Depends(get_current_admin)):
    return course_service.delete_course(id,db)

