# Crear en el diccionario LIBRO los siguientes registros ID, Nombre, Descripcion, Autor y Genero literario, debes hacer un crud, que te permita crearLibro, LeerLibro (id), ActualizarLibro (id) y EliminarLibro (id).  
# Guiate del siguiente codigo y hazlo similar. 
#productos[nombre] = {'precio': precio, 'cantidad': cantidad} 
#libro[id] ={'nombres':nombre, ...} 

libros = {}


def crearLibro(id, nombre, descripcion, autor, genero):
    if id in libros:
        return f"El libro con ID {id} ya existe."
    libros[id] = {
        'nombre': nombre,
        'descripcion': descripcion,
        'autor': autor,
        'genero': genero
    }
    return f"Libro {nombre} creado con éxito."


def leerLibro(id):
    if id not in libros:
        return f"El libro con ID {id} no existe."
    return libros[id]


def actualizarLibro(id, nombre=None, descripcion=None, autor=None, genero=None):
    if id not in libros:
        return f"El libro con ID {id} no existe."
    
    if nombre:
        libros[id]['nombre'] = nombre
    if descripcion:
        libros[id]['descripcion'] = descripcion
    if autor:
        libros[id]['autor'] = autor
    if genero:
        libros[id]['genero'] = genero
        
    return f"Libro con ID {id} actualizado con éxito."


def eliminarLibro(id):
    if id not in libros:
        return f"El libro con ID {id} no existe."
    del libros[id]
    return f"Libro con ID {id} eliminado con éxito."


print(crearLibro())
print(leerLibro())
print(actualizarLibro())
print(leerLibro())
print(eliminarLibro())
print(leerLibro())
