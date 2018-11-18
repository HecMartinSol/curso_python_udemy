# coding=utf-8

"""
En una lista si se accede con valores negativos
empieza a contar desde el ultimo
Es decir, acceder a
    lista[-1] es acceder al ultimo valor
    lista[-2] es acceder al penúltimo valor
"""
def rango_de_meses(ini=0, fin=12):
    meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    return meses[ini:fin]


pass


rango = rango_de_meses(int(raw_input("Mes inicio: ")) - 1, int(raw_input("Mes fin: ")))
print(rango)
