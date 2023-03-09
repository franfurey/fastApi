
from pydantic import BaseModel, Field
from typing import Optional
from middlewares.jwt_bearer import *

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field (default= 'Mi pelicula')
    year: int = Field(default = 2022, le = 2023)
    rating: float = Field(default = 5, ge= 1, le=10)
    category: str = Field (default = 'Categoria',min_length = 5, max_length = 25)

    class Config:
        schema_extra = {
            'example': {
                'id':1,
                'title': 'AA7',
                'year':2022,
                'rating':10,
                'category': 'Accion'
            }
        }