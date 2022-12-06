from flask import Flask,request
from flask.json import jsonify
from flask_cors import CORS
from urllib3 import Retry

from gestor import Gestor
from xml.etree import ElementTree as ET

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
    
@app.route('/agregarCancion',methods=['POST'])
def agregarCancion():
    json=request.get_json()
    gestor.agregar_cancion(json['name'],json['artist'],json['image'],json['album'])
    return jsonify({'ok':True, 'message':'Cancion añadida al album'}),200

@app.route('/agregarCanciones',methods=['POST'])
def agregarCanciones():
    xml=request.data.decode('utf-8')
    raiz=ET.XML(xml)
    for elemento in raiz:
        gestor.agregar_cancion(elemento.attrib['name'],elemento.attrib['artist'],elemento.attrib['image'],elemento.text)
    return jsonify({"ok":True,"message":'Canciones cargadas con exito' }),200

@app.route('/canciones',methods=['GET'])
def get_canciones():
    songs=gestor.obtener_canciones()
    return jsonify(songs),200

if __name__ == "__main__":
    app.run(debug=True)    
