
from xml.dom import minidom
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS
from Categorias import Categorias
from Clientes import Clientes
from Configuraciones import Configuraciones
from Instancias import Instancias
from Funciones import XML
from recurso import CantidadRecurso, Recurso
from Consumos import Consumos

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
@app.route('/agregarCategorias',methods=['POST'])
def agregarCategoria():
    json=request.get_json()
    gestor.agregar_Categoria(json['carga'],json['descripcion'],json['id'],json['nombre'])
    return jsonify({'ok':True, 'data':'Categoria añadida con exito'}),200

@app.route('/agregarRecursos',methods=['POST'])
def agregarRecurso():
    json=request.get_json()
    gestor.agregar_Unre(json['abreviatura'],json['id'],json['metrica'],json['nombre'],json['tipo'],json['valor'])
    return jsonify({'ok':True, 'data':'Recurso añadida con exito'}),200

@app.route('/contenido',methods = ['POST'])
def parseInfo():
    contarcliente=0
    contarrecursos=0
    contarrecate=0
    contarreconfi=0
    contarinsta=0
    body = request.get_json()
    ruta = body['ruta']
    #content = read.entrada(ruta)
    file = 'C:/Users/wendi/Documents/CUARTO SEMESTRE/IPC2/Laboratorio/IPC2_Proyecto3_202106484/Proyecto 3/' + ruta
    tree = minidom.parse(file)
    listare= tree.getElementsByTagName('listaRecursos')
    listacatego= tree.getElementsByTagName('listaCategorias')
    listaclilentes= tree.getElementsByTagName('listaClientes')
    for lisre in listare:
        archivoconfig= lisre.getElementsByTagName('recurso')

        for configInicial in archivoconfig:
            idrecurso=configInicial.getAttribute('id')
            contarrecursos+=1
            nombre1=configInicial.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
            
            abreviatura=configInicial.getElementsByTagName('abreviatura')[0].childNodes[0].nodeValue
            metrica=configInicial.getElementsByTagName('metrica')[0].childNodes[0].nodeValue
            tipo=configInicial.getElementsByTagName('tipo')[0].childNodes[0].nodeValue
            valor=configInicial.getElementsByTagName('valorXhora')[0].childNodes[0].nodeValue
            temporalConfig=Recurso(idrecurso,nombre1,abreviatura,metrica,tipo,valor)
            gestor.agregar_Recurso(temporalConfig)
            
            
    for lisca in listacatego:
        catego= lisca.getElementsByTagName('categoria')
        for categoria in catego:
            idcategoria=categoria.getAttribute('id')
            contarrecate+=1
            nombre2=categoria.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
            descripcion=categoria.getElementsByTagName('descripcion')[0].childNodes[0].nodeValue
            carga=categoria.getElementsByTagName('cargaTrabajo')[0].childNodes[0].nodeValue
            categoriasGu=Categorias(idcategoria,nombre2,descripcion,carga)
            gestor.agregar_Categorias(categoriasGu)
            listaconfiguraciones=categoria.getElementsByTagName('configuracion')        
        
            for configuracion in listaconfiguraciones:
                idconfi=configuracion.getAttribute('id')
                contarreconfi+=1
                nombre3=configuracion.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
                descripcion=configuracion.getElementsByTagName('descripcion')[0].childNodes[0].nodeValue
                configu=Configuraciones(idconfi,nombre3,descripcion)
                gestor.agregar_Configuracion(configu)
                recursosconfigurados=configuracion.getElementsByTagName('recursosConfiguracion') 
            
                for recursos in recursosconfigurados:
                    idrecursoconfi=recursos.getAttribute('id')
                    cantidad=recursos.getElementsByTagName('recurso')[0].childNodes[0].nodeValue

                    temporalConfig=CantidadRecurso(idrecursoconfi,cantidad)

    for liscli in listaclilentes:
        listaclientes=liscli.getElementsByTagName('cliente')
        

        for clientes in listaclientes:
            nit=clientes.getAttribute('nit')
            contarcliente+=1
            nombre4=clientes.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
            usuario=clientes.getElementsByTagName('usuario')[0].childNodes[0].nodeValue
            clave=clientes.getElementsByTagName('clave')[0].childNodes[0].nodeValue
            direccion=clientes.getElementsByTagName('direccion')[0].childNodes[0].nodeValue
            correo=clientes.getElementsByTagName('correoElectronico')[0].childNodes[0].nodeValue

            clientesGu=Clientes(nit,nombre4,usuario,clave,direccion,correo)
            gestor.agregar_cliente(clientesGu)
            listainstancia=clientes.getElementsByTagName('instancia') 

            for instancia in listainstancia:
                idinstancia=instancia.getAttribute('id')
                contarinsta+=1
                idconfi=instancia.getElementsByTagName('idConfiguracion')[0].childNodes[0].nodeValue
                nombre5=instancia.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
                inicio=instancia.getElementsByTagName('fechaInicio')[0].childNodes[0].nodeValue
                estado=instancia.getElementsByTagName('estado')[0].childNodes[0].nodeValue
                final=instancia.getElementsByTagName('fechaFinal')[0].childNodes[0].nodeValue
                instagu=Instancias(idinstancia,idconfi,nombre5,inicio,estado,final)
                gestor.agregar_Instancia(instagu)
                
    
    return jsonify({'data': 'Archivo de Configuración cargado','clientes':contarcliente,'Instancias':contarinsta,"Configuraciones":contarreconfi,"Categorias":contarrecate,"Recursos":contarrecursos})

@app.route('/consumos',methods = ['POST'])
def parseInfo2():
    contarconsumo=0
    body = request.get_json()
    ruta = body['ruta']
    #content = read.entrada(ruta)
    file = 'C:/Users/wendi/Documents/CUARTO SEMESTRE/IPC2/Laboratorio/IPC2_Proyecto3_202106484/Proyecto 3/' + ruta
    tree = minidom.parse(file)
    listare= tree.getElementsByTagName('listadoConsumos')
    
    for lisre in listare:
        archivoconfig= lisre.getElementsByTagName('consumo')

        for configInicial in archivoconfig:
            nit=configInicial.getAttribute('nitCliente')
            contarconsumo+=1
            idinstancia=configInicial.getAttribute('idInstancia')
            tiempo=configInicial.getElementsByTagName('tiempo')[0].childNodes[0].nodeValue
            print(tiempo)
            fecha=configInicial.getElementsByTagName('fechaHora')[0].childNodes[0].nodeValue
            temporalConfig=Consumos(nit,idinstancia,tiempo,fecha)
        

    return jsonify({'data': 'Archivo de Consumos cargado',"Total Consumos":contarconsumo})

#Obtener Canciones
@app.route('/Consultar',methods=['POST'])
def registar():

    dato=gestor.Buscar(request.json['Tipo'])
    return jsonify(dato)

#Iniciar el servidor
if __name__ == "__main__":
    app.run(port=5000,debug=True)    
