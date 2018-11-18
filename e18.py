# coding=utf-8

# importacion de modulos totales
import random
# importacion de determinadas funciones con un nombre
from math import sqrt as raiz_cuadrada


def cargar():
    lista = []
    for x in range(10):
        lista.append(raiz_cuadrada(random.randint(0, 20)))
    pass
    return lista


pass


lista = cargar()
print(lista)
random.shuffle(lista)
print(lista)
