import uvicorn 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from entities.Salary import *

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SalaryModel(BaseModel):
    salary: float

@app.get("/api/v1/healtz")
def healtz():
    return {"status": "running"}

@app.post("/api/v1/salary")
def calcSalary(salary: SalaryModel):
    client = Salary(salary.salary)
    client.netSalaryCalc()
    return client.toString()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info")