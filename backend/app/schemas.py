from pydantic import BaseModel, EmailStr
from typing import Optional
import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str]

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: Optional[str]
    class Config:
        orm_mode = True

class BirthdayCreate(BaseModel):
    name: str
    date: datetime.date

class BirthdayOut(BirthdayCreate):
    id: int
    class Config:
        orm_mode = True

class MeetingCreate(BaseModel):
    title: str
    datetime: datetime.datetime
    location: Optional[str]
    description: Optional[str]

class MeetingOut(MeetingCreate):
    id: int
    class Config:
        orm_mode = True

class TodoCreate(BaseModel):
    content: str
    due_date: Optional[datetime.datetime]
    completed: Optional[bool] = False

class TodoOut(TodoCreate):
    id: int
    class Config:
        orm_mode = True

class SuggestionCreate(BaseModel):
    text: str

class SuggestionOut(SuggestionCreate):
    id: int
    created_at: datetime.datetime
    class Config:
        orm_mode = True
