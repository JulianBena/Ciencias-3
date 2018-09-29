
import ply.lex as lex
declaracionesiniciales = 'iniciar-programa','inicia-ejecucion','termina-ejecucion','finalizar-programa','define-nueva-instruccion','como','define-prototipo-instruccion']
expresiones = ['apagate','gira-izquierda','avanza','coge-zumbador','deja-zumbador','sal-de-instruccion']
sentencias = ['si','entonces','sino','mientras','hacer','repetir','veces','y','o','si-es-cero','precede','sucede']
tokens = []+declaracionesiniciales+expresiones+sentencias

t_ignore = ' \t'
t_MOVE = r'\+'
t_LEFT = r'-'
t_PICK = r'\*'
t_PUT = r'/'
t_OFF = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

lex.input("x = 3 - 4 + 5 * 65")
while True:
    tok = lex.token()
    if not tok: break
    print str(tok.value) + " - " + str(tok.type)
