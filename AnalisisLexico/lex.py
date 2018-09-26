import ply.lex as lex
tokens = ['NUMBER','EQUALS','LPAREN','RPAREN']

reserved = {'SUM' : 'PLUS', 'RES':'MINUS', 'MUL':'TIMES', 'DIV':'DIVIDE'}

tokens += reserved.values()


t_ignore = ' \t'
t_EQUALS = r':='
t_PLUS = r"\+"
t_TIMES = r"\*"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_MINUS = r'-'
t_DIVISION = r'/'

def t_NUMBER(token):
    r"[1-9][0-9]*"
    token.value = int(token.value)
    return token

t_ignore_WHITESPACES = r"[ \t]+"

def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)

def t_error(token):
    message = "Token desconocido:"
    message = "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)

lex.lex() # Build the lexer

lex.input("x = 3 + 4 RES 5 MUL 6 DIV 10")
while True:
    tok = lex.token()
    if not tok: break
    print (str(tok.value) + " - " + str(tok.type))
