import http.server
import socketserver
import os
from urllib.parse import urlparse, parse_qs
from pokesil import PokeDados  # Importa a classe PokeDados do arquivo pokesil.py

class PokemonInfoHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = """
            <html>
            <head>
                <title>Pokemon Info</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f2f2f2;
                        margin: 0;
                        padding: 0;
                    }
                    .container {
                        width: 50%;
                        margin: 0 auto;
                        padding-top: 50px;
                    }
                    h1 {
                        text-align: center;
                    }
                    form {
                        text-align: center;
                    }
                    input[type=text] {
                        width: 50%;
                        padding: 10px;
                        margin: 5px;
                        border: 1px solid #ccc;
                        border-radius: 4px;
                        box-sizing: border-box;
                    }
                    input[type=submit] {
                        background-color: #4CAF50;
                        color: white;
                        padding: 10px 20px;
                        margin: 5px;
                        border: none;
                        border-radius: 4px;
                        cursor: pointer;
                    }
                    input[type=submit]:hover {
                        background-color: #45a049;
                    }
                </style>
            </head>
            <body>
            <div class="container">
            <h1>Get Pokemon Info</h1>
            <form method="post">
                <label for="pokemon_name">Enter the name of a Pokemon:</label><br>
                <input type="text" id="pokemon_name" name="pokemon_name"><br>
                <input type="submit" value="Submit">
            </form>
            </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        elif self.path.startswith('/pokemon'):
            query_components = parse_qs(urlparse(self.path).query)
            pokemon_name = query_components.get('pokemon_name', [''])[0]
            if pokemon_name:
                pokemon = PokeDados(pokemon_name)
                pokemon_data = pokemon.obter_dados_pokemon()
                if pokemon_data:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    info = f"<h2>Info for {pokemon_name.capitalize()}</h2>"
                    info += "<ul>"
                    info += f"<li><b>Nome:</b> {pokemon_name.capitalize()}</li>"
                    info += f"<li><b>Altura:</b> {pokemon.altura(pokemon_data)}</li>"
                    info += f"<li><b>Peso:</b> {pokemon.peso(pokemon_data)}</li>"
                    info += f"<li><b>ID:</b> {pokemon.id_pokemon(pokemon_data)}</li>"
                    info += f"<li><b>Tipos:</b> {pokemon.tipo(pokemon_data)}</li>"
                    info += "</ul>"
                    self.wfile.write(info.encode('utf-8'))
                else:
                    self.send_error(404, 'Pokemon Not Found')
            else:
                self.send_error(400, 'Bad Request')

    def do_POST(self):
        if self.path == '/':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            pokemon_name = parse_qs(post_data)['pokemon_name'][0]
            if pokemon_name:
                self.send_response(303)
                self.send_header('Location', '/pokemon?pokemon_name=' + pokemon_name)
                self.end_headers()
            else:
                self.send_error(400, 'Bad Request')
        else:
            self.send_error(404, 'Not Found')

def run_server():
    PORT = 8000
    with socketserver.TCPServer(("", PORT), PokemonInfoHandler) as httpd:
        print("Server running at localhost:8000")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
              
