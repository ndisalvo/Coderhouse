'''
# 1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:


Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
En caso de no introducir una opción válida, el programa informará de que no es correcta.


init = True

while init == True:
    print ("""
    Menu:
    1- Sumar
    2- Restar
    3- Multiplicar
    4- Finalizar 
    """)

    start = int(input("Por favor ingrese lo que desea realizar: "))
    
    if start == 1:
        print('\nVamos a sumar!')
        num1 = int(input('\nPor favor ingrese el Numero 1: '))
        num2 = int(input('\nPor favor ingrese el Numero 2: '))
        print('La suma de', num1, 'y de', num2, 'es de:', num1 + num2)
        break

    elif start == 2:
        print('\nVamos a restar!')
        num1 = int(input('\nPor favor ingrese el Numero 1: '))
        num2 = int(input('\nPor favor ingrese el Numero 2: '))
        print('La resta de', num1, 'y de', num2, 'es de:', num1 - num2)
        break

    elif start == 3:
        print('\nVamos a multiplicar!')
        num1 = int(input('\nPor favor ingrese el Numero 1: '))
        num2 = int(input('\nPor favor ingrese el Numero 2: '))
        print('La multiplicacion de', num1, 'y de', num2, 'es de:', num1 * num2) 
        break

    elif start == 4:
        print('\nPrograma finalizado, muchas gracias!')
        break

    else:
        print('\nUsted no ha elegido ninguna de las opciones disponibles. Pruebe nuevamente')
        break

'''



'''
# 2) Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

num = 0
num = int(input('Por favor ingrese por teclado un numero impar: '))

while num % 2 == 0:
    print('Usted ha elegido un numero que es par, por favor intente nuevamente')
    num = int(input('Por favor ingrese por teclado un numero impar: '))

print('Usted ha elegido correctamente. Muchas gracias por usar el programa!')

'''



'''
# 3) Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

sum = 0

for i in range(0, 100):
    if i % 2 != 0:
        sum += i

print('La suma de los numeros impares del 0 al 100 es:', sum)

'''



'''
# 4) Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:
cont = 0
num = int(input('Ingrese la cantidad de numeros a calcular por favor:' ))

for x in range(num):
    cont += int(input('Introduce un número: '))

print('La media aritmetica es:', round(cont/num, 2))    

'''



'''
#5) Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se 
# encuentra en la lista de números y notificarlo:

numeros = [1, 3, 6, 9]
num = int(input('Escriba un numero del 0 al 9: '))

while num not in numeros:
    print('No se ha encontrado el numero. Por favor intente nuevamente.')
    num = int(input('Escriba un numero del 0 al 9: '))
else:
    print('Hemos encontrado el numero', num, 'en la lista!!')    

'''



'''
# 6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

list_1 = print(list(range(0, 11)))
list_2 = print(list(range(-10, 1)))
list_3 = print(list(range(0, 21, 2)))
list_4 = print(list(range(-19, 0, 2)))
list_5 = print(list(range(0, 51, 5)))

'''



'''
# 7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []

for letras in lista_1:
    if letras in lista_2 and letras not in lista_3:
        lista_3.append(letras)
    
print(lista_3)

'''