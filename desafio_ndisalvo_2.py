
#!ejercicio 1
def area_Rectangulo(b, a):
    area = b * a
    return area

run = area_Rectangulo(12, 20); print(a)

#!ejercicio 2
pi = 3.14159

def area_Circulo(pr, a):
    area_2 = pi * a ** 2
    return area_2

run_2 = area_Circulo(pi, 5); print(run_2)    

#!ejercico 3
def relacion(num_1, num_2):
    if num_1 > num_2:
        return(1)
    elif num_1 < num_2:
        return(-1)
    else:
        return(0)

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))

#!ejercico 4
def interm(num_1, num_2):
    funcion = (num_1 + num_2) / 2
    return funcion

run = intermedio(-12, 24); print(run)

#!ejercico 5
def recortar(cut, LI, LS):
    if cut < LI:
        return LI
    if cut > LS:
        return LS
    if cut > LI and cut < LS:
        return cut

run = recortar(15, 0, 10); print(run)

#!ejercicio 6
lista = list(range(1, 25))
def separar(lista):
    pares, impares = [], []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

run= separar(lista); print(run)                