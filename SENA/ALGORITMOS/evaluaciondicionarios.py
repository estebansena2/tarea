# Diccionario para almacenar los libros
libros = {}

# Función para crear un libro
def crearLibro(id, nombre, descripcion, autor, genero):
    if id in libros:
        print(f"Error: Ya existe un libro con ID {id}.")
        return
    libros[id] = {
        'nombre': nombre,
        'descripcion': descripcion,
        'autor': autor,
        'genero': genero
    }
    print(f"Libro con ID {id} ha sido creado exitosamente.")

# Función para leer un libro por su ID
def leerLibro(id):
    if id not in libros:
        print(f"Error: No existe un libro con ID {id}.")
        return
    libro = libros[id]
    print(f"ID: {id}\nNombre: {libro['nombre']}\nDescripción: {libro['descripcion']}\nAutor: {libro['autor']}\nGénero: {libro['genero']}")

# Función para actualizar un libro por su ID
def actualizarLibro(id, nombre=None, descripcion=None, autor=None, genero=None):
    if id not in libros:
        print(f"Error: No existe un libro con ID {id}.")
        return
    if nombre:
        libros[id]['nombre'] = nombre
    if descripcion:
        libros[id]['descripcion'] = descripcion
    if autor:
        libros[id]['autor'] = autor
    if genero:
        libros[id]['genero'] = genero
    print(f"Libro con ID {id} ha sido actualizado exitosamente.")

# Función para eliminar un libro por su ID
def eliminarLibro(id):
    if id not in libros:
        print(f"Error: No existe un libro con ID {id}.")
        return
    del libros[id]
    print(f"Libro con ID {id} ha sido eliminado exitosamente.")

# Ejemplos de uso
crearLibro(1, "Cien Años de Soledad", "Una novela de Gabriel García Márquez", "Gabriel García Márquez", "Realismo Mágico")
leerLibro(1)
actualizarLibro(1, descripcion="Una novela icónica de Gabriel García Márquez")
leerLibro(1)
eliminarLibro(1)
leerLibro(1)



