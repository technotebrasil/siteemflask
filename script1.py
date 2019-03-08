#Importar dependências
from flask import Flask

#Cria uma instância em Flask
app = Flask(__name__)

#Define rota e homepage
@app.route("/")
def home():
    return render_template("home.html")

#Define 2 rota e conteúdo
@app.route("/blog")
def about():
    return render_template("blog.html")

#Executando e controlando o script
if (__name__ =="__main__"):
    app.run(debug=True)
