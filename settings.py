from pydantic import BaseSettings


class Settings(BaseSettings):
    db_uri: str
    poke_url: str


settings = Settings()
