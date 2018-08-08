# -*- coding: utf-8 -*-
class Usuario():
    def __init__(self):
        self.placa=""
        self.codigo=0
        self.nombre=" "

    def asig_atrib(self,nombre,codigo,placa):
        self.placa=placa
        self.codigo=codigo
        self.nombre=nombre

class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]
        self.Usuario=[]

    def asignar(self, Usuario ):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(Usuario)
    
    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
    
    def consultar(self):
        for i in range(0,len(self.items)):
            print("Usuario número:"(i+1))
            print(self.items[i].nombre)
            print(self.items[i].codigo)
            print(self.items[i].placa)
            print("")
            
    def agregar(us1):
        self.Usuario=us1
        
        
    
parqueadero=Cola()
x=input("Si desea asignar un usuario del parqueadero, ingrese cualquier tecla excepto 1")
while (x!=1):
    us1=Usuario()
    nombre=input("Ingrese nombre:")
    codigo=input("Ingrese código:")
    placa=input("Ingrese placa:")
    us1.asig_atrib(nombre,codigo,placa)
    parqueadero.asignar(us1)
    x=input("Si no desea asignar otro usuario del parqueadero, ingrese la tecla 1")

parqueadero.consultar()

