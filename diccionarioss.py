#Supongamos que renemos un programa que maneja un carrito de compras
carrito={'diademas':31, 'Mouse':50, 'Gemini pro':10}

#Vamos a hacer un programa donde podamos ver elementos del carro, agregarlos, actualizarlos, eliminarlos.
#Como una forma de menu, en donde al selecionar la opcion, haga el procedimiento

while True:
    opcione=input ('Que deseas hacer: (Agregar, Modificar, Eliminar, Salir).  ').capitalize()
    
    if opcione=='Salir':
        print('Compra finalizada. El carrito final es:')
        print (carrito)
        break
        
    elif opcione=='Agregar':
        producto=input ('Ingresa el nombre del producto')
        cantidad=int(input('Ingresa la cantidad del producto'))
        if producto in carrito:
            print('Oye ese producto ya está en el carrito')
        else:
            carrito[producto]=cantidad
            print('Producto agregado')
    
        
    elif opcione=='Eliminar':
        producto=input ('Ingresa el nombre del producto a eliminar')
        if producto in carrito:
        #Eliminar el producto
            del carrito[producto]
        
    #Actualizar la cantidad de elementos de un producto
        
    elif opcione=='Modificar':
        producto=input ('Ingresa el nombre del producto a modificar')
        if producto in carrito:
            cantidad=int(input('Ingresa la nueva cantidad'))
            carrito[producto]=cantidad
            print ('Cantidad actualizada')
        else:
            print ('El producto no esta en el carrito porfavor intente')
            
    else:
        print('Opción inválida')
    print('Carrito actual: ', carrito)
    print('________________________________')