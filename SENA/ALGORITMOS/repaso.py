import os
os.system ("clear")
#Ejercicio 1: Crear una Lista

#Crea una lista con los números del 1 al 5 y muestra el resultado.

lista=[1,2,3,4,5]
print (lista)

#Ejercicio 2: Acceder al Tercer Elemento

#Accede y muestra el tercer elemento de la lista creada anteriormente.
print(lista[3])
 
 #Ejercicio 3: Modificar el Segundo Elemento

#Cambia el segundo elemento de la lista a 10 y muestra la lista modificada.
lista[1] = 10

print(lista)
#Ejercicio 4: Agregar un Elemento

#Usa `append()` para agregar el número 6 al final de la lista y muestra la lista actualizada.
lista.append(6)

print(lista)
#Usa `remove ()` para eliminar el número 3 de la lista y muestra el resultado.

busca=3

lista.remove(busca)

print(lista)
#Ejercicio 6: Eliminar un Elemento por Índice

#Usa `del` para eliminar el primer elemento de la lista y muestra la lista después de la eliminación.

i=0

del lista[i]

print(lista)

#Ejercicio 7: Longitud de la Lista

#Muestra la longitud de la lista actual.

print(len(lista))

#Ejercicio 8: Extender la Lista

#Usa `extend()` para agregar los números [7, 8, 9] al final de la lista y muestra el resultado.

lista.extend([7, 8, 9])

print(lista)

#Ejercicio 9: Insertar un Elemento

#Usa `insert()` para agregar el número 0 al inicio de la lista y muestra la lista modificada.

lista.insert(0, 0)

print(lista)
#Ejercicio 10: Limpiar la Lista

#Usa `clear()` para eliminar todos los elementos de la lista y muestra la lista vacía.

lista.clear()

print(lista)

#Ejercicio 11: Revertir la Lista

#Crea una lista nueva con los números del 1 al 5, revierte su orden con `reverse()` y muestra el resultado.

lista = [1, 2, 3, 4, 5]

lista.reverse()

print(lista)

#Ejercicio 12: Ordenar la Lista

#Crea una lista desordenada, úsala para ordenar los elementos con `sort()` y muestra la lista ordenada.

lista_desordenada = [5, 3, 1, 4, 2]

lista_desordenada.sort()

print(lista_desordenada)

#Ejercicio 13: Índice de un Elemento

#Encuentra y muestra el índice del número 4 en la lista ordenada.

indice = lista_desordenada.index(4)

print(indice)

#Ejercicio 14: Último Elemento con `pop()`

##Muestra y elimina el último elemento de la lista usando `pop()`, y luego muestra la lista modificada.

ultimo = lista_desordenada.pop()

print(ultimo)

print(lista_desordenada)

# también elimina con el índice del campo

lista_desordenada.pop(i)

#Ejercicio 15: Crear Lista de Listas

#Crea una lista de listas donde cada sublista contiene tres números consecutivos y muestra la lista de listas.

lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista_de_listas)

#Ejercicio 16: Acceder a Elementos de Sublistas

#Accede y muestra el primer elemento de la primera sublista.

print(lista_de_listas[0][0])

#Ejercicio 17: Añadir Sublista

#Añade una nueva sublista `[10, 11, 12]` usando `append()` y muestra la lista de listas.

lista_de_listas.append([10, 11, 12])

print(lista_de_listas)

#Ejercicio 18: Fusionar dos Listas en Una Nueva Lista

#Crea dos listas, fusiona sus elementos en una nueva lista usando el método extend() y muestra la nueva lista.

lista1 = [1, 2, 3]

lista2 = [4, 5, 6]

lista1.extend(lista2)

print(lista1)

#Ejercicio 19: Lista de Strings

#Crea una lista de strings con los nombres de cinco frutas y usa sort() para ordenarlos alfabéticamente.

frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]

frutas.sort()

print(frutas)

#Ejercicio 20: Eliminar Elemento Específico Usando pop()

#Elimina el segundo elemento de la lista de frutas usando pop() y muestra la lista modificada y el elemento eliminado.

i = 2

elemento_eliminado = frutas.pop(i)

print(elemento_eliminado)

print(frutas)

#Ejercicio 21: Eliminar todo el contenido de una lista clear()

lista.clear()