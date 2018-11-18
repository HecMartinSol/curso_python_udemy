# coding=utf-8

# uso de diccionarios
def cargar():
	diccionario = {}
	continuar = "s"
	while continuar == "s":
		esp = str(raw_input("Español: "))
		eng = str(raw_input("Ingles: "))
		diccionario[esp] = eng
		continuar = str(raw_input("¿continuar? [s/n]: "))
	return diccionario
pass

def imprimir(diccionario):
	print("Diccionario:")
	for esp in diccionario:
		print(esp + " - " + diccionario[esp])	
	pass
pass


diccionario = cargar()
imprimir(diccionario)