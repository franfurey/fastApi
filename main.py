from fastapi import FastAPI, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from utils.jwt_manager import create_token
from config.database import Session, engine, Base
from models.movie import Movie as MovieModel
from sqlalchemy.orm.session import sessionmaker
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import *
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind = engine)
Session = sessionmaker(bind = engine)

movies = [
    {
    'id': 1,
     'title' : 'Los ladrones de Cordoba',
     'year' : '2020',
     'rating': 10,
     'category' : 'Romance Medieval'
     },
    {
    'id': 2,
     'title' : 'Los ladrones de Cordoba',
     'year' : '2020',
     'rating': 10,
     'category' : 'Accion'
     }
]

@app.get('/', tags = ['home'])
def message():
    return HTMLResponse('<h1>Hello Fran</h1>')