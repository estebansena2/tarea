#Escribe una función en Python que reciba una lista de números enteros y devuelva la sublista contigua que tenga la mayor suma.
def sublista_mayor_suma(lista):
    max_suma = lista[0]
    max_terminar = lista[0]
    inicio = fin = 0
    inicio_temp = 0
    
    for i in range(1, len(lista)):
        if max_terminar + lista[i] < lista[i]:
            max_terminar = lista[i]
            inicio_temp = i
        else:
            max_terminar += lista[i]
        
        if max_terminar > max_suma:
            max_suma = max_terminar
            inicio = inicio_temp
            fin = i
    
    return lista[inicio:fin + 1]

lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sublista_mayor_suma(lista))


