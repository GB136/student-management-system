import models
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud, schemas
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/students")
def list_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.post("/students")
def add_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.put("/students/{student_id}")
def edit_student(student_id: str, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id, student)

@app.delete("/students/{student_id}")
def remove_student(student_id: str, db: Session = Depends(get_db)):
    crud.delete_student(db, student_id)
    return {"message": "deleted"}

@app.get("/classes")
def list_classes(db: Session = Depends(get_db)):
    return crud.get_classes(db)


@app.post("/classes")
def add_class(class_data: schemas.ClassCreate, db: Session = Depends(get_db)):
    return crud.create_class(db, class_data)

@app.get("/students/search")
def search_students(name: str, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.name.contains(name)).all()

from sqlalchemy import func

@app.get("/stats")
def get_stats(db: Session = Depends(get_db)):

    total_students = db.query(func.count(models.Student.student_id)).scalar()

    avg_gpa = db.query(func.avg(models.Student.gpa)).scalar()

    students_by_major = db.query(
        models.Student.major,
        func.count(models.Student.student_id)
    ).group_by(models.Student.major).all()

    return {
        "total_students": total_students,
        "average_gpa": avg_gpa,
        "students_by_major": students_by_major
    }
import csv
from fastapi.responses import FileResponse
@app.get("/export")
def export_csv(db: Session = Depends(get_db)):

    students = db.query(models.Student).all()

    file_path = "students_export.csv"

    with open(file_path, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "student_id",
            "name",
            "birth_year",
            "major",
            "gpa",
            "class_id"
        ])

        for s in students:
            writer.writerow([
                s.student_id,
                s.name,
                s.birth_year,
                s.major,
                s.gpa,
                s.class_id
            ])

    return FileResponse(file_path, filename="students.csv")