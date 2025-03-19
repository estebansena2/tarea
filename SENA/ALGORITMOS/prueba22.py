
# Crear en el diccionario LIBRO los siguientes registros ID, Nombre, Descripcion, Autor y Genero literario, debes hacer un crud, que te permita crearLibro, LeerLibro (id), ActualizarLibro (id) y EliminarLibro (id).  
# Guiate del siguiente codigo y hazlo similar. 
#productos[nombre] = {'precio': precio, 'cantidad': cantidad} 
#libro[id] ={'nombres':nombre, ...} 
opcion=0
while opcion != 5:
    print("1. Crear Libro")
    print("2. Leer Libro")
    print("3. Actualizar Libro")
    print("4. Eliminar Libro")
    print("5. Salir")
    opcion = int(input("Ingrese alguna opcion del menu: "))
    Libro = {}

    if opcion == 1:
        
         def crearLibro(id, nombre, descripcion, autor, genero):
            Libro[id] = {'nombre': nombre, 'descripcion': descripcion, 'autor': autor, 'genero': genero}
            print(crearLibro(Libro))
            
    if opcion == 2:
        
        def leerLibro(id):
            if id in Libro:
                return Libro[id]
    
            print(leerLibro(Libro))
           
    
    if opcion == 3: 
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
            print(actualizarLibro(Libro))
    
    if opcion == 4:
        def eliminarLibro(id):
            if id in Libro:
                del Libro[id]
                return "Libro eliminado"
            print(eliminarLibro(Libro))   
    if opcion == 5:
        print("Saliste del menú")
        break
        
1
        
