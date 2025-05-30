from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    birthdays = relationship("Birthday", back_populates="user")
    meetings = relationship("Meeting", back_populates="user")
    todos = relationship("Todo", back_populates="user")
    suggestions = relationship("Suggestion", back_populates="user")

class Birthday(Base):
    __tablename__ = "birthdays"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    date = Column(DateTime)
    user = relationship("User", back_populates="birthdays")

class Meeting(Base):
    __tablename__ = "meetings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    datetime = Column(DateTime)
    location = Column(String)
    description = Column(String)
    user = relationship("User", back_populates="meetings")

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    due_date = Column(DateTime)
    completed = Column(Boolean, default=False)
    user = relationship("User", back_populates="todos")

class Suggestion(Base):
    __tablename__ = "suggestions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("User", back_populates="suggestions")
