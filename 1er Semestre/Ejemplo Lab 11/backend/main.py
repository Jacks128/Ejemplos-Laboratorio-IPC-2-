from tkinter.tix import Tree
from flask import Flask, request, jsonify
from flask_cors import CORS

from gestor import Gestor

app = Flask(__name__)
app.config["DEBUG"]=True

CORS(app)

gestor=Gestor()

@app.route('/')
def home():
    return "Esta corriendo bien bro"

@app.route('/login/<user>/<password>')
def login(user=None,password=None):
    res = gestor.obtener_usuario(user,password)
    if res == None:
        return '{"data":false}'
    return '{"data":true}'

#Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)    
