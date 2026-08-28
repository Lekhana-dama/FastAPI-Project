from pydantic import BaseModel,ConfigDict
class Student(BaseModel):
    #this line tells :I am allowed to create this model from an object's attributes.
    model_config=ConfigDict(from_attributes=True)
    id:int
    name:str
    branch:str
    year:int
