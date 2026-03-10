from pydantic import BaseModel

class ClassBase(BaseModel):
    class_id: str
    class_name: str
    advisor: str


class ClassCreate(ClassBase):
    pass


class StudentBase(BaseModel):
    student_id: str
    name: str
    birth_year: int
    major: str
    gpa: float
    class_id: str


class StudentCreate(StudentBase):
    pass