
listado_productos = []

def programa():
    print('Welcome to Rodrigos  Market')
    print('MENU')
    print('1. Add Item')
    print('2. Remove Item')
    print('3. Display Cart')
    print('4. Exit')
    option = str(input('What do you want to do?: '))
    #Validation
    while option not in ('1','2','3','4'):
        option = str(input('You have choosen an invalid option. What do you want to do?: '))
     
    print(f'You have choosen option: {option}')
    print()

    if option == '1':
        #add item
        producto = str(input('Please insert the product name: ')).upper()
        while len(producto) <= 1 :
            option = str(input('You have to input a name for your product. Please insert the product name: '))

        listado_productos.append(producto)
        print(f'You have added: {producto}, to your shopping cart.')
        print()
        programa()
    elif option == '2':
        #remove item
        producto = str(input('Please insert the product to remove: ')).upper()
        while producto not in listado_productos:
            producto = str(input('The product doesnt exists. Please insert the product to remove: ')).upper()

        listado_productos.remove(producto)
        print(f'You have removed: {producto}, from your shopping cwart.')
        print()
        programa()
    elif option == '3':
        #display cart
        indice = 0
        print('You shopping cart has: ')
        while indice < len(listado_productos):
            print(f'Item: {indice} - {listado_productos[indice]}')
            indice = indice + 1    
        print()
        programa()
    else:
        print('Thanks for using our system.')
        exit()

programa()

