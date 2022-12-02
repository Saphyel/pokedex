from flask import Flask, abort, jsonify
from requests.exceptions import HTTPError
from sqlalchemy.exc import NoResultFound, IntegrityError

from clients import PokeClient
from db import session
from repositories import PokemonRepository
from services import PokemonService
from settings import settings

settings = settings

app = Flask(__name__)
service = PokemonService(PokemonRepository(session), PokeClient(settings.poke_url))


@app.route("/pokedex/<name>", methods=["GET"])
def pokedex_find(name: str):
    try:
        return jsonify(service.find(name).dict())
    except NoResultFound:
        abort(404)


@app.route("/pokedex/<name>", methods=["PUT"])
def pokedex_create(name: str):
    try:
        service.create(name)
    except IntegrityError:
        abort(400)
    except HTTPError:
        abort(404)
    return "", 204
