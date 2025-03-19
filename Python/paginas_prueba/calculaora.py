def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        operacion = input("Ingresa el número de la operación (1/2/3/4) o 'q' para salir: ")

        if operacion == 'q':
            print("¡Adiós!")
            break

        if operacion not in ['1', '2', '3', '4']:
            print("Operación no válida. Intenta de nuevo.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingresa números válidos.")
            continue

        if operacion == '1':
            print(f"{num1} + {num2} = {suma(num1, num2)}")
        elif operacion == '2':
            print(f"{num1} - {num2} = {resta(num1, num2)}")
        elif operacion == '3':
            print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
        elif operacion == '4':
            resultado = division(num1, num2)
            print(f"{num1} / {num2} = {resultado}")


calculadora()
