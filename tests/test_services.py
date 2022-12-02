from unittest.mock import Mock

from pytest import mark

from repositories import PokemonRepository
from schema import Pokemon
from services import PokemonService


class TestPokemonService:
    @mark.parametrize(
        ["param", "expect"],
        [("pikachu", Pokemon(name="pikachu", id=25, abilities=[{}], weight=1, location_area_encounters="https://url"))],
    )
    def test_find(self, param: str, expect: Pokemon) -> None:
        result = Mock()
        result.unique.return_value.scalar_one.return_value = expect
        session = Mock()
        session.execute.return_value = result
        assert PokemonService(PokemonRepository(session), Mock()).find(name=param) == expect

    @mark.parametrize(
        ["payload", "expect"],
        [
            (
                {
                    "name": "pikachu",
                    "id": 25,
                    "abilities": [{"ability": {}}],
                    "weight": 1,
                    "location_area_encounters": "https://url",
                },
                "pikachu",
            )
        ],
    )
    def test_create(self, payload: dict, expect: Pokemon) -> None:
        response = Mock()
        response.json.return_value = payload
        client = Mock()
        client.find.return_value = response
        result = Mock()
        result.scalar_one.return_value = expect
        session = Mock()
        session.execute.return_value = result
        assert PokemonService(PokemonRepository(session), client).create(name=payload["name"]) == expect
