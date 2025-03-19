# Importamos la biblioteca de fechas y horas para utilizar en el programa
import datetime

# Creamos una clase Estudiante para manejar los datos de cada estudiante
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Asignamos el nombre del estudiante
        self.edad = edad  # Asignamos la edad del estudiante
        self.fecha_creacion = datetime.datetime.now()  # Guardamos la fecha y hora de creación del registro

    def __str__(self):
        # Retornamos una representación en cadena del objeto Estudiante
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Fecha de Creación: {self.fecha_creacion}"

# Creamos una clase SistemaEstudiantes para manejar la lista de estudiantes y las operaciones relacionadas
class SistemaEstudiantes:
    def __init__(self):
        self.estudiantes = []  # Inicializamos la lista de estudiantes vacía

    def agregar_estudiante(self, nombre, edad):
        # Creamos una instancia de Estudiante y la agregamos a la lista
        estudiante = Estudiante(nombre, edad)
        self.estudiantes.append(estudiante)
        print(f"Estudiante {nombre} agregado exitosamente.")

    def eliminar_estudiante(self, nombre):
        # Filtramos la lista de estudiantes excluyendo el estudiante con el nombre dado
        self.estudiantes = [est for est in self.estudiantes if est.nombre != nombre]
        print(f"Estudiante {nombre} eliminado exitosamente.")

    def buscar_estudiante(self, nombre):
        # Buscamos el estudiante por nombre
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                return estudiante
        return None

    def listar_estudiantes(self):
        # Listamos todos los estudiantes
        for estudiante in self.estudiantes:
            print(estudiante)

# Función principal para ejecutar el sistema de gestión de estudiantes
def main():
    # Creamos una instancia del sistema de estudiantes
    sistema = SistemaEstudiantes()
    
    # Agregamos algunos estudiantes
    sistema.agregar_estudiante("Juan", 20)
    sistema.agregar_estudiante("Ana", 22)
    sistema.agregar_estudiante("Luis", 21)
    
    # Listamos los estudiantes
    print("\nLista de estudiantes:")
    sistema.listar_estudiantes()
    
    # Buscamos un estudiante
    nombre_buscar = "Ana"
    estudiante_encontrado = sistema.buscar_estudiante(nombre_buscar)
    if estudiante_encontrado:
        print(f"\nEstudiante encontrado: {estudiante_encontrado}")
    else:
        print(f"\nEstudiante {nombre_buscar} no encontrado.")
    
    # Eliminamos un estudiante
    sistema.eliminar_estudiante("Luis")
    
    # Listamos nuevamente los estudiantes después de la eliminación
    print("\nLista de estudiantes después de la eliminación:")
    sistema.listar_estudiantes()

# Ejecutamos la función principal si este archivo es ejecutado como script
if __name__ == "__main__":
    main()
