import os
os.system("clear")
opcion = 0
Libro = {}
try:
    while opcion != 5:
        print("1. Crear Libro")
        print("2. Leer Libro")
        print("3. Actualizar Libro")
        print("4. Eliminar Libro")
        print("5. Salir")
        opcion = int(input("Ingrese alguna opcion del menu: "))
        print("")
    Libro = {}

    if opcion == 1:
         def crearLibro(id, nombre, descripcion, autor, genero):
            Libro[id] = {'nombre': nombre, 'descripcion': descripcion, 'autor': autor, 'genero': genero}
            print (input(f"libro {nombre} creado exitosamente."))

    if opcion == 2:
        def leerLibro(id):
            if id in Libro:
                return Libro[id]
            
            else:
                return "Libro no encontrado"
                
    
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
            else:
                return "Libro no encontrado"
    
    if opcion == 4:
        def eliminarLibro(id):
            if id in Libro:
                del Libro[id]
                return "Libro eliminado"
            else:
                return "Libro no encontrado"    
    elif opcion == 5:
        print("Saliste del menú")
        exit()
except ValueError:
    print("Error: Entrada no válida")
        
    