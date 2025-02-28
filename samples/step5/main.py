
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Todo
from schemas import TodoCreate, TodoUpdate

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
	
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
	target_todo = db.query(Todo).filter(Todo.id == todo_id).first()
	if todo.title != None:
		target_todo.title = todo.title

	if todo.content != None:
		target_todo.content = todo.content
	
	db.commit()
	return db.query(Todo).all()
	
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
	target_todo = db.query(Todo).filter(Todo.id == todo_id).first()
	db.delete(target_todo)
	db.commit()
	return db.query(Todo).all()