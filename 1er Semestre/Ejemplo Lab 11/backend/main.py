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
    return "Esta corriendo bien bro"

@app.route('/login/<user>/<password>')
def login(user=None,password=None):
    res = gestor.obtener_usuario(user,password)
    if res == None:
        return '{"data":false}'
    return '{"data":true}'

#Agregar cancion
@app.route('/agregarCancion',methods=['POST'])
def agregarCancion():
    json=request.get_json()
    gestor.agregar_cancion(json['name'],json['artist'],json['image'],json['album'])
    return jsonify({'ok':True, 'data':'Cancion añadida con exito'}),200

#Cargar Archivo
@app.route('/agregarCanciones',methods=['POST'])
def agregarCanciones():
    xml=request.data.decode('utf-8')
    raiz=ET.XML(xml)
    for elemento in raiz:
        gestor.agregar_cancion(elemento.attrib['name'],elemento.attrib['artist'],elemento.attrib['image'],elemento.text)
    return jsonify({'ok':True,'data':'Canciones cargadas con exito'}),200

#Obtener Canciones
@app.route('/canciones',methods=['GET'])
def get_canciones():
    c=gestor.obtener_canciones()
    return jsonify(c),200

#Iniciar el servidor
if __name__ == "__main__":
    app.run(debug=True)    
