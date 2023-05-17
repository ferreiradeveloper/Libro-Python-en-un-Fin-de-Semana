'''
Escriba una función que reciba una lista y que regrese True si en la
lista hay, por lo menos, dos elementos tipo cadena de caracteres (str).
En caso contrario deberá regresar False. Además, debe escribir un programa 
para probar la función desarrollada.
'''
def determina_minimo_2cadenas(lista):
    limite = len(lista)
    indice = 0
    contador = 0
    while indice < limite and contador <2:
        if type(lista[indice])== str:
            contador +=1
        indice +=1
    return contador == 2

# CP1: se da una lista con 4 cadenas
list1 = ['rojo','verde','blanco','amarillo']
if determina_minimo_2cadenas(list1):
    print('\nCP1: Sí hay, minimo, 2cadenas')
else:
    print('\nCP1: No hay, minimo, 2cadenas')

# CP2: se da una lista con 2 cadenas y otros datos
list2 = ['rojo',True,21,'amarillo',0.30]
if determina_minimo_2cadenas(list2):
    print('\nCP2: Sí hay, minimo, 2cadenas')
else:
    print('\nCP2: No hay, minimo, 2cadenas')

# CP3: se da una lista con 1 cadena
list2.pop(0)
if determina_minimo_2cadenas(list2):
    print('\nCP3: Sí hay, minimo, 2cadenas')
else:
    print('\nCP3: No hay, minimo, 2cadenas')

# CP4: se da una lista sin cadenas
list3 = [1,2,5]
if determina_minimo_2cadenas(list3):
    print('\nCP4: Sí hay, minimo, 2cadenas')
else:
    print('\nCP4: No hay, minimo, 2cadenas')

# CP5: se da una lista vacia
list3.clear() # vaciamos la lista
if determina_minimo_2cadenas(list3):
    print('\nCP5: Sí hay, minimo, 2cadenas')
else:
    print('\nCP5: No hay, minimo, 2cadenas')