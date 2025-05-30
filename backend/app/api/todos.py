from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db
from app.models import Todo
from app.schemas import TodoCreate, TodoOut
from app.api.users import get_current_user

router = APIRouter()

@router.get('/', response_model=list[TodoOut])
def list_todos(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Todo).filter(Todo.user_id == user.id).all()

@router.post('/', response_model=TodoOut)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_todo = Todo(user_id=user.id, content=todo.content, due_date=todo.due_date, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.patch('/{todo_id}', response_model=TodoOut)
def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.content = todo.content
    db_todo.due_date = todo.due_date
    db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.delete('/{todo_id}')
def delete_todo(todo_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"ok": True}
