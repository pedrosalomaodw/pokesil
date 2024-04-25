import os
import requests

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

    def salvar_info_arquivo(self, pokemon_data):
        if pokemon_data:
            nome_arquivo = f"{self.nome_pokemon.lower()}.txt"
            try:
                with open(nome_arquivo, "w") as arquivo:
                    arquivo.write(f"Nome do Pokémon: {self.nome_pokemon}\n")
                    self.habilidades(pokemon_data)
                    self.altura(pokemon_data)
                    self.peso(pokemon_data)
                    self.id_pokemon(pokemon_data)
                    self.tipo(pokemon_data)
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
    print("\033[1;32;40mPPPPPPP      OOOOO     K     K       EEEEEEEEEE     SSSSSSSSS      IIIIIII     L      ")
    print("P      P    O     O    K    K        E              S                 I        L       ")
    print("P      P    O     O    K   K         E              S                 I        L       ")
    print("PPPPPPP     O     O    KKKK          EEEEEEEEEE     SSSSSSSSS         I        L       ")
    print("P           O     O    K   K         E                       S        I        L       ")
    print("P           O     O    K    K        E                       S        I        L       ")
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
            pokemon.habilidades(pokemon_data)
            pokemon.altura(pokemon_data)
            pokemon.peso(pokemon_data)
            pokemon.id_pokemon(pokemon_data)
            pokemon.tipo(pokemon_data)
            pokemon.salvar_info_arquivo(pokemon_data)
        if not reiniciar_programa():
            break

if __name__ == "__main__":
    main()
            
