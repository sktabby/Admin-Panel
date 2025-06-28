from fastapi import FastAPI
from models import Student
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# replace the url with your actual mongodb atlas id
client = MongoClient("mongodb+srv://Tabish:Aqsashah7272@cluster1.4lodgpx.mongodb.net/")
db = client["admin_db"]
students_collection = db["students"]

@app.post("/students")
async def add_student(student: Student):
    student_dict = student.dict()
    student_dict["custom_id"] = generate_custom_id()
    result = students_collection.insert_one(student_dict)
    return {"message": "Student added", "id": str(result.inserted_id)}

def generate_custom_id():
    count = students_collection.count_documents({})
    return f"wasimsir@{count + 1}"
