#*USANDO ELIF y Try Except: Desarrolla un algoritmo en Python que solicite al usuario ingresar tres números y luego imprima el mayor de los tres, el del medio de los 3,
# el menor de los 3, si son iguales, si al menos hay dos iguales. Asegúrate de que tu código maneje correctamente cualquier tipo de números (positivos, negativos y decimales).
# Después de completar tu algoritmo, muestra tu código al profesor para su revisión. Una vez que tu solución haya sido revisada y aprobada, copia y pega tu código en word
# y conviertelo en pdf y subelo en el espacio a continuación.
try:
    
    num1 = float(input("Ingresa el primer número: \n"))
    num2 = float(input("Ingresa el segundo número:\n"))
    num3 = float(input("Ingresa el tercer número:\n"))

    if num1==num2 and num2==num3 and num3==num1:
        print("los numeros estan repetidos")
    elif num1==num2 or num2==num3:
        print(" almenos dos numeros son iguales")
        
    elif num1>num2 and num2>num3:
        print("el mumero mayor es",num1,"\nel numero del medio es",num2,"\ny el numero menor es",num3)
    elif num2>num1 and num1>num3:
        print("el mumero mayor es",num2,"\nel numero del medio es",num1,"\ny el numero menor es",num3)
    elif num3>num2 and num2>num1:
        print  ("el mumero mayor es",num3,"\nel numero del medio es",num2,"\nel numero menor es",num1)
    elif num3>num1 and num1>num2:
        print ("el mumero mayor es",num3,"\nel numero del medio es",num1,"\nel numero menor es",num3)
    elif num2>num3 and num3>num1:
        print("el mumero mayor es",num2,"\nel numero del medio es",num3,"\nel numero menor es",num1)
    elif num1>num3 and num3> num1:
        print("el mumero mayor es",num1,"\nel numero del medio es",num3,"\n1el numero menor es",num2)
    elif num1>num2 and num3>num2:
        print("el mumero mayor es",num1,"\nel numero del medio es",num3,"\n1el numero menor es",num2)
    
except ValueError:
     print("digite numeros porfavor")