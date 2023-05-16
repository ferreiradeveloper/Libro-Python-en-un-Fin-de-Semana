'''
En este problema se piden dos funciones. La primera de ellas debe ser una función booleana
que recibe dos listas de númros, lista1 y lista2, y que regresa True si se cumple la siguiente
condición: el primer elemento de la lista1 es multiplo del primer elemento de la lista2, el
segundo elemento de la lista1 es multiplo del segundo elemento de la lista2 y asi sucesivamente
hasta el final de la lista, Ademas las listas deben tener el mismo número de componentes. si
alguna o ambas condiciones no se cumple, la funcion regresa False.
La segunda función debe recibir una lista de números y un entero positivo (n) y debe calcular y 
regresar el promedio de los números que ocupan posiciones múltiplos de n.
'''
def todos_son_multiplos(list1, list2):
    if len(list1) == len(list2):
        limite = len(list1)
        index = 0
        while index < limite and list1[index]%list2[index]==0:
            index += 1
        respuesta = index == limite
    else:
        respuesta = False
    return respuesta


#CP1: se proporcionan dos listas de números que cumplan con las condiciones
lista1 = [9,16,15,8,21] 
lista2 = [3,4,5,8,7]
if todos_son_multiplos(lista1,lista2):
    print('\nCP1: Si cumple con las condiciones.')
else:
    print('\nCP1: No cumple con las condiciones.')

#CP2: se proporcionan dos listas de números con longitudes diferentes
lista3 = [9,16,15,8,21,17] 
if todos_son_multiplos(lista1,lista3):
    print('\nCP2: Si cumple con las condiciones.')
else:
    print('\nCP2: No cumple con las condiciones.')
     
#CP3: se proporcionan dos listas de números con longitudes diferentes
lista4 = [4,2,5,8,7] 
if todos_son_multiplos(lista1,lista4):
    print('\nCP3: Si cumple con las condiciones.')
else:
    print('\nCP3: No cumple con las condiciones.')


def calcula_promedio(list, n):
    suma = 0
    contador = 0
    for i, elemento in enumerate(list):
        if i%n == 0:
            suma += elemento
            contador += 1
    try:
        promedio = suma/contador
        return promedio
    except:
        raise ArithmeticError('No se puede calcular promedio.')
    
#CP4: se proporciona una lista de números enteros.
lista5 = [9,16,15,8,21,17]
prom1 = calcula_promedio(lista5,2)
print('\nCP4 --> Promedio enteros =', prom1)

#CP5: se proporciona una lista de números reales.
lista6 = [9.1,-1.6,1.5,3.8,2.1,1.7]
prom2 = calcula_promedio(lista6,3)
print('\nCP5 --> Promedio reales =', prom2)

#CP6: se proporciona una lista vacia.
lista7 = []
try:
    prom3 = calcula_promedio(lista7,5)
    print('\nCP6 --> Promedio (lista vacía) =', prom3)
except ArithmeticError as e:
    print('\nCP6 --> Error:', e)