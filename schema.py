from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, Json


class PokemonCreate(BaseModel):
    id: int
    name: str
    abilities: Json
    weight: int
    location_area_encounters: str
    captured: datetime = Field(default_factory=datetime.utcnow)


class Pokemon(BaseModel):
    id: int
    name: str
    abilities: List
    weight: int
    location_area_encounters: str
    captured: datetime = Field(default_factory=datetime.utcnow)
