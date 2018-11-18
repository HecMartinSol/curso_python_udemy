# coding=utf-8


def rango_de_meses(ini=0, fin=12):
    meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    return meses[ini:fin]


pass


rango = rango_de_meses(int(raw_input("Mes inicio: ")) - 1, int(raw_input("Mes fin: ")))
print(rango)
