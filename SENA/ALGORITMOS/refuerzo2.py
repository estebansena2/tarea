## crear dos crud para crear dos crud que permita crear un producto y uan estrada de producto
productos = {}
entradas = {}

# CRUD para productos
def crear_producto():
    id_producto = input("Ingrese el ID del producto: ")
    if id_producto in productos:
        print(f"El producto con ID {id_producto} ya existe.")
    else:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        productos[id_producto] = {'id': id_producto, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        print(f"Producto {nombre} creado exitosamente con ID {id_producto}.")

def leer_productos():
    if productos:
        for id_producto, detalles in productos.items():
            print(f"ID: {id_producto}, Producto: {detalles['nombre']}, Precio: {detalles['precio']}, Cantidad: {detalles['cantidad']}")
    else:
        print("No hay productos en el inventario.")

def actualizar_producto():
    id_producto = input("Ingrese el ID del producto a actualizar: ")
    if id_producto in productos:
        nombre = input("Ingrese el nuevo nombre del producto (dejar en blanco para no cambiar): ")
        precio = input("Ingrese el nuevo precio del producto (dejar en blanco para no cambiar): ")
        cantidad = input("Ingrese la nueva cantidad del producto (dejar en blanco para no cambiar): ")
        if nombre:
            productos[id_producto]['nombre'] = nombre
        if precio:
            productos[id_producto]['precio'] = float(precio)
        if cantidad:
            productos[id_producto]['cantidad'] = int(cantidad)
        print(f"Producto con ID {id_producto} actualizado exitosamente.")
    else:
        print(f"El producto con ID {id_producto} no existe.")

def eliminarProductoPorId():
    id_producto = input("Ingrese el ID del producto a eliminar: ")
    if id_producto in productos:
        del productos[id_producto]
        print(f"Producto con ID {id_producto} eliminado exitosamente.")
    else:
        print(f"El producto con ID {id_producto} no existe.")

# CRUD para entradas de producto
def crearEntrada():
    id_entrada = input("Ingrese el ID de la entrada: ")
    id_producto = input("Ingrese el ID del producto: ")
    if id_producto in productos:
        if id_entrada in entradas:
            print(f"La entrada con ID {id_entrada} ya existe.")
        else:
            cantidad = int(input("Ingrese la cantidad de la entrada: "))
            fecha = input("Ingrese la fecha de la entrada (YYYY-MM-DD): ")
            entradas[id_entrada] = {'id': id_entrada, 'id_producto': id_producto, 'cantidad': cantidad, 'fecha': fecha}
            productos[id_producto]['cantidad'] += cantidad
            print(f"Entrada {id_entrada} creada exitosamente y stock actualizado.")
    else:
        print(f"El producto con ID {id_producto} no existe.")

def leerEntradas():
    if entradas:
        for id_entrada, detalles in entradas.items():
            print(f"ID Entrada: {id_entrada}, ID Producto: {detalles['id_producto']}, Cantidad: {detalles['cantidad']}, Fecha: {detalles['fecha']}")
    else:
        print("No hay entradas registradas.")

def actualizarEntrada():
    id_entrada = input("Ingrese el ID de la entrada a actualizar: ")
    if id_entrada in entradas:
        cantidad = input("Ingrese la nueva cantidad de la entrada (dejar en blanco para no cambiar): ")
        fecha = input("Ingrese la nueva fecha de la entrada (dejar en blanco para no cambiar): ")
        if cantidad:
            id_producto = entradas[id_entrada]['id_producto']
            productos[id_producto]['cantidad'] += int(cantidad) - entradas[id_entrada]['cantidad']
            entradas[id_entrada]['cantidad'] = int(cantidad)
        if fecha:
            entradas[id_entrada]['fecha'] = fecha
        print(f"Entrada con ID {id_entrada} actualizada exitosamente.")
    else:
        print(f"La entrada con ID {id_entrada} no existe.")

def eliminarEntradaporid():
    id_entrada = input("Ingrese el ID de la entrada a eliminar: ")
    if id_entrada in entradas:
        id_producto = entradas[id_entrada]['id_producto']
        productos[id_producto]['cantidad'] -= entradas[id_entrada]['cantidad']
        del entradas[id_entrada]
        print(f"Entrada con ID {id_entrada} eliminada exitosamente.")
    else:
        print(f"La entrada con ID {id_entrada} no existe.")

def mostrar_menu():
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
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_producto()
        elif opcion == '2':
            leer_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminarProductoPorId()
        elif opcion == '5':
            crearEntrada()
        elif opcion == '6':
            leerEntradas()
        elif opcion == '7':
            actualizarEntrada()
        elif opcion == '8':
            eliminarEntradaporid()
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            