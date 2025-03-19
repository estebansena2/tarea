import os 
os.system("clear")
producto=[]
cantidad=[]
precio=[]
opc=0
while opc != 9:
    print("")
    print(".:INVENTARIO DE PRODUCTOS:.")
    print("")
    print("1 - Crear producto")    
    print("2 - Buscar producto")
    print("3 - Actualizar producto")
    print("4 - Eliminar producto")
    print("5 - Listar producto")
    print("6 - Ordenar producto por nombre")
    print("7 - Invertir los productos")
    print("8 - Eliminar todos los productos")
    print("9 - Salir del panel del producto")
    opc=int(input("ingrese una opcion del menú: "))
    print("")
    if opc== 1:
        os.system("clear")        
        print("<:submenú crear producto:>")
        apro=input("Nombre del producto: ")
        acan=int(input("Cual es la cantidad: "))
        apre=float(input("Cual es el precio: "))
        producto.append(apro)
        cantidad.append(acan)
        precio.append(apre)
    if opc== 2:
        os.system("clear")
        print("<:submenú buscar producto:>")
        busPro=input("Ingrese el nombre del producto a buscar: ")
        if busPro in producto:
            print("Producto encontrado")            
            i=producto.index(busPro)
            print(producto[i])
            print(cantidad[i])
            print(precio[i])
        else:
            print("El producto no fué econtrado")
    if opc== 3:
        os.system("clear")
        print("<:submenú actualizar producto:>")
        busPro=input("Ingrese el nombre del producto a actualizar: ")
        if busPro in producto:
            print("Producto encontrado")            
            i=producto.index(busPro)
            producto[i]=input("Cual es el nuevo nombre: ")
            cantidad[i]=int(input("Cual es la nueva cantidad: "))
            precio[i]=float(input("Cual es el nuevo precio: "))        
            print("El producto fué econtrado y actualizado con éxito")
        else:
            print("El producto no fué econtrado")
    if opc== 4:
        os.system("clear")
        print("submenú eliminar producto")
        busPro=input("Ingrese el nombre del producto a eliminar: ")
        if busPro in producto:
            print("Producto encontrado")            
            i=producto.index(busPro)
            elEliProd=producto.pop(i)
            elEliCant=cantidad.pop(i)
            elEliPrec=precio.pop(i)        
            print(f"El producto {elEliProd} con cantidad {elEliCant} y precio {elEliPrec} fue eliminado con éxito")
        else:
            print("El producto no fué econtrado")
    if opc== 5:
        os.system("clear")
        print("submenú listar producto")
        if producto:
            print("listado de productos")
            for p,c,pr in zip(producto,cantidad,precio):
                print (f"producto {p} cantidad {c} precio {pr}")
        else:
            print("No hay productos para mostrar")    
    if opc== 6:
        os.system("clear")
        print("submenú ordenar producto")
        if producto:
            producto, cantidad, precio = zip(*sorted(zip[producto,cantidad,precio]))
        else:
            print("No hay productos para mostrar")    
    if opc== 7:
        os.system("clear")
        print("submenú invertir producto")
        if producto:
            producto.reverse()
            cantidad.reverse()
            precio.reverse()
        else:
            print("No hay productos para mostrar")  
    if opc== 8:
        os.system("clear")
        print("submenú crear producto")
        if producto:
            producto.clear()
            cantidad.clear()
            precio.clear()
        else:
            print("No hay productos para borrar") 
print("Panel del producto ha finalizado con éxito.")