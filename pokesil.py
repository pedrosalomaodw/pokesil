import os
import requests

class PokeDados:

    def __init__(self, nome_pokemon):
        self.nome_pokemon = nome_pokemon
        self.api_poke = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.nome_pokemon}")
        self.api_poke_json = self.api_poke.json()

    def habilidades(self):
        for x in range(len(self.api_poke_json["abilities"])):
            habilidade = self.api_poke_json["abilities"][x]["ability"]["name"]
            print(habilidade)
    
    def altura(self):
        altura = self.api_poke_json["height"]
        print(altura)

    def peso(self):
        peso = self.api_poke_json["weight"]
        print(float(peso))
    
    def id_pokemon(self):
        id_pokemon = self.api_poke_json["id"]
        print(id_pokemon)
        return id_pokemon

    def tipo(self):
        tipo = self.api_poke_json["types"][0]["type"]["name"]
        print(tipo)

    def salvar_info_arquivo(self):
        nome_arquivo = f"{self.nome_pokemon.lower()}.txt"
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(f"Nome do Pokémon: {self.nome_pokemon}\n")
            arquivo.write("Habilidades:\n")
            for x in range(len(self.api_poke_json["abilities"])):
                habilidade = self.api_poke_json["abilities"][x]["ability"]["name"]
                arquivo.write(f"- {habilidade}\n")
            arquivo.write(f"Altura: {self.api_poke_json['height']}\n")
            arquivo.write(f"Peso: {self.api_poke_json['weight']}\n")
            arquivo.write(f"ID do Pokémon: {self.api_poke_json['id']}\n")
            arquivo.write(f"Tipo: {self.api_poke_json['types'][0]['type']['name']}\n")

def reiniciar_programa():
    reiniciar = input("Deseja reiniciar o programa? (S/s para sim, outro para não): ").lower()
    return reiniciar == 's'

try:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do console
# Define a cor verde para o texto
print("\033[1;32;40mPPPPPPP      OOOOO     K     K       EEEEEEEEEE     SSSSSSSSS      IIIIIII     L")
print("P      P    O     O    K    K        E              S                 I        L")
print("P      P    O     O    K   K         E              S                 I        L")
print("PPPPPPP     O     O    KKKK          EEEEEEEEEE     SSSSSSSSS         I        L")
print("P           O     O    K   K         E                       S        I        L")
print("P           O     O    K    K        E                       S        I        L")
print("P            OOOOO     K     K       EEEEEEEEEE     SSSSSSSSSS     IIIIIII     LLLLLLLL")
# Restaura a cor padrão do texto
print("\033[0;37;40m")
    print("\nPokeSil: https://github.com/pedrosalomaodw/pokesil/")

    while True:
        nome_pokemon = input("\nDigite o nome do Pokémon: ")
        pokemon = PokeDados(nome_pokemon)
        pokemon.habilidades()
        pokemon.altura()
        pokemon.peso()
        pokemon.id_pokemon()
        pokemon.tipo()
        pokemon.salvar_info_arquivo()
        if not reiniciar_programa():
            break

except Exception as error:
    print("Ocorreu um erro:", error)
