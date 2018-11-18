# coding=utf-8

suma = x = 0
veces = 10
while x < veces:
	valor = int(raw_input("Valor: "))
	suma += valor
	x +=1
pass
promedio = float(suma) / float(veces)

print("La suma de los " + str(veces) + " valores es " + str(suma))
print("El promedio es " + str(promedio))