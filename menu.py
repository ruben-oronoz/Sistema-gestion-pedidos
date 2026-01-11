from inventario import (
    agregar_producto,
    mostrar_productos,
    buscar_productos,
    eliminar_producto,
    resumen_inventario
)

def menu():
    while True:
        print("==== MENU INVENTARIO ====")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Eliminar producto")
        print("5. Resumen del inventario")
        print("6. Salir")

        opcion = input("Elegir opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_productos()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            resumen_inventario()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

def main():
    menu()

main()
