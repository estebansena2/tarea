import os
os.system("clear")
opcion = 0
try:
    while opcion != 21:
        print("1: Sumar pares y impares")
        print("2: Producto de pares y impares")
        print("3: Elementos comunes")
        print("4: Numeros eliminados")
        print("5: Cubos")
        print("6: Ordenar por longitud")
        print("7: Remover elementos negativos")
        print("8: Encontrar el segundo mayor numero")
        print("9: Intercalar Elementos de dos Listas")
        print("10: Dividir la lista en dos partes")
        print("11: Crear una lista de factoriales")
        print("12: Filtrar palabras")
        print("13: Duplicar el elemento de una lista")
        print("14: Alternar mayúsculas y minúsculas")
        print("21: Salir")
        print("")
        opcion = int(input("Ingrese alguna opcion del menu: "))
        print("")
        if opcion == 1:
            lista = [1, 2, 3, 4, 5, 6]
            suma_pares = sum(num for num in lista if num % 2 == 0)
            suma_impares = sum(num for num in lista if num % 2 != 0)
            print("La suma de los elementos pares es:", suma_pares)
            print("La suma de los elementos impares es:", suma_impares)
        elif opcion == 2:
            lista = [1, 2, 3, 4, 5, 6]
            productos_impares = 1
            for num in lista:
                if num % 2 != 0:
                    productos_impares *= num
            print("El producto de los elementos impares es:", productos_impares)
        elif opcion == 3:
            lista1 = [1, 2, 3, 4, 5]
            lista2 = [4, 5, 6, 7, 8]
            comunes = list(set(lista1) & set(lista2))
            print("Elementos comunes:", comunes)
        elif opcion == 4:
            lista = [1, 2, 3, 4, 5, 6, 7, 8]
            n = 3
            listaA = lista[n:]
            print("Lista después de eliminar los primeros", n, "elementos:", listaA)
            listaB = lista[:-n]
            print("Lista después de eliminar los últimos", n, "elementos:", listaB)
        elif opcion == 5:
            cubos = [num**3 for num in range(1, 11)]
            print("Lista de cubos:", cubos)
        elif opcion == 6:
            palabras = ["python", "es", "un", "lenguaje", "de", "programación"]
            palabras_ordenadas = sorted(palabras, key=len)
            print("Palabras ordenadas por longitud:", palabras_ordenadas)
        elif opcion == 7:
            lista = [1, -2, 3, -4, 5, -6]
            lista_positiva = [abs(num) for num in lista]
            print("Lista de valores absolutos:", lista_positiva)
            lista_positiva2 = [num for num in lista if num >= 0]
            print("Lista sin elementos negativos:", lista_positiva2)
            lista_negativos = [num for num in lista if num < 0]
            print("Lista de negativos:", lista_negativos)
        elif opcion == 8:
            lista = [1, 2, 3, 4, 5]
            mayor = max(lista)
            menor = min(lista)
            lista_sin_mayor = [num for num in lista if num != mayor]
            segundo_mayor = max(lista_sin_mayor)
            print("Numero menor:", menor)
            print("Numero mayor:", mayor)
            print("El segundo mayor número es:", segundo_mayor)
        elif opcion == 9:
            lista1 = [1, 3, 5]
            lista2 = [2, 4, 6]
            lista_intercalada = [None] * (len(lista1) + len(lista2))
            lista_intercalada[::2] = lista1
            lista_intercalada[1::2] = lista2
            print("Lista intercalada:", lista_intercalada)
        elif opcion == 10:
            lista = [1, 7, 5, 0, 4, 8, 9]
            mitad = len(lista) // 2
            if len(lista) % 2 != 0:
                mitad += 1
            lista1 = lista[:mitad]
            lista2 = lista[mitad:]
            print("Primera parte:", lista1)
            print("Segunda parte:", lista2)
        elif opcion == 11:
            import math
            factoriales = [math.factorial(num) for num in range(1, 6)]
            print("Lista de factoriales:", factoriales)
        elif opcion == 12:
            palabras = ["hola", "mundo", "holanda", "python", "holístico"]
            subcadena = "hol"
            palabras_filtradas = [palabra for palabra in palabras if subcadena in palabra]
            print("Palabras que contienen 'hol':", palabras_filtradas)
        elif opcion == 13:
            lista = [1, 2, 3, 4, 5]
            lista_duplicada = [num * 2 for num in lista]
            print("Lista con elementos duplicados:", lista_duplicada)
        elif opcion == 14:
            palabras = ["python", "es", "genial"]
            palabras_alt = [palabra.upper() if i % 2 == 0 else palabra.lower() for i, palabra in enumerate(palabras)]
            print("Palabras con alternación de mayúsculas y minúsculas según si es par o impar:", palabras_alt)
        elif opcion == 21:
            print("Saliste del menú")
            break
except ValueError:
    print("Error: Entrada no válida")

