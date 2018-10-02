import lex

PROGRAMA_FILE = "programa.in"
ANALISIS_FILE = "analisis.out"

def escribir(analisis):
    archivo = open(PROGRAMA_FILE, "a")
    archivo.write(str(analisis)+'\n')
    file.close()


def leer():
    archivo = open(PROGRAMA_FILE, "r")
    filas = (archivo.read().splitlines())
    clearFile(ANALISIS_FILE)
    for exp in filas:
        result = lexer.tokens(programa)
        writeFile(result)
        lexer.lista = []
        print(programa)

    file.close()

if __name__ == "__main__":
    leer()
