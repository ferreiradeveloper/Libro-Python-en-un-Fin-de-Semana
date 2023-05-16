'''
Escriba una función que reciba un a lista que regrese el total de números positivos
que contiene. Se puede suoner que todos los elementos de la lista son del mismo tipo,
aunque de antemano no se sabe de que tipo son. En su solución debe prever qué pasa 
si la lista no almacena valores numéricos.
'''
def cuenta_positivos(lista):
    if lista and (type(lista[0])== int or type(lista[0])== float):
        positivos =0
        for numero in lista:
            # if numero == int or numero == float:
            if (type(numero) == int or type(numero) == float) and  numero>0:
                positivos +=1
        return positivos
    raise ValueError('Error en los datos: no es un dato válido o no tiene números.')

# CP1: se proporciona una lista de números enteros
lista1 = [405,-107,210,5,-23,-45,87,27,59,-1]
print('nCP1 - Total positivos =',cuenta_positivos(lista1))
print('----------------------------------------')

# CP2: se proporciona una lista de números reales negativos.
lista2 = [-107,-5,-23,-45,-87,-27,-59,-1]
print('nCP1 - Total positivos =',cuenta_positivos(lista2))
print('----------------------------------------')

# CP3: se proporciona una lista de strings
lista3 = ['Venezuela', 'Portugal', 'España','USA']
try:
    print('nCP3 - Total positivos =',cuenta_positivos(lista3))
except ValueError as e:
    print('CP3-', e)
print('----------------------------------------')

# CP4: No se proporciona una lista
lista4 = None
try:
    print('nCP4 - Total positivos =',cuenta_positivos(lista4))
except ValueError as e:
    print('CP4-', e)
print('----------------------------------------')

# CP5: No todos los elementos de la lista son números
lista5 = [107,5,'25',-45,-87,-27,-59,1]
try:
    print('nCP5 - Total positivos =',cuenta_positivos(lista5))
except ValueError as e:
    print('CP5-', e)
print('----------------------------------------')