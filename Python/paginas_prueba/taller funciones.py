
def suma(num1,num2):
    return num1 + num2

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "un error, se detectó una división por cero"
    return a / b

menuPrincipal=True
while menuPrincipal == True:
    respuestasPosibles=[1,2,3,4]
    respuesta= int(input("Selecciona la operacion\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Salir\nIngresa tu respuesta aqui: "))
    while respuesta in respuestasPosibles: 
        
        if respuesta == 1:
            print("digite dos numeros")
            num1=float(input("\nIngresa el primer numero: "))
            num2=float(input("Ingresa el segundo numero: "))
            print(f'\nEl resultado es',suma(num1,num2),f'tus respuestas fueron: {num1} + {num2},\n')  
            
            reintento=str(input("Quieres hacer otra operacion? Elige una opcion\n1.Si\n2.No\nIngresa tu opcion aca: "))
            if reintento=='si':
                respuestasPosibles=[0]
            elif reintento=='no':
                print("gracias")
                quit()
 
        elif respuesta ==2:
            num1=float(input("\nIngresa el primer numero: "))
            num2=float(input("Ingresa el segundo numero que se restará al primero: "))
            print(f'\nEl resultado es',resta(num1,num2),f'tus respuestas fueron: {num1} - {num2}\n')
            
            reintento=str(input("Quieres hacer otra operacion? Elige una opcion\n1.Si\n2.No\nIngresa tu opcion aca: "))
            if reintento=='si':
                respuestasPosibles=[0] 
            elif reintento=='no':
                print("gracias")
                quit()
             
        elif respuesta == 3:
            num1=float(input("\nIngresa el primer numero: "))
            num2=float(input("Ingresa el segundo numero: "))
            print(f'\nEl resultado es',multiplicacion(num1,num2),f'tus respuestas fueron: {num1}X{num2}\n')
        
            reintento=str(input("Quieres hacer otra operacion? Elige una opcion\n1.Si\n2.No\nIngresa tu opcion aca: "))
            if reintento=='si':
                respuestasPosibles=[0]
            elif reintento=='no':
                print("gracias")
                quit()
            
        else:
            num1=float(input("\nIngresa el primer numero: "))
            num2=float(input("Ingresa el numero de las veces a dividir el primer numero: "))
            print(f'\nEl resultado es',division(num1,num2),f'tus respuestas fueron: {num1}/{num2}\n')
            
            reintento=str(input("Quieres hacer otra operacion? Elige una opcion\n1.Si\n2.No\nIngresa tu opcion aca: "))
            if reintento=='si':
                respuestasPosibles=[0]     
            elif reintento=='no':
                print("gracias")
                quit()
    if respuesta==5:    
        print("Hasta luego")
        exit()