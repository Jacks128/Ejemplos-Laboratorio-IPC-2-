from tkinter.tix import Tree
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

from gestor import Gestor
from xml.etree import ElementTree as ET

app = Flask(__name__)
app.config["DEBUG"]=True

CORS(app)

gestor=Gestor()

@app.route('/')
def home():
    return "Esta corriendo bien mi API"

@app.route('/login/<user>/<password>')
def login(user=None,password=None):
    res = gestor.obtener_usuario(user,password)
    if res==None:
        return {'data':False,'message':'Usuario no encontrado o erroneo'}
    return {'data':True}

@app.route('/agregarCancion',methods=['POST'])
def agregarCancion():
    json=request.get_json()
    gestor.agregar_cancion(json['name'],json['artist'],json['image'],json['album'])
    return jsonify({'ok':True,'message':'Cancion añadida con exito'}),200

@app.route('/agregarCanciones',methods=['POST'])
def agregarCanciones():
    xml=request.data.decode('utf-8')
    raiz=ET.XML(xml)
    for elemento in raiz:
        gestor.agregar_cancion(elemento.attrib['name'],elemento.attrib['artist'],elemento.attrib['image'],elemento.text)
    return jsonify({'ok':True,'message':'Canciones cargadas con exito'}),200

@app.route('/canciones',methods=['GET'])
def get_canciones():
    c=gestor.obtener_canciones()
    return jsonify(c),200

if __name__ =="__main__":
    app.run(debug=True)

