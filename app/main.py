from ast import Return
from cgitb import text
from hashlib import new
from http.client import FOUND
from importlib.resources import contents
from pydoc import ModuleScanner
from sqlite3 import Cursor
from turtle import title
from typing import Optional, List
from urllib import response
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor 
import time
from . import models, schemas, utils
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host = "localhost", database= "fastapi", user= "postgres", password = "Aviati@123", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection succesful")
        break
    except Exception as error:
        print("Connecting to databse failed")
        print("Error: ", error)
        time.sleep(2)



my_posts = [{"title": "title 1", "content": "content 1", "id": 1}, {"title": "fav foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

def find_index_post(id):
    for i , p in enumerate(my_posts):
        if p["id"] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return { "message": "Hello World"}




