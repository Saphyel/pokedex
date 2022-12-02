# Pokedex
## Getting Started
### Prerequisites
Requirements:
* Docker-compose

Optional:
* Postman/Insomnia/curl

### Start the project
Inside the container execute:

```commandline
alembic upgrade head
```

To install the testing libraries you need to execute:

```commandline
pip install .[test]
```
and then you can do the normal pytest with coverage:

```commandline
coverage run -m pytest tests/
coverage report -m
```


## Using the project

This project is a Pokedex, so you have an endpoint to fetch a captured Pokemon

`GET http://localhost:8000/pokedex/pikachu`

And other url for capture a new Pokemon:

`PUT http://localhost:8000/pokedex/pikachu`

