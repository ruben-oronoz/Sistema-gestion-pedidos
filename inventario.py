productos = []

def agregar_producto():
    nombre = input("Nombre: ").title()
    if nombre == "":
        print("No puedes dejar el nombre vacío")
        return

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        if precio < 0:
            print("ERROR: El precio no puede ser negativo")
        elif stock <= 0:
            print("ERROR: El stock debe ser mayor a cero")
        else:
            productos.append({
                "nombre": nombre,
                "precio": precio,
                "stock": stock
            })
            print("Producto registrado")
    except ValueError:
        print("ERROR: Solo debes introducir valores numéricos")

def mostrar_productos():
    if not productos:
        print("No hay registro de productos")
        return

    for p in productos:
        print(f"Nombre: {p['nombre']} | Precio: {p['precio']} | Stock: {p['stock']}")

def buscar_productos():
    if not productos:
        print("No hay registro de productos")
        return

    buscado = input("Producto a buscar: ").title()
    encontrado = False

    for p in productos:
        if p["nombre"] == buscado:
            print(f"Nombre: {p['nombre']} | Precio: {p['precio']} | Stock: {p['stock']}")
            encontrado = True

    if not encontrado:
        print("No hay registros con ese nombre")

def eliminar_producto():
    if not productos:
        print("No hay registro de productos")
        return

    eliminado = input("Producto a eliminar: ").title()

    for p in productos[:]:
        if p["nombre"] == eliminado:
            permiso = input("Seguro que desea eliminarlo? (s/n): ")
            if permiso == "s":
                productos.remove(p)
                print("Producto eliminado")
                return
            elif permiso == "n":
                print("Eliminación cancelada")
                return

    print("No hay registros con ese nombre")

def resumen_inventario():
    if not productos:
        print("No hay registro de productos")
        return

    total_productos = len(productos)
    total_inventario = 0

    for p in productos:
        total_inventario += p["precio"] * p["stock"]

    print(f"Total de productos: {total_productos}")
    print(f"Valor total del inventario: {total_inventario}$")
