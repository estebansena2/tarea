#Ejercicio 1: Crear una Lista Crea una lista con los números del 1 al 5 y muestra el resultado.

lista= [1,2,3,4,5]
print(lista)
#Ejercicio 2: Acceder al Tercer ElementoAccede y muestra el tercer elemento de la lista creada anteriormente.

print(lista[3])

#Ejercicio 3: Modificar el Segundo ElementoCambia el segundo elemento de la lista a 10 y muestra la lista modificada.

lista[1]=10

#Ejercicio 4: Agregar un Elemento Usa `append()` para agregar el número 6 al final de la lista y muestra la lista actualizada.

lista.append(6)
print(lista)

#Ejercicio 5: Eliminar un Elemento por ValorUsa `remove()` para eliminar el número 3 de la lista y muestra el resultado.
buscar=(3)
lista.remove(4)
print(lista)

#Ejercicio 5: Eliminar un Elemento por Valor Usa `remove()` para eliminar el número 3 de la lista y muestra el resultado.
del lista[1]
print(lista)

#Ejercicio 7: Longitud de la Lista Muestra la longitud de la lista actual.

print(len(lista))

#Ejercicio 8: Extender la Lista Usa `extend()` para agregar los números [7, 8, 9] al final de la lista y muestra el resultado.
vector1=[7,8,9]
lista.extend(vector1)
print(lista)

#Ejercicio 9: Insertar un Elemento Usa `insert()` para agregar el número 0 al inicio de la lista y muestra la lista modificada.
lista.insert(0,"Esteban")
print(lista)

#Ejercicio 10: Limpiar la Lista Usa `clear()` para eliminar todos los elementos de la lista y muestra la lista vacía.
lista.clear()
print(lista)

#Ejercicio 11: Revertir la Lista Crea una lista nueva con los números del 1 al 5, revierte su orden con `reverse()` y muestra el resultado.

listanueva=[1,2,3,4,5]
listanueva.reverse()
print(listanueva)

#Ejercicio 12: Ordenar la Lista Crea una lista desordenada, úsala para ordenar los elementos con `sort()` y muestra la lista ordenada.

listadesordenada = [5, 3, 1, 444, 2]
listadesordenada.sort()
print(listadesordenada)

#Ejercicio 13: Índice de un Elemento Encuentra y muestra el índice del número 4 en la lista ordenada.
indice=listadesordenada.index(444)
print(indice)

#Ejercicio 14: Último Elemento con `pop()` Muestra y elimina el último elemento de la lista usando `pop()`, y luego muestra la lista modificada.

ultimo=listadesordenada.pop
print(ultimo)
print(listadesordenada)
