# coding=utf-8

#####################################
#	Listas
#####################################

lista = []
for x in range(4):
	lista.append(raw_input("Introduce valor en la lista: "))
pass
print(lista)
print("#################################################################################")
i = int(raw_input("Introduce el indice a modificar: "))
i -= 1
if i < 0 or i >= len(lista):
	print("\t La posicion no existe")
else:
	nuevo_valor = raw_input("Introduce el nuevo valor para ("+str(lista[i])+"): ")
	lista[i] = nuevo_valor
	print(lista)
pass
print("#################################################################################")
valor_agregar = raw_input("Introduce un nuevo elemento al final: ")
lista.insert(len(lista), valor_agregar)
print(lista)
print("#################################################################################")
valor_eliminar = raw_input("Introduce elemento a eliminar: ")
if not(valor_eliminar in lista):
	print("\t El valor '"+str(valor_eliminar)+"' no está en la lista")
else:
	i_eliminar = lista.index(valor_eliminar) + 1

	lista.remove(valor_eliminar)
	print(str(valor_eliminar) + " eliminado de la lista (posicion "+str(i_eliminar)+")")
	print(lista)
pass
print("#################################################################################")

