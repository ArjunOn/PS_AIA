from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, users, birthdays, meetings, todos, suggestions
from app.database import engine
from app import models

app = FastAPI(title="Personal AI Secretary Assistant")

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(birthdays.router, prefix="/birthdays", tags=["birthdays"])
app.include_router(meetings.router, prefix="/meetings", tags=["meetings"])
app.include_router(todos.router, prefix="/todos", tags=["todos"])
app.include_router(suggestions.router, prefix="/suggestions", tags=["suggestions"])
