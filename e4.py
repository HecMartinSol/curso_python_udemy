# coding=utf-8
sueldo=int(raw_input("Introduce tu sueldo: "))

if sueldo > 3000:
	print("El usuario tiene que pagar impuestos")
else:
	print("El usuario NO tiene que pagar impuestos")

if sueldo > 6000 and sueldo < 10000:
	print("El usuario tiene que pagar 1000€")
pass

if sueldo == 20000 or sueldo == 30000:
	print("El usuario tiene que pagar el 10\% del sueldo")
pass

