import requests


class PokeClient:
    def __init__(self, url: str):
        self.url = url

    def find(self, name: str):
        result = requests.get(self.url + name)
        result.raise_for_status()
        return result
