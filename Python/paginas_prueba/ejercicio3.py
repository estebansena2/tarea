#
#solucion python con elif que es similar a según case o también llamado switch
try:
    Vocal=int(input("Ingrese un mumero entre el 1 y 5 pasa saber a que vocal equivale\n"))
    if Vocal==1:
        print("su equivalente es: A.")
    elif Vocal==2:
        print("su equivalente es: E.")
    elif Vocal==3:
        print("su equivalente es: I.")
    elif Vocal==4:
        print("su equivalente es: O.")
    elif Vocal==5:
        print("su equivalente es: U.")
    else:
        print("el numero que ingreso no esta en el rango requerido")
    
except:
    print("ingrese numero porfavor")    