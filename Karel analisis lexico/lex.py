import ply.lex as lex

declaracionesiniciales = ['iniciar-programa','inicia-ejecucion','termina-ejecucion','finalizar-programa','define-nueva-instruccion','como','define-prototipo-instruccion']

expresiones = ['apagate','gira-izquierda','avanza','coge-zumbador','deja-zumbador','sal-de-instruccion']

sentencias = ['si','entonces','sino','mientras','hacer','repetir','veces','y','o','si-es-cero','precede','sucede']

booleanos=['frente-libre', 'junto-a-zumbador', 'orientado-al-norte','frente-bloqueado','no-junto-a-zumbador','orientado-al-sur','izquierda-libre','algun-zumbador-en-la mochila',
           'orientado-al-este','izquierda-bloqueada','ningun-zumbador-en-la mochila','orientado-al-oeste','derecha-libre','no-orientado-al-norte','derecha-bloqueada',
           'no-orientado-al-sur','no-orientado-al-este','no-orientado-al-oeste']

tokens = declaracionesiniciales + expresiones + sentencias + booleanos

#Declaraciones iniciales
t_iniciar-programa = r'iniciar-programa'
t_inicia-ejecucion = r'inicia-ejecucion'
t_termina-ejecucion = r'termina-ejecucion'
t_finalizar-programa = r'finalizar-programa'
t_define-nueva-instruccion = r'define-nueva-instruccion'
t_como = r'como'
t_define-prototipo-instruccion = r'define-prototipo-instruccion'
#Expresiones
t_apagate = r'apagate'
t_gira-izquierda = r'gira-izquierda'
t_avanza = r'avanza'
t_coge-zumbador = r'coge-zumbador'
t_deja-zumbador = r'sal-de-instruccion'
#Sentencias
t_si = r'si'
t_entonces = r'entonces'
t_sino = r'sino'
t_mientras = r'mientras'
t_hacer = r'hacer'
t_repetir = r'repetir'
t_veces = r'veces'
t_y = r'y'
t_o = r'o'
t_si-es-cero = r'si-es-cero'
t_precede = r'precede'
t_sucede = r'sucede'
#Booleanos
t_frente-libre = r'frente-libre'
t_junto-a-zumbador = r'junto-a-zumbador'
t_orientado-al-norte = r'orientado-al-norte'
t_frente-bloqueado = r'frente-bloqueado'
t_no-junto-a-zumbador = r'no-junto-a-zumbador'
t_orientado-al-sur = r'orientado-al-sur'
t_izquierda-libre = r'izquierda-libre'
t_algun-zumbador-en-la-mochila = r'algun-zumbador-en-la-mochila'
t_orientado-al-este = r'orientado-al-este'
t_izquierda-bloqueada = r'izquierda-bloqueada'
t_ningun-zumbador-en-la-mochila = r'ningun-zumbador-en-la-mochila'
t_orientado-al-oeste = r'orientado-al-oeste'
t_derecha-libre = r'derecha-libre'
t_no-orientado-al-norte = r'no-orientado-al-norte'
t_derecha-bloqueada = r'derecha-bloqueada'
t_no-orientado-al-sur = r'no-orientado-al-sur'
t_no-orientado-al-este = r'no-orientado-al-este'
t_no-orientado-al-oeste = r'no-orientado-al-oeste'


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



# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer



def tokens(programa):
    lex.input(programa)
    while True:
        tok = lex.token()
        if not tok: break
        lista.append(str(tok.value) + " -> " + str(tok.type))
    return lista
