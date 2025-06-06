from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.deps import get_db
from app.models import Birthday
from app.schemas import BirthdayCreate, BirthdayOut
from app.api.users import get_current_user

router = APIRouter()

@router.get('/', response_model=list[BirthdayOut])
def list_birthdays(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Birthday).filter(Birthday.user_id == user.id).all()

@router.post('/', response_model=BirthdayOut)
def create_birthday(birthday: BirthdayCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_birthday = Birthday(user_id=user.id, name=birthday.name, date=birthday.date)
    db.add(db_birthday)
    db.commit()
    db.refresh(db_birthday)
    return db_birthday

@router.patch('/{birthday_id}', response_model=BirthdayOut)
def update_birthday(birthday_id: int, birthday: BirthdayCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_birthday = db.query(Birthday).filter(Birthday.id == birthday_id, Birthday.user_id == user.id).first()
    if not db_birthday:
        raise HTTPException(status_code=404, detail="Birthday not found")
    db_birthday.name = birthday.name
    db_birthday.date = birthday.date
    db.commit()
    db.refresh(db_birthday)
    return db_birthday

@router.delete('/{birthday_id}')
def delete_birthday(birthday_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    birthday = db.query(Birthday).filter(Birthday.id == birthday_id, Birthday.user_id == user.id).first()
    if not birthday:
        raise HTTPException(status_code=404, detail="Birthday not found")
    db.delete(birthday)
    db.commit()
    return {"ok": True}
