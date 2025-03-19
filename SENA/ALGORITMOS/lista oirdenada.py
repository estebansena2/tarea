# Definir una lista de palabras
lista_de_palabras = ["manzana", "banana", "pera", "kiwi", "uva", "naranja"]

# Implementar el algoritmo de ordenamiento de burbuja
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Intercambiar los elementos
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Ordenar la lista usando el algoritmo de burbuja
bubble_sort(lista_de_palabras)

# Imprimir la lista ordenada
print("Lista de palabras en orden alfabético:")
print(lista_de_palabras)
