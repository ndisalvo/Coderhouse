nombre = input('Cual es tu nombre?: ')
print('Bienvenido ' + nombre + '. Vamos a calcular tu nota final. Por favor ingresa tus dos calificaciones:')

nota_1 = int(input('Nota 1: '))
nota1 = nota_1
promedio1 = nota1 * 40/100
print('Tu nota 1 es', promedio1)
print('----------')

nota_2 = int(input('Nota 2: '))
nota2 = nota_2
promedio2 = nota2 * 60/100
print('Tu nota 2 es', promedio2)
print('----------')

nota_final = promedio1 + promedio2

print('Tu nota final es:', nota_final)
print('----------')