# coding=utf-8
#	tipos de funciones

#	con params
def inicio(mensaje):
	print(mensaje)
	print("*******************")
pass

#	funcion con retorno de valores y entradas variables
def cargar_suma(v1, v2 , *v_n):
	suma = v1 + v2
	for i in range(len(v_n)):
		suma += v_n[i]
	pass

	return suma
pass

# funcion con valor predefinido
def mostrar_suma(valor, mensaje="Resultado:"):
	print(str(mensaje) + " " + str(valor))
pass

#	funcion con recepcion de lista
def mostrar_lista(listaValores):
	for x in range(len(listaValores)):
		print("\t + " + str(listaValores[x]))
	pass
pass


inicio("Suma de valores")

v1 = float(raw_input("Valor 1: "))
v2 = float(raw_input("Valor 2: "))

listaValores = [1,2,3,4,5]
mostrar_lista(listaValores)

mostrar_suma(cargar_suma(v1,v2,1,2,3,4,5), "Total: ")