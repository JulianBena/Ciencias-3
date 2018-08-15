# -*- coding: utf-8 -*-

class Libro:
    def __init__(self):
        self.titulo=""
        self.autor=""
        self.genero=""

    def asig_atrib(self,titulo,autor,genero):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero

class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def asignar(self, Libro):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(Libro)

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

    def buscar(self, x):
        if(self.es_vacia==True):
            print("No se tiene registro del libro solicitado.")
        else:
            for i in range(0,len(self.items)):
                if(self.items[i].titulo==x or self.items[i].autor==x or self.items[i].genero==x):
                    print("\nInformacion del libro encontrado:")
                    print(self.items[i].titulo)
                    print(self.items[i].autor)
                    print(self.items[i].genero)
                else:
                    print("No se tiene registro del libro solicitado.")
                    
def main():
    Biblioteca = Cola()
    a=0
    salir = False
    while not salir:
        while(a!='1' and a!='2'):
            print(" ** MENU ** ")
            print("Seleccione una opcion.")
            print("1. Agregar nuevo libro.")
            print("2. Buscar un libro.")
            print("3. Salir")
            a=input()

        if a=='1':
            nuvLibro = Libro()
            titulo=input("\nIngrese Titulo del libro:")
            autor=input("Ingrese Autor:")
            genero=input("Ingrese Genero:")
            nuvLibro.asig_atrib(titulo,autor,genero)
            Biblioteca.asignar(nuvLibro)
            print("\nEl libro ha sido asignado")
            a=0
        else:
            x=input("Ingrese elemento a buscar: ")    
            Biblioteca.buscar(x)
            
        
if __name__ == "__main__":main()

