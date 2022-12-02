from typing import List

from sqlalchemy import select, insert
from sqlalchemy.orm.session import Session
from models import Pokemon
from schema import PokemonCreate


class PokemonRepository:
    def __init__(self, db: Session):
        self.db = db

    def find(self, *, name: str) -> Pokemon:
        query = select(Pokemon).where(Pokemon.name == name)
        result = self.db.execute(query)
        return result.unique().scalar_one()

    def create(self, *, obj_in: PokemonCreate) -> str:
        try:
            query = insert(Pokemon).values(obj_in.dict()).returning(Pokemon.name)
            result = self.db.execute(query)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        return result.scalar_one()
