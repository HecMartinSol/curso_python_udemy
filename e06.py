# coding=utf-8
nota1=int(raw_input("Introduce la primera nota: "))
nota2=int(raw_input("Introduce la segunda nota: "))
nota3=int(raw_input("Introduce la tercera nota: "))
prom=(nota1+nota2+nota3)/3

print("\tMedia de " + str(prom))

if prom >= 7:
	print("Promocionado")
else:
	if prom >= 4:
		print("Regular")
	else:
		print("Reprobado")