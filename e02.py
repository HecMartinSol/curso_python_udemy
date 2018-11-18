# coding=utf-8

print("Datos de la primera persona")

#	Entrada de usuario
nombre1=str(raw_input("Introduce nombre de producto #1: "))
precio1=int(raw_input("Introduce precio #1: "))

nombre2=str(raw_input("Introduce nombre de producto #2: "))
precio2=int(raw_input("Introduce precio #2: "))

#	Constante va con mayus
BONIFICACION = 20

""" 
Hacemos varias operaciones aritméticas y lógicas a continuacion
""" 
precio_compra_total = precio1 + precio2
comparar = precio1 >= precio2
logico = (precio1 < precio2 and precio1 == precio2)


"""
Concatenamos texto de dos maneras
"""
cabecera = "resultados del producto {0}. y del producto {1}. :"
print(cabecera.format(nombre1, nombre2)) #
print("el precio del 1º es >= al precio del 2º")
print(comparar)

print("La suma de los dos productos es: " + str(precio_compra_total))
print("precio1 < precio2 and precio1 == precio2 ")
print(logico)

precio_compra_total += BONIFICACION
print("precio total con BONIFICACION = " + str(precio_compra_total))