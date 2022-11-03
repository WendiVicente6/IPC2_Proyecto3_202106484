from usuario import Usuario
from cancion import Cancion
from Clientes import Clientes
import json

class Gestor:
    def __init__(self):
        self.usuarios=[]
        self.cliente=[]
        self.usuarios.append(Usuario('Jacky','Benitez','admin','admin'))
        self.usuarios.append(Usuario('Kirby','SuperStar','kirby','kirby'))
    
    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None
    
    def agregar_cancion(self,nit,nombre4,usuario,clave,direccion,correo):
        self.cliente.append(Clientes(nit,nombre4,usuario,clave,direccion,correo))
        return True
    
    def obtener_canciones(self):
        json=[]
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
        
