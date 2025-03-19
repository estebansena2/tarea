Libro = {}

# Crear libro
def crearLibro(id, nombre, descripcion, autor, genero):
    Libro[id] = {'nombre': nombre, 'descripcion': descripcion, 'autor': autor, 'genero': genero}
    print("Libro creado:", Libro[id])

# Leer libro        
def leerLibro(id):
    if id in Libro:
        return Libro[id]
    else:
        print("El libro con id", id, "no existe.")

# Actualizar libro                 
def actualizarLibro(id, nombre=None, descripcion=None, autor=None, genero=None):
    if id in Libro:
        if nombre:
            Libro[id]['nombre'] = nombre
        if descripcion:
            Libro[id]['descripcion'] = descripcion
        if autor:
            Libro[id]['autor'] = autor
        if genero:
            Libro[id]['genero'] = genero
        return Libro[id]
    else:
        print("El libro con id", id, "no existe.")

# Eliminar libro  
def eliminarLibro(id):
    if id in Libro:
        del Libro[id]
        return "Libro eliminado"
    else:
        print("El libro con id", id, "no existe.")

opcion = 0    
while opcion != 5:
    print("\n1. Crear Libro")
    print("2. Leer Libro")
    print("3. Actualizar Libro")
    print("4. Eliminar Libro")
    print("5. Salir")
   
    opcion = int(input("Ingrese una opción del menú: "))   
    
    if opcion == 1:
        id = int(input("Ingrese el id del libro: "))
        nombre = input("Ingrese el nombre del libro: ")
        descripcion = input("Ingrese la descripción del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        crearLibro(id, nombre, descripcion, autor, genero)
         
    elif opcion == 2:
        id = int(input("Ingrese el id del libro: "))
        libro = leerLibro(id)
        if libro:
            print(f"ID: {id}, Nombre: {libro['nombre']}, Descripción: {libro['descripcion']}, Autor: {libro['autor']}, Género: {libro['genero']}")

    elif opcion == 3:
        id = int(input("Ingrese el id del libro a actualizar: "))
        nombre = input("Ingrese el nuevo nombre del libro (presione enter para dejarlo igual): ")
        descripcion = input("Ingrese la nueva descripción del libro (presione enter para dejarlo igual): ")
        autor = input("Ingrese el nuevo autor del libro (presione enter para dejarlo igual): ")
        genero = input("Ingrese el nuevo género del libro (presione enter para dejarlo igual): ")
        libro_actualizado = actualizarLibro(id, nombre or None, descripcion or None, autor or None, genero or None)
        if libro_actualizado:
            print("Libro actualizado:", libro_actualizado)
        
    elif opcion == 4:
        id = int(input("Ingrese el id del libro a borrar: "))
        resultado = eliminarLibro(id)
        if resultado:
            print(resultado)

    elif opcion == 5:
        print("Saliendo del programa.")
    
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
