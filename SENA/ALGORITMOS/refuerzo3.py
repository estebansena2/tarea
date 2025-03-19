productos = {}

def crearProducto():
    idProducto = input("Ingrese el ID del producto: ")
    if idProducto in productos:
        print(f"El producto con ID {idProducto} ya existe.")
    else:
        nombre = input("Ingrese el nombre del producto: ").capitalize()
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        productos[idProducto] = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        print(f"Producto {nombre} creado exitosamente con ID {idProducto}.")

def leerProductos():
    if productos:
        for idProducto, detalles in productos.items():
            print(f"ID: {idProducto}, Producto: {detalles['nombre']}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")
    else:
        print("No hay productos en el inventario.")

def actualizarProducto():
    idProducto = input("Ingrese el ID del producto a actualizar: ")
    if idProducto in productos:
        nombre = input("Ingrese el nuevo nombre del producto (dejar en blanco para no cambiar): ").capitalize()
        precio = input("Ingrese el nuevo precio del producto (dejar en blanco para no cambiar): ")
        cantidad = input("Ingrese la nueva cantidad del producto (dejar en blanco para no cambiar): ")
        if nombre:
            productos[idProducto]['nombre'] = nombre
        if precio:
            productos[idProducto]['precio'] = float(precio)
        if cantidad:
            productos[idProducto]['cantidad'] = int(cantidad)
        print(f"Producto con ID {idProducto} actualizado exitosamente.")
    else:
        print(f"El producto con ID {idProducto} no existe.")

def eliminarProductoPorId():
    idProducto = input("Ingrese el ID del producto a eliminar: ")
    if idProducto in productos:
        del productos[idProducto]
        print(f"Producto con ID {idProducto} eliminado exitosamente.")
    else:
        print(f"El producto con ID {idProducto} no existe.")

def ordenarProductos():
    productosOrdenados = dict(sorted(productos.items(), key=lambda x: x[1]['nombre']))
    print("Productos ordenados alfabéticamente:")
    for idProducto, detalles in productosOrdenados.items():
        print(f"ID: {idProducto}, Producto: {detalles['nombre']}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")

def invertirOrdenProductos():
    productosInvertidos = dict(reversed(list(productos.items())))
    print("Orden de productos invertido:")
    for idProducto, detalles in productosInvertidos.items():
        print(f"ID: {idProducto}, Producto: {detalles['nombre']}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")

def eliminarTodosLosProductos():
    productos.clear()
    print("Todos los productos han sido eliminados.")

def mostrarMenu():
    print("\n--- Menú CRUD ---")
    print("1. Crear producto")
    print("2. Leer productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto por ID")
    print("5. Listar productos")
    print("6. Ordenar productos por nombre")
    print("7. Invertir orden de productos")
    print("8. Eliminar todos los productos")
    print("9. Salir del programa")

if __name__ == "__main__":
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crearProducto()
        elif opcion == '2':
            leerProductos()
        elif opcion == '3':
            actualizarProducto()
        elif opcion == '4':
            eliminarProductoPorId()
        elif opcion == '5':
            leerProductos()
        elif opcion == '6':
            ordenarProductos()
        elif opcion == '7':
            invertirOrdenProductos()
        elif opcion == '8':
            eliminarTodosLosProductos()
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
