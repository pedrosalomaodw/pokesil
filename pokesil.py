import os
import requests

class PokeDados():

    def __init__(self, nome_pokemon):
        self.nome_pokemon = nome_pokemon
        self.api_url = f"https://pokeapi.co/api/v2/pokemon/{self.nome_pokemon.lower()}"

    def obter_dados_pokemon(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao obter dados do Pokémon: {e}")
            return None

    def habilidades(self, pokemon_data):
        if pokemon_data:
            abilities = [ability['ability']['name'] for ability in pokemon_data.get("abilities", [])]
            print("Habilidades:")
            for ability in abilities:
                print("-", ability)
        else:
            print("Não foi possível obter as habilidades do Pokémon.")

    def altura(self, pokemon_data):
        if pokemon_data:
            print("Altura:", pokemon_data.get("height") / 10, "metros")
        else:
            print("Não foi possível obter a altura do Pokémon.")

    def peso(self, pokemon_data):
        if pokemon_data:
            print("Peso:", pokemon_data.get("weight") / 10, "quilogramas")
        else:
            print("Não foi possível obter o peso do Pokémon.")

    def id_pokemon(self, pokemon_data):
        if pokemon_data:
            print("ID do Pokémon:", pokemon_data.get("id"))
            return pokemon_data.get("id")
        else:
            print("Não foi possível obter o ID do Pokémon.")
            return None

    def tipo(self, pokemon_data):
        if pokemon_data:
            types = [type_info['type']['name'] for type_info in pokemon_data.get("types", [])]
            print("Tipo(s):", ", ".join(types))
        else:
            print("Não foi possível obter o tipo do Pokémon.")

