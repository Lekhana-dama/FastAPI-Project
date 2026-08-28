import time
from fastapi import FastAPI,Request
from database import engine
from database_models.student_models import Base
from database_models.course_models import CourseDB
from database_models.enrollment_models import EnrollmentDB
from routers.students import router as student_router
from routers.course import router as course_router
from routers.enrollment import router as enrollment_router
from routers.user import router as user_router
from routers.upload import router as upload_router
from routers.websocket import router as webscoket_router
from exceptions import custom_exceptions
from exceptions import exception_handlers
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from cache.redis_cache  import get_cache,set_cache,delete_cache

app=FastAPI()

app.mount("/uploads",StaticFiles(directory="uploads"),name="uploads")

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
app.include_router(upload_router)
app.include_router(webscoket_router)


@app.middleware("http")
async def log_request_time(request:Request,call_next):
    start_time=time.time()
    response=await call_next(request)
    process_time=time.time()-start_time
    response.headers["X-Process-Time"]=str(process_time)
    return response
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.middleware("http")
async def security_header(request:Request,call_next):
    response= await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    return response

@app.get("/cache-test")
def cache_test():
    set_cache("test_user",{
        "id":1,
        "name":"LEkhana"
    })
    value=get_cache("test_user")
    return{
        "cached_data":value
    }