from pydantic import BaseModel
class Course(BaseModel):
    id:int
    course_name:str
    course_code:str
    credits:int
    teacher:str