from fastapi import APIRouter
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
from schemas.user import User

user_router = APIRouter()

@user_router.post('/login', tags = ['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(content=token, status_code=200)