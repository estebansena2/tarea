#*USANDO ELIF y Try Except: Desarrolla un algoritmo en Python que solicite al usuario ingresar tres números y luego imprima el mayor de los tres, el menor de los 3,
# si son iguales, si al menos hay dos iguales. Asegúrate de que tu código maneje correctamente cualquier tipo de números (positivos, negativos y decimales). Después de completar
# tu algoritmo, muestra tu código al profesor para su revisión. Una vez que tu solución haya sido revisada y aprobada, copia y pega tu código en word y conviertelo en pdf y subelo en el espacio a continuación.
try:
    print("ingrese 3 numeros diferentes\n")
    num1=int(input("ingrese el primer numero"))
    num2=int(input("ingrese el segundo numero"))
    num3=int(input("ingrese el tercer numero"))

    if num1 > num2 and num1 < num3:
        print("el numero mayor es el ",num3,"y el menor es",num2)
    elif num2 >num1 and num2< num3:
        print("el numero mayor es el",num3," y el menor es ", num1)
    elif num3 >num2 and num3< num1:
        print("el numero mayor es el ",num1,"y el el menor es ",num2)
    elif num1< num2 and num1 >num3:
        print("numero menor es ",num1,"y numero mayor es",num2)
    elif num2< num1 and num2> num3:
        print("numero menor es el ",num2,"y numero mayor es",num1)
    elif num3 <num1 and num1 > num2:
        print("el numero menor es el ", num2,"y el mayor es ",num1)
    else:
        ("alguno de los numero esta repetido ")
        
except:
    print(" verifique que este ingresadno numero")