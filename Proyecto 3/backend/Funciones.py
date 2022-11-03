from xml.dom import minidom
from flask import Flask, request
from flask.json import jsonify
from Categorias import Categorias
from Clientes import Clientes
from Configuraciones import Configuraciones
from Instancias import Instancias
from recurso import CantidadRecurso, Recurso
from tkinter import N

from gestor import Gestor
gestor=Gestor()


class XML():
    '''def entrada(self,ruta):
        entrada=''
        file = 'C:/Users/wendi/Documents/CUARTO SEMESTRE/IPC2/Laboratorio/Proyecto 3/' + ruta
        fi=open(file,'r', encoding="utf-8")
        for line in file:
            entrada += line
        fi.close() 
        return entrada'''
    def readXML(self,ruta):
        file = 'C:/Users/wendi/Documents/CUARTO SEMESTRE/IPC2/Laboratorio/Proyecto 3/' + ruta
        tree = minidom.parse(file)
        listare= tree.getElementsByTagName('listaRecursos')
        listacatego= tree.getElementsByTagName('listaCategorias')
        listaclilentes= tree.getElementsByTagName('listaClientes')
        for lisre in listare:
            archivoconfig= lisre.getElementsByTagName('recurso')

            for configInicial in archivoconfig:
                idrecurso=configInicial.getAttribute('id')
                nombre1=configInicial.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
                
                abreviatura=configInicial.getElementsByTagName('abreviatura')[0].childNodes[0].nodeValue
                metrica=configInicial.getElementsByTagName('metrica')[0].childNodes[0].nodeValue
                tipo=configInicial.getElementsByTagName('tipo')[0].childNodes[0].nodeValue
                valor=configInicial.getElementsByTagName('valorXhora')[0].childNodes[0].nodeValue
                temporalConfig=Recurso(idrecurso,nombre1,abreviatura,metrica,tipo,valor)
              
        for lisca in listacatego:
            catego= lisca.getElementsByTagName('categoria')
            for categoria in catego:
                idcategoria=categoria.getAttribute('id')
                nombre2=categoria.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
                print(nombre2)
                descripcion=categoria.getElementsByTagName('descripcion')[0].childNodes[0].nodeValue
                carga=categoria.getElementsByTagName('cargaTrabajo')[0].childNodes[0].nodeValue
                temporalConfig=Categorias(idcategoria,nombre2,descripcion,carga)
                listaconfiguraciones=categoria.getElementsByTagName('configuracion')        
            
                for configuracion in listaconfiguraciones:
                    idconfi=configuracion.getAttribute('id')
                    nombre3=configuracion.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
                    print(nombre3)
                    descripcion=configuracion.getElementsByTagName('descripcion')[0].childNodes[0].nodeValue
                    temporalConfig=Configuraciones(idconfi,nombre3,descripcion)
                    recursosconfigurados=configuracion.getElementsByTagName('recursosConfiguracion') 
                
                    for recursos in recursosconfigurados:
                        idrecursoconfi=recursos.getAttribute('id')
                        cantidad=recursos.getElementsByTagName('recurso')[0].childNodes[0].nodeValue
                        print(cantidad)
                        temporalConfig=CantidadRecurso(idrecursoconfi,cantidad)
        for liscli in listaclilentes:
            listaclientes=liscli.getElementsByTagName('cliente')

            for clientes in listaclientes:
                nit=clientes.getAttribute('nit')
                nombre4=clientes.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
                print(nombre4)
                usuario=clientes.getElementsByTagName('usuario')[0].childNodes[0].nodeValue
                clave=clientes.getElementsByTagName('clave')[0].childNodes[0].nodeValue
                direccion=clientes.getElementsByTagName('direccion')[0].childNodes[0].nodeValue
                correo=clientes.getElementsByTagName('correoElectronico')[0].childNodes[0].nodeValue

                temporalConfig=Clientes(nit,nombre4,usuario,clave,direccion,correo)
                listainstancia=clientes.getElementsByTagName('instancia') 

                for instancia in listainstancia:
                    idinstancia=instancia.getAttribute('id')
                    idconfi=instancia.getElementsByTagName('idConfiguracion')[0].childNodes[0].nodeValue
                    print(idconfi)
                    nombre5=instancia.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
                    inicio=instancia.getElementsByTagName('fechaInicio')[0].childNodes[0].nodeValue
                    print(inicio)
                    estado=instancia.getElementsByTagName('estado')[0].childNodes[0].nodeValue
                    final=instancia.getElementsByTagName('fechaFinal')[0].childNodes[0].nodeValue
                    temporalConfig=Instancias(idinstancia,idconfi,nombre5,inicio,estado,final)
        return temporalConfig