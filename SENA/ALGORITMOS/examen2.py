#1¿Cuál es la suma de los elementos de la lista lista = [1, 2, 3, 4, 5]? - Fórmula: sum(lista)
lista=[1,2,3,4,5]
suma=sum(lista)
print(suma)

#2
producto = 1
for numero in lista:
    producto = producto * numero
    print(producto)
    lista=[1,2,3,4,5]
    
    
#3Cuántas veces aparece el número 3 en la lista lista = [1, 2, 3, 4, 5, 3, 3]?
lista = [1, 2, 3, 4, 5, 3, 3]
contador=lista.count(3)
print(contador)

#4 Cuál es el valor máximo y mínimo en la lista lista = [1, 2, 3, 4, 5]?
lista = [1, 2, 3, 4, 5]
max=max(lista)
min=min(lista)
print(min)
print(max)

#5 Cuál es la lista sin duplicados de lista = [1, 2, 3, 4, 5, 3, 3]?

list(set(lista))
print(lista)

#6¿Cuál es la lista después de intercambiar el primer y último elemento de lista = [1, 2, 3, 4, 5]?
lista[0], lista[-1] = lista[-1], lista[0]
print(lista)

#7 ¿Cuál es la lista después de invertir la sublista lista[1:4] de lista = [1, 2, 3, 4, 5]?
sublista = lista[1:4]
sublista.reverse()
lista[1:4] = sublista
print(sublista)

#8 Cuántos números pares e impares hay en la lista lista = [1, 2, 3, 4, 5]?
lista = [1, 2, 3, 4, 5]

numpares = len([num for num in lista if num % 2 == 0])

numimpares = len([num for num in lista if num % 2 != 0])

print("Números pares:", numpares)

print("Números impares:", numimpares)
 
 #9¿Cuál es la cadena concatenada de la lista de strings frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]?

frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]

cadena_concatenada = "".join(frutas)

print( cadena_concatenada) 

#10 Cuáles números de la lista lista = [1, 2, 3, 4, 5] son mayores que 3
lista = [1, 2, 3, 4, 5]

valor = 3

filtrados = [num for num in lista if num > valor]

print( valor, ":", filtrados) 

#11 Cuál es la suma de los elementos de la sublista lista[1:4] de lista = [1, 2, 3, 4, 5]?

lista = [1, 2, 3, 4, 5]

sublista = lista[1:4] 

sumsublista = sum(sublista)

print( sumsublista) 

# 12 ¿Cuál es el promedio de los elementos de la lista lista = [1, 2, 3, 4, 5]?

lista = [1, 2, 3, 4, 5]

promedio = sum(lista) / len(lista)

print(promedio)

#13 ¿Cuáles son los números pares en la lista lista = [1, 2, 3, 4, 5]?
lista = [1, 2, 3, 4, 5]

numeros_pares = [num for num in lista if num % 2 == 0]

print( numeros_pares)

#14 ¿Cuál es la lista de los cuadrados de los números del 1 al 5?

cuadrados = [num**2 for num in range(1, 6)]

print( cuadrados)

#15 ¿El número 3 existe en la lista lista = [1, 2, 3, 4, 5]?
lista = [1, 2, 3, 4, 5]

numeroAbuscar = 3

existe = numeroAbuscar in lista

print({numeroAbuscar} , existe)

#16 Cuál es la lista de números negativos del -1 al -10?

negativos = [-num for num in range(1, 11)]

print( negativos)
 
 #17 ¿Cuál es la lista resultante de concatenar lista1 = [1, 2, 3] y lista2 = [4, 5, 6]?

lista1 = [1, 2, 3]

lista2 = [4, 5, 6]

listanueva= lista1 + lista2

print(listanueva)

#18 Cuál es la lista de pares ordenados (tuplas) a partir de lista1 = [1, 2, 3] y lista2 = ['a', 'b', 'c']?

lista1 = [1, 2, 3]

lista2 = ['a', 'b', 'c']

paresOrdenados = list(zip(lista1, lista2))

print( paresOrdenados)

#19 ¿Cuál es la lista con los primeros 5 números naturales?
N = 5

primerosnumerosnaturales = list(range(1, N+1)) 

print("los primeros", N, "números naturales son:", primerosnumerosnaturales)

#20 ¿Cuál es la lista de palabras en mayúsculas de palabras = ["HoLa", "MUNDO", "pYThon"]?

palabras = ["HoLa", "MUNDO", "pYThon"]
palabrasMayusculas = [palabra.upper() for palabra in palabras]
print( palabrasMayusculas)

