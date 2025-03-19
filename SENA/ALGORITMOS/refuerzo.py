productos = {}

# Listas para almacenar entradas de productos
entradaIds = []
entradaProductos = []
entradaCantidades = []
entradaFechas = []

# CRUD para productos
def crearProducto():
    idProducto = input("Ingrese el ID del producto: ")
    if idProducto in productos:
        print(f"El producto con ID {idProducto} ya existe.")
    else:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        productos[idProducto] = {'id': idProducto, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
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
        nombre = input("Ingrese el nuevo nombre del producto (dejar en blanco para no cambiar): ")
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

# CRUD para entradas de producto usando listas separadas
def crearEntrada():
    idEntrada = input("Ingrese el ID de la entrada: ")
    idProducto = input("Ingrese el ID del producto: ")
    if idProducto in productos:
        if idEntrada in entradaIds:
            print(f"La entrada con ID {idEntrada} ya existe.")
        else:
            cantidad = int(input("Ingrese la cantidad de la entrada: "))
            fecha = input("Ingrese la fecha de la entrada (YYYY-MM-DD): ")
            entradaIds.append(idEntrada)
            entradaProductos.append(idProducto)
            entradaCantidades.append(cantidad)
            entradaFechas.append(fecha)
            productos[idProducto]['cantidad'] += cantidad
            print(f"Entrada {idEntrada} creada exitosamente y stock actualizado.")
    else:
        print(f"El producto con ID {idProducto} no existe.")

def leerEntradas():
    if entradaIds:
        for i in range(len(entradaIds)):
            print(f"ID Entrada: {entradaIds[i]}, ID Producto: {entradaProductos[i]}, Cantidad: {entradaCantidades[i]}, Fecha: {entradaFechas[i]}")
    else:
        print("No hay entradas registradas.")

def actualizarEntrada():
    idEntrada = input("Ingrese el ID de la entrada a actualizar: ")
    if idEntrada in entradaIds:
        index = entradaIds.index(idEntrada)
        cantidad = input("Ingrese la nueva cantidad de la entrada (dejar en blanco para no cambiar): ")
        fecha = input("Ingrese la nueva fecha de la entrada (dejar en blanco para no cambiar): ")
        if cantidad:
            idProducto = entradaProductos[index]
            productos[idProducto]['cantidad'] += int(cantidad) - entradaCantidades[index]
            entradaCantidades[index] = int(cantidad)
        if fecha:
            entradaFechas[index] = fecha
        print(f"Entrada con ID {idEntrada} actualizada exitosamente.")
    else:
        print(f"La entrada con ID {idEntrada} no existe.")

def eliminarEntradaPorId():
    idEntrada = input("Ingrese el ID de la entrada a eliminar: ")
    if idEntrada in entradaIds:
        index = entradaIds.index(idEntrada)
        idProducto = entradaProductos[index]
        productos[idProducto]['cantidad'] -= entradaCantidades[index]
        del entradaIds[index]
        del entradaProductos[index]
        del entradaCantidades[index]
        del entradaFechas[index]
        print(f"Entrada con ID {idEntrada} eliminada exitosamente.")
    else:
        print(f"La entrada con ID {idEntrada} no existe.")

def mostrarMenu():
    print("\n--- Menú CRUD ---")
    print("1. Crear producto")
    print("2. Leer productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto por ID")
    print("5. Crear entrada de producto")
    print("6. Leer entradas de producto")
    print("7. Actualizar entrada de producto")
    print("8. Eliminar entrada de producto por ID")
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
            crearEntrada()
        elif opcion == '6':
            leerEntradas()
        elif opcion == '7':
            actualizarEntrada()
        elif opcion == '8':
            eliminarEntradaPorId()
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
