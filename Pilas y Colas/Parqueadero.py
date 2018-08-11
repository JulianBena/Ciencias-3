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
            print("\nUsuario número:",(i+1),"°")
            print(self.items[i].nombre)
            print(self.items[i].codigo)
            print(self.items[i].placa)
            
def main():
    Parqueadero = Cola()
    decision="a"

    while(decision=="a"):
        tempUsuario = Usuario()
        nombre=input("\nIngrese nombre:")
        codigo=input("Ingrese código:")
        placa=input("Ingrese placa:")
        tempUsuario.asig_atrib(nombre,codigo,placa)
        Parqueadero.asignar(tempUsuario)
        print("\nEl usuario a sido asignado")
        print("a. Agregar nuevo usuario.")
        print("b. Salir.")
        decision=input("Desea realizar otra accion:")
        
    Parqueadero.consultar()

if __name__ == "__main__":main() 
