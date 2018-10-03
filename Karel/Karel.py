import ply.lex as lex


tokens = [ 'iniciar-programa','define-nueva-instruccion','repetir','como','veces','si', 'entonces' , 'avanza' , 'hacer'
, 'fin' , 'gira-izquierda' , 'apagate', 'termina-ejecucion', 'finalizar-programa', 'inicio', 'mientras'
, 'frente-libre', 'no-junto-a-zumbador']
reserved = {
    'iniciar-programa' : 'PARA',
    'define-nueva-instruccion' : 'SI',
    'repetir' : 'LUEGO',
    'como' : 'ESCRIBIR',
    'veces' : 'ESCRIBIR',
    'si' : 'ESCRIBIR',
    'entonces' : 'ESCRIBIR',
    'avanza' : 'ESCRIBIR',
    'hacer' : 'ESCRIBIR',
    'fin' : 'ESCRIBIR',
    'gira-izquierda' : 'ESCRIBIR',
    'apagate' : 'ESCRIBIR',
    'termina-ejecucion' : 'ESCRIBIR',
    'finalizar-programa' : 'ESCRIBIR',
    'inicio' : 'ESCRIBIR',
    'mientras' : 'ESCRIBIR',
    'frente-libre' : 'ESCRIBIR',
    'no-junto-a-zumbador' : 'ESCRIBIR'
}
