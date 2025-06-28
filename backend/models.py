from pydantic import BaseModel, Field

class Student(BaseModel):
    full_name: str
    parent_phone: str
    student_phone: str
    class_name: str
    address: str
    school: str
    age: int = Field(ge=0)  # ensures age is >= 0

