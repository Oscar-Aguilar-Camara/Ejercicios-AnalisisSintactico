#Importar librerias
import ply.yacc as yacc
import re
import os
import codecs
from analizador import tokens
from sys import stdin

precedence = (	
	('left','DESIGUAL'),
	('left','MENORQUE','MAYORQUE'),
	('left','SUMA','RESTA'),
	('left','PRODUCTO','DIVISION'),
	('left','PARENTIZQ','PARENTDER'),
	('left','LLAVEIZQ','LLAVEDER'),
	('right','ID','MODULE', 'IMPORTS'),
	('right','IGUAL'),
	('right','UPDATE'),
	('right','NUMERO'),
	('right','WHILE'),
	('right','PUNTO'),
	)

def p_condition1(p):
	'condition : expression'
	print ("condition 1")

def p_condition2(p):
	'condition : expression relation expression'
	print ("condition 2")

def p_relation1(p):
	'relation : IGUAL'
	print ("relation 1")

def p_relation2(p):
	'relation : DESIGUAL'
	print ("relation 2")

def p_relation3(p):
	'relation : MENORQUE'
	print ("relation 3")

def p_relation4(p):
	'relation : MAYORQUE'
	print ("relation 4")

def p_relation5(p):
	'relation : TRUE'
	print ("relation 5")

def p_relation6(p):
	'relation : FALSE'
	print ("relation 6")

def p_expression1(p):
	'expression : term'
	print ("expresion 1")

def p_expression2(p):
	'expression : addingOperator term'
	print ("expresion 2")

def p_expression3(p):
	'expression : expression addingOperator term'
	print ("expresion 3")

def p_expression4(p):
	'expression : DATETIME PUNTO NOW'
	print ("expresion 4")

def p_expression5(p):
	'expression : LLAVEIZQ ID LLAVEDER'
	print ("expresion 5")

def p_expression6(p):
	'expression : VBCRLF'
	print ("expresion 5")

def p_expression7(p):
	'expression : MODULE PROGRAM'
	print ("expresion 7")

def p_expression8(p):
	'expression : END MODULE'
	print ("EndMod")

def p_expression9(p):
	'expression : CONSOLE PUNTO READKEY PARENTIZQ boolean PARENTDER'
	print ("expresion 8")

def p_expression10(p):
	'expression : DIM ID IGUAL CONSOLE PUNTO READLINE PARENTIZQ PARENTDER'
	print ("expresion 9")

def p_expression11(p):
	'expression : CONSOLE PUNTO WRITELINE PARENTIZQ ID PARENTDER'
	print ("expresion 10")

def p_addingOperator1(p):
	'addingOperator : SUMA'
	print ("addingOperator 1 ")

def p_addingOperator2(p):
	'addingOperator : RESTA'
	print ("addingOperator 2")

def p_addingOperator3(p):
	'addingOperator : MOD'
	print ("addingOperator 3")

def p_term1(p):
	'term : factor'
	print ("term 1")

def p_term2(p):
	'term : term multiplyingOperator factor'
	print ("term 2")

def p_multiplyingOperator1(p):
	'multiplyingOperator : PRODUCTO'
	print ("multiplyingOperator 1")

def p_multiplyingOperator2(p):
	'multiplyingOperator : DIVISION'
	print ("multiplyingOperator 2")

def p_module(p):
	'module : program'	
	print ("Module")
	
def p_factor1(p):
	'factor : ID'
	print ("factor 1")

def p_factor2(p):
	'factor : NUMERO'
	print ("factor 2")

def p_factor3(p):
	'factor : PARENTIZQ expression PARENTDER'
	print ("factor 3")

def p_boolean(p):
	'boolean : BOOLEAN'

def p_empty(p):
	'empty :'
	pass

def p_error(p):
	print ("Error de sintaxis ", p)

def buscarFicheros(direct):
	fichero = []
	Numfile = ''
	resp = False
	cont = 1

	for base, dirs, files in os.walk(direct):
		fichero.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while resp == False:
		Numfile = input('\nTest: ')
		for file in files:
			if file == files[int(Numfile)-1]:
				resp = True
				break
	print ("Ha elegido: \"%s\" \n" %files[int(Numfile)-1])
	return files[int(Numfile)-1]

direccion = "C:\Users\azulo\Desktop\EJERCICIOS ANALISIS SINTACTICO"

myFile = buscarFicheros(direccion)
prueba = direccion+myFile
fp = codecs.open(prueba, "r", "utf-8")
cadena = fp.read()
fp.close()
parser = yacc.yacc()
result = parser.parse(cadena)
print (result)