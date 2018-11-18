# coding=utf-8

def presentacion():
	print("Calculadora:")
	print("**********************")
pass

def introducirDatos():
	global v1
	global v2
	v1 = float(raw_input("Valor 1: "))
	v2 = float(raw_input("Valor 2: "))
pass

def suma():
	global suma
	suma = v1 + v2
pass

def resta():
	global resta
	resta = v1 - v2
pass

def multiplicacion():
	global multiplicacion
	multiplicacion = v1 * v2
pass

def division():
	global division
	division = v1 / v2
pass

def mostrarDatos():
	print("**********************")
	print("Operaciones:")
	print("\t"+ str(v1) + " + " + str(v2) + " = " + str(suma))
	print("\t"+ str(v1) + " - " + str(v2) + " = " + str(resta))
	print("\t"+ str(v1) + " * " + str(v2) + " = " + str(multiplicacion))
	print("\t"+ str(v1) + " / " + str(v2) + " = " + str(division))
pass

# Llamamos
presentacion()
introducirDatos()
suma()
resta()
multiplicacion()
division()
mostrarDatos()