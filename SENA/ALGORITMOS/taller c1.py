#Ejercicio 1: Sumar Elementos Pares

#Escribe un algoritmo que sume todos los elementos pares de una lista de números enteros.

lista = [1, 2, 3, 4, 5, 6]
sumaPares= sum(num for num in lista if num % 2==0)
sumaImpares= sum(num for num in lista if num % 2!=0)

print(" la suma de numero pares es: ",sumaPares)
print(" la suma de numero Impares es: ",sumaImpares)

#Ejercicio 2: Producto de Elementos Impares

#Escribe un algoritmo que calcule el producto de todos los elementos impares de una lista de números enteros.
lista = [1, 2, 3, 4, 5, 6]

producto_impares = 1

for num in lista:

    if num % 2 != 0:

        producto_impares *= num

print("El producto de los elementos impares es:", producto_impares)

#combinacion ejercicio 1 y dos
 
lista = [1, 2, 3, 4, 5, 6]
opcion = 0

while opcion != 3:
    print("Ingrese 1 para saber la suma de pares e impares")
    print("Ingrese 2 para saber el cálculo de pares e impares")
    print("Ingrese 3 para salir del programa")
    
    opcion = int(input("Ingrese alguna opción del menú: "))
    
    if opcion == 1:
        sumaPares = sum(num for num in lista if num % 2 == 0)
        sumaImpares = sum(num for num in lista if num % 2 != 0)
        
        print("La suma de los números pares es:", sumaPares)
        print("La suma de los números impares es:", sumaImpares)

    elif opcion == 2:
        productoImpares = 1
        for num in lista:
            if num % 2 != 0:
                productoImpares *= num
            print("El producto de los números impares es:", productoImpares)    
        productoPares = 2
        for num in lista:
            if num % 2 == 0:
                productoPares *= num
            print("El producto de los números pares es:", productoPares)
    
        
    else:
        
        print("Saliendo del programa...")
        break
    
