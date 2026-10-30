
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first deployed application!"}

@app.get("/about")
def about():
    return {"message": "This is my Python CI/CD project."}
