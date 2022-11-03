

from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
from Categorias import Categorias
from Clientes import Clientes
from Configuraciones import Configuraciones
from Instancias import Instancias
from Funciones import XML
from recurso import CantidadRecurso, Recurso

from gestor import Gestor
read = XML()
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


@app.route('/contenido',methods = ['POST'])
def parseInfo():
    body = request.get_json()
    ruta = body['ruta']
    #content = read.entrada(ruta)
    dirc=read.readXML(ruta)

    return jsonify({'data': ruta,'dict':ruta})
#Cargar Archivo
'''@app.route('/agregarCanciones',methods=['POST'])
def agregarCanciones():
    xml=request.data.decode('utf-8')
    raiz=ET.XML(xml)
    for elemento in raiz:
        gestor.agregar_cancion(elemento.attrib['name'],elemento.attrib['artist'],elemento.attrib['image'],elemento.text)
    return jsonify({'ok':True,'data':'Canciones cargadas con exito'}),200

    archivoLeido =minidom.parse(xml)
    archivoconfig= archivoLeido.getElementsByTagName('recurso')
    
    for configInicial in archivoconfig:
        idrecurso=configInicial.getAttribute('id')
        nombre=configInicial.getElementsByTagName('nombre')[1].childNodes[0].nodeValue
        abreviatura=configInicial.getElementsByTagName('abreviatura')[0].childNodes[0].nodeValue
        metrica=configInicial.getElementsByTagName('metrica')[0].childNodes[0].nodeValue
        tipo=configInicial.getElementsByTagName('tipo')[0].childNodes[0].nodeValue
        valor=configInicial.getElementsByTagName('valorXhora')[0].childNodes[0].nodeValue
        temporalConfig=Recurso(idrecurso,nombre,abreviatura,metrica,tipo,valor)
        gestor.agregar_cancion(temporalConfig)
        listacategorias=configInicial.getElementsByTagName('categoria')

        

    for categoria in listacategorias:
        idcategoria=categoria.getAttribute('id')
        nombre=categoria.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
        descripcion=categoria.getElementsByTagName('descripcion')[0].childNodes[0].nodeValue
        carga=categoria.getElementsByTagName('cargaTrabajo')[0].childNodes[0].nodeValue
        temporalConfig=Categorias(idcategoria,nombre,descripcion,carga)
        listaconfiguraciones=categoria.getElementsByTagName('configuracion')        
        
        for configuracion in listaconfiguraciones:
            idconfi=configuracion.getAttribute('id')
            nombre=configuracion.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
            descripcion=configuracion.getElementsByTagName('descripcion')[0].childNodes[0].nodeValue
            temporalConfig=Configuraciones(idconfi,nombre,descripcion)
            recursosconfigurados=configuracion.getElementsByTagName('recurso') 
        
            for recursos in recursosconfigurados:
                idrecursoconfi=recursos.getAttribute('id')
                cantidad=recursos.getElementsByTagName('recurso')[0].childNodes[0].nodeValue
                temporalConfig=CantidadRecurso(idrecursoconfi,cantidad)
                listaclientes=configuracion.getElementsByTagName('cliente')

    for clientes in listaclientes:
        nit=clientes.getAttribute('nit')
        nombre=clientes.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
        usuario=clientes.getElementsByTagName('usuario')[0].childNodes[0].nodeValue
        clave=clientes.getElementsByTagName('clave')[0].childNodes[0].nodeValue
        direccion=clientes.getElementsByTagName('direccion')[0].childNodes[0].nodeValue
        correo=clientes.getElementsByTagName('correoElectronico')[0].childNodes[0].nodeValue

        temporalConfig=Clientes(nit,nombre,usuario,clave,direccion,correo)
        listainstancia=configuracion.getElementsByTagName('instancia') 

        for instancia in listainstancia:
            idinstancia=instancia.getAttribute('id')
            idconfi=instancia.getElementsByTagName('idConfiguracion')[0].childNodes[0].nodeValue
            nombre=instancia.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
            inicio=instancia.getElementsByTagName('fechaInicio')[0].childNodes[0].nodeValue
            estado=instancia.getElementsByTagName('estado')[0].childNodes[0].nodeValue
            final=instancia.getElementsByTagName('fechaFinal')[0].childNodes[0].nodeValue
            temporalConfig=Instancias(idinstancia,idconfi,nombre,inicio,estado,final)
    return jsonify({'ok':True,'data':'Canciones cargadas con exito'}),200'''


#Obtener Canciones
@app.route('/canciones',methods=['GET'])
def get_canciones():
    c=gestor.obtener_canciones()
    return jsonify(c),200

#Iniciar el servidor
if __name__ == "__main__":
    app.run(port=5000,debug=True)    
