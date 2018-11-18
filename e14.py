# coding=utf-8
def cargar_pais_poblacion(n=10):
	paises = []
	for i in range(0, n):
		nombre = str(raw_input("Nombre: "))
		poblacion = int(raw_input("Poblacion: "))
		paises.append((nombre,poblacion))
	pass

	return paises
pass

def imprimir(paises = []):
	for i in range(0, len(paises)):
		pais = paises[i]
		print(str(pais[0]) + ": " + str(pais[1]) + " habitantes")
	pass
pass

def mostrar_mayor_poblacion(paises = []):
	i_mayor = 0
	for i in range(0, len(paises)):
		if paises[i][1] > paises[i_mayor][1]:
			i_mayor = 1
		pass
	pass

	print("El que mas tiene es " + str(paises[i_mayor][0]) + " con " + str(paises[i_mayor][1]) + " habitantes")
pass

paises = cargar_pais_poblacion(3)
imprimir(paises)
mostrar_mayor_poblacion(paises)