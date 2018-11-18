# coding=utf-8


def carga_productos():
    productos = {}
    continuar = "s"
    while continuar == "s":
        codigo = str(raw_input("Código: "))
        nombre = str(raw_input("Nombre: "))
        precio = float(raw_input("Precio: "))
        stock = int(raw_input("Stock: "))
        productos[codigo] = (nombre, precio, stock)

        continuar = str(raw_input("¿Continuar? [s/n]: "))
    pass
    print("************************")

    return productos


pass


def mostrar_productos(productos, solo_con_stock=False):
    for codigo in productos:
        prod = productos[codigo]
        if solo_con_stock and prod[2] == 0:
            print("Codigo: " + str(codigo) + " agotado")
        else:
            print("Codigo: " + str(codigo))
            print("Nombre: " + str(prod[0]))
            print("Precio: " + str(prod[1]))
            print("Stock: " + str(prod[2]))
        pass
        
        print("************************")
    pass


pass


productos = carga_productos()
mostrar_productos(productos, True)
