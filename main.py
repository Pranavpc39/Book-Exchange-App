from fastapi import FastAPI, APIRouter, Depends, Query
from sqlmodel import Session
from contextlib import asynccontextmanager
from database import create_tables
from routes import books, users

# @asynccontextmanager
# def lifecycle():
#     pass

app = FastAPI(
    title="Book Exchange Application",
    description="",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_tables()


app.include_router(users.router)
app.include_router(books.router)

@app.get("/")
def home():
    return {"message":"Welcome to the Book Exchange API"}