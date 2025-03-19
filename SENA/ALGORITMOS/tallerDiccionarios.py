#Ejercicio 1: Elabore un algoritmo que permita ingresar un número entero (1 a 10), y muestre su equivalente en romano.

def enteroRomano(num):
    romanos={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}
    if num in romanos:
        return romanos[num]
        
    else:
        return"numero fuera de rango"

if __name__=="__main__":
    numBuscar=int(input("ingresa un numero del 1 al 10 para saber su equivalente romano: \n"))
    print("el quivalente en ronamno es: ",enteroRomano(numBuscar))
 
#Ejercicio 3: Crear un Diccionario de Estudiantes
#Crea un diccionario donde las claves sean los nombres de los estudiantes y los valores sean sus calificaciones   

def crear_diccionario_estudiantes():
    estudiantes = {
        "Ana": 85,
        "Luis": 92,
        "Carlos": 78,
        "María": 95,
        "Pedro": 88
    }
    return estudiantes
if __name__=="__main__":
    dicNotas=crear_diccionario_estudiantes()
    print(dicNotas)
    
    nom=input("ingrese el nombre del nuevo Estudiante")
    nota=int(input("ingrese la nota del nuevo estudiante"))
    dicNotas[nom]=nota
    print(dicNotas)
    
#promedio
    promedio=sum(dicNotas.values())/len(dicNotas)
    print(f"el promedio del salon es:\n{promedio}")
    
#nombres de los estudiantes que su nota
    estudiantesPasaron=[clave for clave,valor in dicNotas.items() if valor>=90]
    print(estudiantesPasaron)
#eliminar un registro del diccionario con clave
nombreaborrar = input("Ingrese el nombre del estudiante a borrar: ")
listaEditada = [clave for clave, valor in dicNotas.items() if clave == nombreaborrar]
if listaEditada:
    dicNotas.pop(nombreaborrar)
    print(dicNotas)
#