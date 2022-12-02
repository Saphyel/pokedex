import json

from clients import PokeClient
from repositories import PokemonRepository
from schema import Pokemon, PokemonCreate


class PokemonService:
    def __init__(self, repository: PokemonRepository, client: PokeClient):
        self.repository = repository
        self.client = client

    def find(self, name: str) -> Pokemon:
        return Pokemon(**self.repository.find(name=name).__dict__)

    def create(self, name: str) -> str:
        result = self.client.find(name)
        obj_in = result.json()
        obj_in["abilities"] = json.dumps(obj_in["abilities"])
        return self.repository.create(obj_in=PokemonCreate(**obj_in))
