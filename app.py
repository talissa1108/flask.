# ========================================================== 
# O Flask possibilita a junção de python com js, html e css
# ==========================================================

# Flask = cria o servidor Web
# render_template = cria a página html
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #Rota
def home():
    return render_template("index.html") #Cria a página html

#Codigo roda apenas quando executa esse arquivo diretamente
if __name__ == "__main__": 
    # Inicia o servidor e debugTrue vê erros e atualiza a página
    app.run(debug=True)