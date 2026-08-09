from pydantic import BaseModel
class Student(BaseModel):
    id:int
    name:str
    branch:str
    year:int
