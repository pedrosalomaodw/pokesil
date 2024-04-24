import requests

"""
versão: 1.0.1
perfil Facebook: Pedro Josué Salomão DW


"""

"""parametros que precisam ter:
evoluções, imagem,  genero"""

"""evolucoes 
    https://pokeapi.co/api/v2/evolution-chain/{id}/
    """


try:
    class PokeDados():

        def __init__(self, nome_pokemon):

            self.nome_pokemon = nome_pokemon
            api_poke = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.nome_pokemon}")

            self.api_poke_json = api_poke.json()

        def habilidades(self):
            for x in range(0,1+1):
                self.habilidades_pokemon = self.api_poke_json["abilities"][x]["ability"]["name"]
                print(self.habilidades_pokemon)
            
        def altura(self):
            self.altura = self.api_poke_json["height"]
            print(self.altura)

        def peso(self):
            self.peso = self.api_poke_json["weight"]
            print(float(self.peso))
        
        def id_pokemon(self):
            self.id_pokemon = self.api_poke_json["id"]
            global id_pokemon_funcao
            id_pokemon_funcao = self.id_pokemon

            print(self.id_pokemon)
            return id_pokemon_funcao

        
        def tipo(self):
            self.tipo = self.api_poke_json["types"][0]["type"]["name"]
            print(self.tipo)
        
        #def genero(self):
            #self.genero = self.api_poke_json[""]
            #print(self.genero)


except  Exception as error:
    print("está dando erro no:", error)




