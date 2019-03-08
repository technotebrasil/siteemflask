#Importar dependências
from flask import Flask

#Cria uma instância em Flask
app = Flask(__name__)

#Define rota
@app.route("/")

#Conteudo
def home():
    return("Home Page")

#Executando e controlando o script
if (__name__ =="__main__"):
    app.run(debug=True)
