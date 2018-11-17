# coding=utf-8
nota1=int(raw_input("Introduce la primera nota: "))
nota2=int(raw_input("Introduce la segunda nota: "))
nota3=int(raw_input("Introduce la tercera nota: "))
media=(nota1+nota2+nota3)/3

print("\tMedia de " + str(media))

if media == 9 or media == 10:
	print("Promocionado")
elif media == 8 or media == 7:
	print("Notable")
elif media == 6:
	print("Bien")
elif media == 5:
	print("Suficiente")
else:
	print("Suspenso")
