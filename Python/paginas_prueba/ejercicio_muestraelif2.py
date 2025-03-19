#⦁	Elabore un algoritmo que permita ingresar el monto de venta alcanzado por un vendedor durante el mes,
# luego de calcular la bonificación que le corresponde sabiendo:
#0-1000
#1000-5000
#5000-20000
#20000- +
try:
    
    monven=int(input("ingrese la el valor de venta realizada:\n"))
    if monven>0 and monven<1000:
        print("Su bonificacion es", 0 )
    elif monven>=999 and monven<5000:
            print("su bonificacion es ",(monven*100)/3)
    elif monven>=4999 and monven<20000:
            print("su bonificacion es ",(monven*5)/100)
    elif monven>=20000:
            print("su bonificacion es ",(monven*8)/100)
except:
    print("recuerde que el valor debe ser numerico")