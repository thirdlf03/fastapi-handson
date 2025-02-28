from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Todo
from schemas import TodoCreate

app = FastAPI()

@app.get("/")
def hello():
	return {"message": "Hello World"}
	
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
	return db.query(Todo).all()

@app.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
	new_todo = Todo(title = todo.title, content = todo.content)
	db.add(new_todo)
	db.commit()
	return db.query(Todo).all()