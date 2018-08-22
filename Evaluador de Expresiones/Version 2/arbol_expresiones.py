from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)

class diccionario():
    def __init__(self, lista=None):
        self.lista=[]
    def agregar(string,int):
        self.lista.append((string,int))

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor == "=":
        return evaluar(arbol.izq)
    return int(arbol.valor)


dicc = diccionario()
pila = Pila()
respuestas = []

archivo = open("expresionesin.txt", "r")
lista = archivo.readlines()
for contenido in lista:
    contenido = contenido.strip("\n")
    print(contenido.split(" "))
    convertir(contenido.split(" "), pila)
    dicc.agregar(a,evaluar(pila.desapilar()))
    respuestas.append(str(dicc[0][0]),str(dicc[0][1]))
"""
f=open("expresionesout.txt","w")
for i in range(0,len(respuestas)-1):
    f.write(respuestas[i]+"\n")
    
f.close()
print (respuestas)
"""


