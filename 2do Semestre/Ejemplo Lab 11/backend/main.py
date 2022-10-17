from flask import Flask, Flask,request
from flask.json import jsonify
from flask_cors import CORS

from gestor import Gestor

app=Flask(__name__)
app.config["DEBUG"]=True

CORS(app)

gestor=Gestor()

@app.route('/')
def home():
    return "Los alumnos de IPC2 B van a ganar"

@app.route('/login/<user>/<password>')
def login(user=None,password=None):
    res=gestor.obtener_usuario(user,password)
    if res==None:
        return '{"data":false,"message":"Tu usuario no existe o es invalido"}'
    return '{"data":true,"message":"Bienvenido"}'
    
@app.route('/login')
def login2():
    json=request.get_json()
    res=gestor.obtener_usuario(json['user'],json['password'])
    if res==None:
        return jsonify({"data":False,"message":"Tu usuario no existe o es invalido"})
    return jsonify({"data":True,"message":"Bienvenido"})
    


if __name__ == "__main__":
    app.run(debug=True)    
