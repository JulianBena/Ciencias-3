
import ply.lex as lex
declaracionesiniciales = 'iniciar-programa','inicia-ejecucion','termina-ejecucion','finalizar-programa','define-nueva-instruccion','como','define-prototipo-instruccion']
expresiones = ['apagate','gira-izquierda','avanza','coge-zumbador','deja-zumbador','sal-de-instruccion']
sentencias = ['si','entonces','sino','mientras','hacer','repetir','veces','y','o','si-es-cero','precede','sucede']
booleanos=['frente-libre', 'junto-a-zumbador', 'orientado-al-norte','frente-bloqueado','no-junto-a-zumbador','orientado-al-sur','izquierda-libre','algun-zumbador-en-la mochila','orientado-al-este','izquierda-bloqueada','ningun-zumbador-en-la mochila','orientado-al-oeste',
'derecha-libre','no-orientado-al-norte','derecha-bloqueada','no-orientado-al-sur','no-orientado-al-este','no-orientado-al-oeste']
tokens = []+declaracionesiniciales+expresiones+sentencias+booleanos
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

def tokens(programa):
    lex.input(programa)
    while True:
        tok = lex.token()
        if not tok: break
        lista.append(str(tok.value) + " -> " + str(tok.type))
    return lista
    
