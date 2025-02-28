from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Todo

app = FastAPI()

@app.get("/")
def hello():
	return {"message": "Hello World"}
	
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
	return db.query(Todo).all()