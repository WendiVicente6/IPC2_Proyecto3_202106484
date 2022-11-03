from usuario import Usuario
from cancion import Cancion
import json

class Gestor:
    def __init__(self):
        self.usuarios=[]
        self.canciones=[]
        self.recurso=[]
        self.usuarios.append(Usuario('Jacky','Benitez','admin','admin'))
        self.usuarios.append(Usuario('Kirby','SuperStar','kirby','kirby'))
    
    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_usuario(self,user,password):
        for x in self.usuarios:
            if x.user==user and x.password==password:
                return x
        return None
    
    def agregar_cancion(self,recurso):
        self.recurso.append(recurso)
        return True
    
    def obtener_canciones(self):
        json=[]
        for i in self.recurso:
            cancion={
                'name':i.idrecurso,
                'artist':i.nombre,
                'image':i.abreviatura,
                'album':i.metrica
            }
            json.append(cancion)
        return json
        
