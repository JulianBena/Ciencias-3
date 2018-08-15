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
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)



pila = Pila()
respuestas = []

archivo = open("expresionesin.txt", "r")
lista = archivo.readlines()
for contenido in lista:
    contenido = contenido.strip("\n")
    print(contenido.split(" "))
    convertir(contenido.split(" "), pila)
    b = evaluar(pila.desapilar())
    respuestas.append(str(b))

f=open("expresionesout.txt","w")
for i in range(0,len(respuestas)-1):
    f.write(respuestas[i]+"\n")
    
f.close()
print (respuestas)



