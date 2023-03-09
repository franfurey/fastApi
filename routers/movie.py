from fastapi import APIRouter
from fastapi import  Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import  List
from config.database import Session, engine, Base
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import *
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/', tags = ['movies'], response_model = List[Movie])
def get_movies_by_category(category: str = Query(min_length = 5, max_length = 25)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movie_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content=jsonable_encoder(result))
    return JSONResponse(status_code=200, content= jsonable_encoder(result))

@movie_router.post('/movies', tags=['movies'], response_model = dict, status_code= 201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={'message':'Se ha registrado la pelicula'}, status_code= 201)

@movie_router.put('/movies/{id}', tags = ['movies'], response_model = dict, status_code = 200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message':'No encontrado'})
    MovieService(db).update_movie(id, movie)
    db.commit()
    return JSONResponse(content= {'message': 'Se ha MODIFICADO la pelicula'}, status_code= 200)
        
@movie_router.delete('/movies/{id}', tags = ['movies'], response_model = dict, status_code= 200)
def delete_movie(id: int)-> dict:
    db = Session()
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code = 404, content = {'message':'No encontrado'})
    MovieService(db).delete_movie(id)
    return JSONResponse(content= {'message': 'Se ha ELIMINADO la pelicula'}, status_code= 200)