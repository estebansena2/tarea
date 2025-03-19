try:
    opcion = 0
    while opcion != 21:

        print(".:Seleccione una opcion:.")
        print("1: Suma")
        print("2: Producto de la lista")
        print("3: Cuantas veces aparece el mismo numero")
        print("4: Valor Maximo y Minimo")
        print("5: Eliminar duplicados")
        print("6: Intercambiar el primer elemento por el ultimo")
        print("7: Invertir sub lista")
        print("8: Cuantos Numero Pares y Impares Hay en la lista")
        print("9: Cadena concatenada de frutas")
        print("10: Numeros de mayor valor")
        print("11: Suma de elementos de un Sublista")
        print("12: Promedio de elementos de la lista")
        print("13: Numero de pares en la lista")
        print("14: Lista de cuadrados")
        print("15: Saber si existe un numero dentro de la lista")
        print("16: Lista de numeros negativos")
        print("17: Lista de pares ordenados (tuplas)")
        print("18: Lista de los numeros naturales")
        print("19: Lista de palabras mayusculas")
        print("20: Salir del menu")

        opcion = int(input("Ingrese alguna opcion del menu: "))

        if opcion == 1:
            print("Suma")
            lista = [1, 2, 3, 4, 5]
            suma = sum(lista)
            print(suma)

        elif opcion == 2:
            print("Producto de la lista")
            lista = [1, 2, 3, 4, 5]
            producto = 1
            for numero in lista:
                producto *= numero
            print(producto)

        elif opcion == 3:
            print("Cuantas veces aparece el mismo numero")
            lista = [1, 2, 3, 4, 5, 3, 3]
            contador = lista.count(3)
            print(contador)

        elif opcion == 4:
            print("Valor Maximo y Minimo")
            lista = [1, 2, 3, 4, 5]
            max_valor = max(lista)
            min_valor = min(lista)
            print(min_valor)
            print(max_valor)

        elif opcion == 5:
            print("Eliminar duplicados")
            lista = [1, 2, 3, 4, 5, 3, 3]
            lista = list(set(lista))
            print(lista)

        elif opcion == 6:
            print("Intercambiar el primer elemento por el ultimo")
            lista = [1, 2, 3, 4, 5]
            lista[0], lista[-1] = lista[-1], lista[0]
            print(lista)

        elif opcion == 7:
            print("Invertir sub lista")
            lista = [1, 2, 3, 4, 5]
            sublista = lista[1:4]
            sublista.reverse()
            lista[1:4] = sublista
            print(lista)

        elif opcion == 8:
            print("Cuantos Numero Pares y Impares Hay en la lista")
            lista = [1, 2, 3, 4, 5]
            numpares = len([num for num in lista if num % 2 == 0])
            numimpares = len([num for num in lista if num % 2 != 0])
            print("Números pares:", numpares)
            print("Números impares:", numimpares)

        elif opcion == 9:
            print("Cadena concatenada de frutas")
            frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]
            cadena_concatenada = "".join(frutas)
            print(cadena_concatenada)

        elif opcion == 10:
            print("Numeros de mayor valor")
            lista = [1, 2, 3, 4, 5]
            valor = 3
            filtrados = [num for num in lista if num > valor]
            print(valor, ":", filtrados)

        elif opcion == 11:
            print("Suma de elementos de un Sublista")
            lista = [1, 2, 3, 4, 5]
            sublista = lista[1:4]
            sumsublista = sum(sublista)
            print(sumsublista)

        elif opcion == 12:
            print("Promedio de elementos de la lista")
            lista = [1, 2, 3, 4, 5]
            promedio = sum(lista) / len(lista)
            print(promedio)

        elif opcion == 13:
            print("Numero de pares en la lista")
            lista = [1, 2, 3, 4, 5]
            numeros_pares = [num for num in lista if num % 2 == 0]
            print(numeros_pares)

        elif opcion == 14:
            print("Lista de cuadrados")
            cuadrados = [num**2 for num in range(1, 6)]
            print(cuadrados)

        elif opcion == 15:
            print("Saber si existe un numero dentro de la lista")
            lista = [1, 2, 3, 4, 5]
            numero_a_buscar = 3
            existe = numero_a_buscar in lista
            print(f"{numero_a_buscar} existe: {existe}")

        elif opcion == 16:
            print("Lista de numeros negativos")
            negativos = [-num for num in range(1, 11)]
            print(negativos)

        elif opcion == 17:
            print("Lista de pares ordenados (tuplas)")
            lista1 = [1, 2, 3]
            lista2 = [4, 5, 6]
            pares_ordenados = list(zip(lista1, lista2))
            print(pares_ordenados)

        elif opcion == 18:
            print("Lista de los numeros naturales")
            lista = [1, 2, 3, 4, 5]
            print(lista)

        elif opcion == 19:
            print("Lista de palabras mayusculas")
            palabras = ["HoLa", "MUNDO", "pYThon"]
            palabras_mayusculas = [palabra.upper() for palabra in palabras]
            print(palabras_mayusculas)

        elif opcion == 20:
            print("Salir del menu")
            break

        elif opcion == 21:
            break

except:
    print("digite un numero valido")