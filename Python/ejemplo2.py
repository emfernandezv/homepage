
listado_productos = []
listado_precios = []
listado_cantidad = []

def programa():
    print('Welcome to Rodrigos  Market')
    print('MENU')
    print('1. Add Item')
    print('2. Remove Item')
    print('3. Display Cart')
    print('4. Total')
    print('5. Exit')
    option = str(input('What do you want to do?: '))
    #Validation
    while option not in ('1','2','3','4','5'):
        option = str(input('You have choosen an invalid option. What do you want to do?: '))
     
    print(f'You have choosen option: {option}')
    print()

    if option == '1':
        #add item
        producto = str(input('Please insert the product name: ')).upper()
        while len(producto) <= 1 :
            producto = str(input('You have to input a name for your product. Please insert the product name: '))
        
        #add price
        precio  = float(input('Please insert the product price: '))
        while precio < 0 :
            precio = str(input('Please insert a valid price. Please insert the produc price: '))
        
        #add quantity
        cantidad  = float(input('Please insert the product quantity: '))
        while cantidad <= 0 :
            cantidad = str(input('Please insert a valid quantity. Please insert the produc quantity: '))

        listado_productos.append(producto)
        listado_precios.append(precio)
        listado_cantidad.append(cantidad)

        print(f'You have added: {producto} , quantity: {cantidad}, unit price: ${precio}, to your shopping cart.')
        print()
        programa()
    elif option == '2':
        #remove item
        producto = str(input('Please insert the product to remove: ')).upper()
        indice = 0
        while indice < len(listado_productos):
            if listado_productos[indice] == producto:
                listado_productos.pop(indice)
                listado_precios.pop(indice)
                listado_cantidad.pop(indice)
                print(f'You have removed: {producto}, from your shopping cart.')
                print()
                programa()
            else:
                print('The product does not exist in your cart')
                producto = str(input('Please insert the product to remove: ')).upper()
            indice = indice + 1
        
    elif option == '3':
        #display cart
        print('You shopping cart has: ')
        indice = 0
        while indice < len(listado_productos):
            print(f'Item: {indice} - {listado_productos[indice]} - Quantity: {listado_cantidad[indice]} - ${listado_precios[indice]}')
            indice = indice + 1    
        print()
        programa()
    elif option == '4':
        #Operation
        indice = 0
        valor = 0
        while indice < len(listado_productos):
            valor = valor + (listado_cantidad[indice] * listado_precios[indice])
            indice = indice + 1    
        print()    
        print(f'The total is: {valor}')
        print()
        programa()
    else:
        print('Thanks for using our system.')
        exit()

programa()

