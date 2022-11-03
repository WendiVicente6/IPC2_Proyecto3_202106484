from usuario import Usuario
from cancion import Cancion
from Clientes import Clientes
from Categorias import Categorias
from Configuraciones import Configuraciones
from Instancias import Instancias
from recurso import CantidadRecurso, Recurso
from Consumos import Consumos
import json

class Gestor:
    def __init__(self):
        self.usuarios=[]
        self.cliente=[]
        self.Recurso=[]
        self.Categorias=[]
        self.Configuracion=[]
        self.Instancia=[]
        self.usuarios.append(Usuario('Jacky','Benitez','admin','admin'))
        self.usuarios.append(Usuario('Kirby','SuperStar','kirby','kirby'))
    
    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None
    
    def agregar_cliente(self,clientes):
        self.cliente.append(clientes)
        return True
    def agregar_unaclientes(self,clave,correo,direccion,nit,nombre,usuario):
        cli=Clientes(nit,nombre,usuario,clave,direccion,correo)
        self.cliente.append(cli)
        return True
        
    def agregar_Recurso(self,clientes):
        self.Recurso.append(clientes)
        return True
    def agregar_Unre(self,abre,id,metrica,nombre,tipo,valor):
        cli=Recurso(id,nombre,abre,metrica,tipo,valor)
        self.Recurso.append(cli)
        return True
    def agregar_Categorias(self,clientes):
        self.Categorias.append(clientes)
        return True
    def agregar_Categoria(self,carga,descripcion,id,nombre):
        cli=Categorias(id,nombre,descripcion,carga)
        self.Categorias.append(cli)
        return True
    def agregar_Configuracion(self,clientes):
        self.Configuracion.append(clientes)
        return True
    def agregar_unaconfi(self,descrip,id,nom):
        cli=Configuraciones(id,nom,descrip)
        self.Configuracion.append(cli)
        return True
    def agregar_Instancia(self,clientes):
        self.Instancia.append(clientes)
        return True

    def agregar_unaInsta(self,final,estado,inicio,id,idconfi,nombre):
        cli=Instancias(id,idconfi,nombre,inicio,estado,final)
        self.Instancia.append(cli)
        return True
        
    
 
    def Buscar(self,tipo):
        json=[]
        if tipo=='Clientes':
            for i in self.cliente:
                Clientes={
                    'nit':i.nit,
                    'nombre':i.nombre,
                    'usuario':i.usuario,
                    'clave':i.clave,
                    'direccion':i.direccion,
                    'correo':i.correo
                }
                json.append(Clientes)
            return json

        elif tipo=='Recursos':
            for i in self.Recurso:
                Recurso={
                'id':i.idrecurso,
                'nombre':i.nombre,
                'abreviatura':i.abreviatura,
                'metrica':i.metrica,
                'tipo':i.tipo,
                'valor':i.valor
                }
                json.append(Recurso)
            return json

        elif tipo=='Categorias':
            for i in self.Categorias:
                Cate={
                'id':i.idcate,
                'nombre':i.nombre,
                'descripcion':i.descripcion,
                'carga':i.carga
                }
                json.append(Cate)
            return json

        elif tipo=='Configuraciones':
            for i in self.Configuracion:
                Configur={
                'id':i.idconfig,
                'nombre':i.nombre,
                'descripcion':i.descripcion
                }
                json.append(Configur)
            return json

        elif tipo=='Instancias':
            for i in self.Instancia:
                Insta={
                'id':i.idinst,
                'id_config':i.idconfig,
                'nombre':i.nombre,
                'fecha_inicio':i.inicio,
                'estado':i.estado,
                'Fecha_Final':i.final
                }
                json.append(Insta) 
            return json

        
