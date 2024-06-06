import os
import requests
import json

class PokeDados:

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
            return abilities
        else:
            return None

    def altura(self, pokemon_data):
        if pokemon_data:
            return pokemon_data.get("height") / 10
        else:
            return None

    def peso(self, pokemon_data):
        if pokemon_data:
            return pokemon_data.get("weight") / 10
        else:
            return None
    
    def id_pokemon(self, pokemon_data):
        if pokemon_data:
            return pokemon_data.get("id")
        else:
            return None

    def tipo(self, pokemon_data):
        if pokemon_data:
            types = [type_info['type']['name'] for type_info in pokemon_data.get("types", [])]
            return types
        else:
            return None

    def salvar_info_arquivo(self, pokemon_data):
        if pokemon_data:
            info_pokemon = {
                "habilidades": self.habilidades(pokemon_data),
                "altura": self.altura(pokemon_data),
                "peso": self.peso(pokemon_data),
                "id": self.id_pokemon(pokemon_data),
                "tipo": self.tipo(pokemon_data)
            }
            nome_arquivo = f"{self.nome_pokemon.lower()}.json"
            try:
                with open(nome_arquivo, "w") as arquivo:
                    json.dump(info_pokemon, arquivo, indent=4)
                print(f"As informações foram salvas no arquivo: {nome_arquivo}")
            except IOError as e:
                print(f"Erro ao salvar as informações do Pokémon no arquivo: {e}")
        else:
            print("Não foi possível salvar as informações do Pokémon.")

def reiniciar_programa():
    reiniciar = input("Deseja reiniciar o programa? (S/s para sim, outro para não): ").lower()
    return reiniciar == 's'

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_banner():
    limpar_console()
    print("\033[1;32;40mPPPPPPP      OOOOO     K     K       EEEEEEEEEE     SSSSSSSSS      IIIIIII     L")
    print("P      P    O     O    K    K        E              S                 I        L")
    print("P      P    O     O    K   K         E              S                 I        L")
    print("PPPPPPP     O     O    KKKK          EEEEEEEEEE     SSSSSSSSS         I        L")
    print("P           O     O    K   K         E                       S        I        L")
    print("P           O     O    K    K        E                       S        I        L")
    print("P            OOOOO     K     K       EEEEEEEEEE     SSSSSSSSSS     IIIIIII     LLLLLLLL")
    print("\033[0;37;40m")
    print("\nPokeSil: https://github.com/pedrosalomaodw/pokesil/")

def main():
    imprimir_banner()
    while True:
        nome_pokemon = input("\nDigite o nome do Pokémon: ").lower()
        pokemon = PokeDados(nome_pokemon)
        pokemon_data = pokemon.obter_dados_pokemon()
        if pokemon_data:
            habilidades = pokemon.habilidades(pokemon_data)
            altura = pokemon.altura(pokemon_data)
            peso = pokemon.peso(pokemon_data)
            id_pokemon = pokemon.id_pokemon(pokemon_data)
            tipo = pokemon.tipo(pokemon_data)
            print("Habilidades:", habilidades)
            print("Altura:", altura)
            print("Peso:", peso)
            print("ID do Pokémon:", id_pokemon)
            print("Tipo(s):", tipo)
            pokemon.salvar_info_arquivo(pokemon_data)
        if not reiniciar_programa():
            break

if __name__ == "__main__":
    main()
