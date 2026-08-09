from fastapi import FastAPI
from database import engine
from database_models.student_models import Base
from database_models.course_models import CourseDB
from database_models.enrollment_models import EnrollmentDB
from routers.students import router as student_router
from routers.course import router as course_router
from routers.enrollment import router as enrollment_router
from routers.user import router as user_router
from exceptions import custom_exceptions
from exceptions import exception_handlers

app=FastAPI()
app.add_exception_handler(custom_exceptions.StudentNotFoundException,exception_handlers.student_not_found_handler)
app.add_exception_handler(custom_exceptions.StudentAlreadyExistsException,exception_handlers.student_already_exists_handler)
app.add_exception_handler(custom_exceptions.CourseNotFoundException,exception_handlers.course_not_found_handler)
app.add_exception_handler(custom_exceptions.CourseAlreadyExistsException,exception_handlers.course_already_exists_handler)
app.add_exception_handler(custom_exceptions.EnrollmentNotFoundException,exception_handlers.enrollment_not_found_handler)
app.add_exception_handler(custom_exceptions.EnrollmentAlreadyExistsException,exception_handlers.enrollment_already_exists_handler)

Base.metadata.create_all(bind=engine)
app.include_router(student_router)
app.include_router(course_router)
app.include_router(enrollment_router)
app.include_router(user_router)
"""@app.get("/hello")
def hello():
    return {"message":"Hello welcome on board"}
@app.get("/about")
def about():
    return {
        "name":"lekhana",
        "city":"hyd"
        }
"""
    
