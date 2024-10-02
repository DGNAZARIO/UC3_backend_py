from flask import Flask, render_template, request
import mensagens
from atv_aula02.atv05 import mensagem

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST"
        nome = request. form.get("nome")
        mensagem = f"Ola {nome}!\nmensagem: {mensagens.obter_mensagem_aleatoria()}"
    return render_template("imdex.html")

if __name__ == "__main__":
    app.run(debug=True)