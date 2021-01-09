import ply.lex as lex
import os
import sys
import re
import codecs

PalabrasReservadas = ['PROGRAM','MAIN','ARGS','AS','STRING','CONSOLE','WRITELINE','VBCRLF','DIM','READLINE', 'MODULE','SUB','END','MOD','IMPORTS','DATETIME','NOW','READKEY','TRUE','FALSE','BOOLEAN', 'BEGIN', 'WHILE']

Tokens = PalabrasReservadas+['ID','NUMERO','SUMA','RESTA','DIVISION','PRODUCTO','MENORQUE','MAYORQUE','IGUAL','DESIGUAL','PARENTIZQ','PARENTDER','LLAVEIZQ','LLAVEDER','PUNTO','UPDATE']

#Tokens
t_SUMA = r'\+'
t_RESTA = r'\-'
t_PRODUCTO = r'\*'
t_DIVISION = r'/'
t_IGUAL = r'='
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PARENTIZQ = r'\('
t_PARENTDER = r'\)'
t_PUNTO = r'\.'
t_DESIGUAL = '~='
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_UPDATE = r':='
t_ignore = '\t '

#Operaciones
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in PalabrasReservadas:
		t.value = t.value.upper()		
		t.type = t.value
	return t

def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):	
	t.lexer.skip(1)

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\'.*'
	pass

#Salida
analizador = lex.lex()