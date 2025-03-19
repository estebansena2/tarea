EJERCICIOS ESTRUCTURA SEGÚN CASO

⦁	Elabore un algoritmo que permita ingresar un número entero (1 a 10), y muestre su equivalente en romano.

Número Entero (1 a 10) NE, Equivalente en Romano ER
Inicio
Leer NE
EN CASO NE SEA
CASO 1
	ER = “I”
CASO 2
	ER = “II”
CASO 3
	ER = “III”
CASO 4
	ER = “IV”
CASO 5
	ER = “V”
CASO 6
	ER = “VI”
CASO 7
	ER = “VII”
CASO 8
	ER = “VIII”
CASO 9
	ER = “IX”
CASO 10
	ER = “X”
FIN_CASO
Escribir ER
Fin

#solución en Python con elif que es switch o según caso
numero_entero = int (input ("Ingrese un número entero del 1 al 10: "))
if numero_entero == 1:
    equivalente_romano = 'I'
elif numero_entero == 2:
    equivalente_romano = 'II'
elif numero_entero == 3:
    equivalente_romano = 'III'
elif numero_entero == 4:
    equivalente_romano = 'IV'
elif numero_entero == 5:
    equivalente_romano = 'V'
elif numero_entero == 6:
    equivalente_romano = 'VI'
elif numero_entero == 7:
    equivalente_romano = 'VII'
elif numero_entero == 8:
    equivalente_romano = 'VIII'
elif numero_entero == 9:
    equivalente_romano = 'IX'
elif numero_entero == 10:
    equivalente_romano = 'X'
else:
    equivalente_romano = "Número fuera de rango"
print ("El equivalente en romano es:", equivalente_romano)
#con diccionario se puede resolver así:
def entero_a_romano (numero):
    romanos = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
    if numero in romanos:
        return romanos[numero]
    else:
        return "Número fuera de rango"

numero_entero = int (input ("Ingrese un número entero del 1 al 10: "))
print ("El equivalente en romano es:", entero_a_romano (numero_entero))

⦁	Elabore un algoritmo que permita ingresar el monto de venta alcanzado por un vendedor durante el mes, luego de calcular la bonificación que le corresponde sabiendo:
 
Monto de Venta MV
Total, de Bonificación TB
Inicio
Leer MV
EN CASO MV SEA
CASO MV >= 0 y MV < 1000 
	TB = (0  MV) / 100
CASO MV >= 1000 y MV < 5000 
	TB = (3  MV) / 100
CASO MV >= 5000 y MV < 20000 
	TB = (5  MV) / 100
CASO   MV >= 20000
	TB = (8  MV) / 100
Fin
FIN_CASO
Escribir TB
Fin

#solucion en Python con elif que es switch o según caso
monto_venta = float (input ("Ingrese el monto de venta del vendedor: "))
if monto_venta < 1000:
        boni=0
elif monto_venta < 5000:
       boni= 0.03 * monto_venta
elif monto_venta < 20000:
      boni= 0.05 * monto_venta
else:
      boni= 0.08 * monto_venta
print ("La bonificación es:", boni)

#solucion en Python con funciones
def calcular_bonificacion (monto_venta):
    if monto_venta < 1000:
        return 0
    elif monto_venta < 5000:
        return 0.03 * monto_venta
    elif monto_venta < 20000:
        return 0.05 * monto_venta
    else:
        return 0.08 * monto_venta

monto_venta = float (input ("Ingrese el monto de venta del vendedor: "))
print ("La bonificación es:", calcular_bonificacion(monto_venta))

⦁	Elabore un algoritmo que solicite un número entero y muestre un mensaje indicando la vocal correspondiente, considerando que la vocal A = 1.

Número Entero NE, 
Vocal V

Inicio
Leer NE
EN CASO NE SEA
CASO 1
	V = “A”
CASO 2
	V = “E”
CASO 3
	V = “I”
CASO 4
	V = “O”
CASO 5
	V = “U”
OTRO CASO
	V = “Valor Incorrecto”
FIN_CASO
Escribir V
Fin

#solucion python con elif que es similar a según case o también llamado switch
numero_entero = int (input ("Ingrese un número entero del 1 al 5: "))
if numero_entero == 1:
    vocal_correspondiente = 'A'
elif numero_entero == 2:
    vocal_correspondiente = 'E'
elif numero_entero == 3:
    vocal_correspondiente = 'I'
elif numero_entero == 4:
    vocal_correspondiente = 'O'
elif numero_entero == 5:
    vocal_correspondiente = 'U'
else:
    vocal_correspondiente = "Valor Incorrecto"
print ("La vocal correspondiente es:", vocal_correspondiente)

#solucion python sin funciones y con diccionarios
numero_entero = int (input ("Ingrese un número entero del 1 al 5: "))
vocales = {1: 'A', 2: 'E', 3: 'I', 4: 'O', 5: 'U'}
if numero in vocales:
    respuesta= vocales[numero]
else:
    respuesta= "Valor Incorrecto"
print ("La vocal correspondiente es:", respuesta)

#solucion python con funciones y diccionarios
def asignar_vocal (numero):
    vocales = {1: 'A', 2: 'E', 3: 'I', 4: 'O', 5: 'U'}
    if numero in vocales:
        return vocales[numero]
    else:
        return "Valor Incorrecto"
numero_entero = int (input ("Ingrese un número entero del 1 al 5: "))
print ("La vocal correspondiente es:", asignar_vocal(numero_entero))

17. Ejercicio 1: Clasificación de edades.

 Escribe un programa que reciba una edad como entrada y clasifique a la persona en las siguientes categorías: niño (menos de 11 años), adolescente (12-17 años), adulto (18-64 años) o mayor (65 años o más).
Opcional: preadolescente: 11 a 13 y adolescente de 14 a 17
   Solución:
   edad = int (input ("Introduce la edad: "))

   if edad < 11:
       print ("La persona es un niño.")
   elif 12 <= edad < 18:
       print ("La persona es un adolescente.")
   elif 18 <= edad < 65:
       print ("La persona es un adulto.")
   else:
       print ("La persona es mayor.")

18. Ejercicio 2: Clasificación de notas.

    Escribe un programa que reciba una nota (0-100) y la clasifique en: deficiente (menos de 50), aprobado (50-64), notable (65-84), sobresaliente (85-100).

   Solución:
   nota = int (input ("Introduce la nota: "))

   if nota < 50:
       print("Deficiente ")
   elif 50 <= nota < 65:
       print("Aprobado")
   elif 65 <= nota < 85:
       print("Notable")
   elif 85 <= nota <= 100:
       print("Sobresaliente")
   else:
       print ("Nota fuera del rango permitido.")

19. Ejercicio 3: Clasificación de temperaturas.

    Escribe un programa que reciba una temperatura (en grados Celsius) y la clasifique en: frío (menos de 10°C), templado (10-20°C), cálido (21-30°C) o caluroso (más de 30°C).

   Solución:
Forma #1 con and
temp = float (input ("Introduce la temperatura en grados Celsius: "))
if temp < 10:
    print("Frío")
elif temp >= 10 and temp <= 20:
    print("Templado")
elif temp >= 21 and temp <= 30:
    print("Cálido")
elif temp > 30:
    print("Caluroso")

Forma #2 sin and (es único en python)
   temp = float (input ("Introduce la temperatura en grados Celsius: "))
   if temp < 10:
       print("Frío")
   elif 10 <= temp <= 20:
       print("Templado")
   elif 21 <= temp <= 30:
       print("Cálido")
   elif temp > 30:
       print("Caluroso")

20. Ejercicio 4: Clasificación de IMC.

 Escribe un programa que reciba el Índice de Masa Corporal (IMC) de una persona y lo clasifique en: bajo peso (menos de 18.5), normal (18.5-24.9), sobrepeso (25-29.9) u obeso (30 o más).

   Solución:
   imc = float (input ("Introduce el IMC: "))
   if imc < 18.5:
       print ("Bajo peso")
   elif 18.5 <= imc < 25:
       print("Normal")
   elif 25 <= imc < 30:
       print("Sobrepeso")
   elif imc >= 30:
       print("Obeso")

21. Ejercicio 5: Evaluación del viento.

 Escribe un programa que reciba la velocidad del viento (en km/h) y la clasifique en: calmado (menos de 5 km/h), ligero (5-19 km/h), moderado (20-39 km/h) o fuerte (más de 40 km/h).

   Solución:
   velocidad = float (input ("Introduce la velocidad del viento en km/h: "))
   if velocidad < 5:
       print("Viento calmado")
   elif 5 <= velocidad < 20:
       print("Viento ligero")
   elif 20 <= velocidad < 40:
       print("Viento moderado")
   elif velocidad >= 40:
       print("Viento fuerte")

22. Ejercicio 6: Clasificación de automóviles.

    Escribe un programa que reciba la velocidad máxima de un automóvil (en km/h) y lo clasifique en: económico (menos de 140 km/h), estándar (140-180 km/h), deportivo (181-220 km/h) o de alto rendimiento (más de 220 km/h).

   Solución:

   velocidad = float(input("Introduce la velocidad máxima del automóvil en km/h: "))
   if velocidad < 140:
       print("Automóvil económico")
   elif 140 <= velocidad <= 180:
       print("Automóvil estándar")
   elif 181 <= velocidad <= 220:
       print("Automóvil deportivo")
   elif velocidad > 220:
       print("Automóvil de alto rendimiento")

23. Ejercicio 7: Clasificación de alturas.

    Escribe un programa que reciba la altura de una persona (en centímetros) y la clasifique en: baja (menos de 150 cm), promedio (150-180 cm) o alta (más de 180 cm).

   Solución:

   altura = float(input("Introduce la altura de la persona en centímetros: "))

   if altura < 150:
       print("Persona baja")
   elif 150 <= altura <= 180:
       print("Persona de estatura promedio")
   elif altura > 180:
       print("Persona alta")

24. Ejercicio 8: Clasificación de nivel de lectura.

    Escribe un programa que reciba la cantidad de libros leídos por una persona en un año y la clasifique en: no lector (menos de 1 libro), ocasional (1-4 libros), frecuente (5-12 libros) o ávido lector (más de 12 libros).

   Solución:
   libros = int (input ("Introduce la cantidad de libros leídos en un año: "))
   if libros < 1:
       print ("No lector")
   elif 1 <= libros <= 4:
       print ("Lector ocasional")
   elif 5 <= libros <= 12:
       print ("Lector frecuente")
   elif libros > 12:
       print ("Ávido lector")

25. Ejercicio 9: Clasificación de tamaños de pantalla.

 Escribe un programa que reciba el tamaño de una pantalla (en pulgadas) y la clasifique en: pequeña (menos de 15 pulgadas), mediana (15-27 pulgadas), grande (28-40 pulgadas) o muy grande (más de 40 pulgadas).

   Solución:

   pulgadas = float (input ("Introduce el tamaño de la pantalla en pulgadas: "))
   if pulgadas < 15:
       print ("Pantalla pequeña")
   elif 15 <= pulgadas <= 27:
       print ("Pantalla mediana")
   elif 28 <= pulgadas <= 40:
       print ("Pantalla grande")
   elif pulgadas > 40:
       print ("Pantalla muy grande")

26. Ejercicio 10: Clasificación de sueldos.

     Escribe un programa que reciba el sueldo mensual de una persona y lo clasifique en: bajo (menos de 1000 euros), medio (1000-3000 euros), alto (3001-5000 euros) o muy alto (más de 5000 euros).

    Solución:

    sueldo = float (input ("Introduce el sueldo mensual en euros: "))
    if sueldo < 1000:
        print ("Sueldo bajo")
    elif 1000 <= sueldo <= 3000:
        print ("Sueldo medio")
    elif 3001 <= sueldo <= 5000:
        print ("Sueldo alto")
    elif sueldo > 5000:
        print ("Sueldo muy alto")

27.	Elaborar un algoritmo que solicite 2 números enteros y un operador aritmético y luego debe de mostrar el resultado de la operación correspondiente.
 
Inicio
Leer N1, Leer N2, Leer OP
EN CASO OP SEA
CASO “+”
	R = N1 + N2
CASO “-”
	R = N1 – N2
CASO “*”
	R = N1 * N2
CASO “^”
	R = N1 ^ N2
OTRO CASO
R = 0
FIN_CASO
Escribir R
Fin