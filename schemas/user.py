from fastapi import APIRouter
from fastapi import FastAPI, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from utils.jwt_manager import create_token


class User(BaseModel):
    email: str
    password: str