from pydantic_models.student_model import Student
from fastapi import Depends,Query,BackgroundTasks, logger
from sqlalchemy.orm import Session
from database_models.student_models import StudentDB
from fastapi import APIRouter
from database import get_db
from services import student_service
from repositories import student_repository
import logging
import logging_config
from exceptions import custom_exceptions
from dependencies import get_current_user,get_current_admin
from cache.redis_cache import get_cache,set_cache,delete_cache

router=APIRouter(prefix="/students",tags=["Students"])
@router.get("/",summary="Get all student",description="Retrieving all students registered in the system")
def student(skip:int=Query(0,ge=0),limit:int=Query(10,ge=1,le=100),
            branch:str|None=None,year:int|None=None,
            sort:str|None=None,
            search:str|None=None,
            db:Session=Depends(get_db),
            current_user=Depends(get_current_user)):
    return student_service.get_all_students(skip,limit,branch,year,sort,search,db)
    
@router.get("/{id}")
def student_by_id(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    cache_key=f"student:{id}"

    cached_student= get_cache(cache_key)

    if cached_student is not None:
        print(f"Cache HIT for %s ",cache_key)
        return cached_student
    print(f"cache MISS for %s",cache_key)
    student=student_repository.get_student_by_id(id,db)

    if student is None:
        raise custom_exceptions.StudentNotFoundException

    student_data={
        "id":student.id,
        "name":student.name,
        "branch":student.branch,
        "year":student.year
    }
    set_cache(cache_key,student_data,expire=60)
    return student_data
    
@router.post("/")
def adding_student(student:Student,db:Session=Depends(get_db),current_admin= Depends(get_current_admin)):
    return student_service.create_student(student,db)

@router.put("/{id}")
def updateing(id:int,student:Student,db:Session=Depends(get_db),current_admin=Depends(get_current_admin)):
   return student_service.update_student(id,student,db)

@router.delete("/{id}")
def deleting(id:int,db:Session=Depends(get_db),current_admin = Depends(get_current_admin)):
    return student_service.delete_student(id,db)

@router.get("/{id}/courses")
def get_student_courses(
    id:int,
    db:Session=Depends(get_db),
    current_user=Depends(get_current_user)
):
    return student_service.get_student_courses(id,db)
