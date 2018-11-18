# coding=utf-8

cantidad = x = 0
n = int(raw_input("Piezas a cargar: "))
while x < n:
	largo = float(raw_input("Medida de la pieza en cm:"))
	if largo >= 1.2 and largo <= 1.3:
		cantidad += 1
	pass
	x +=1
pass

print("Piezas válidas: " + str(cantidad))
