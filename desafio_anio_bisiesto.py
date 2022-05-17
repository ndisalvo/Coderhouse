def año_bisiesto():
    
    while True:
        año = input('Ingrese un año por favor: ')
        try:
            año = int(año)
            if año % 4 == 0 and (año % 100 != 0 or año % 400 != 0):
                return 'El año es bisiesto'
            

            else:
                return 'El año no es bisiesto'
            break    
        except ValueError:
            print('Por favor ingresar unicamente numeros enteros. Por favor, ingrese un nuevo número:')       

año_bisiesto()