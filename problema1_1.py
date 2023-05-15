'''
Escriba una función que reciba una lista y que regrese como resultado una tupla almacenado
el primer y el último elemento de la lista. En caso de que la lista no tenga dos o mas 
elementos, debe lanzar una excepción.
'''

def primero_ultimo(lista):
    '''
        obtiene el primero y el ultimo elemento de una lista, la funcion debe recivir un parametro tipo lista y debe 
        tener almenos 2 elementos, de lo contrario debe lanzar una exception
    '''
    if type(lista) != list:
        raise TypeError('El parametro debe ser una lista')
    else:
        if len(lista) < 2:
           raise ValueError('La lista debe tener almenos 2 elementos')
        else:
            return (lista[0], lista[-1])

#lista con mas de dos elementos   
lista1 = [1,2,3,4,5,6]
print('\nCP1',primero_ultimo(lista1))
print('------------------------------')

#lista con 1 elemento
lista2 = [6]
try:
    print('\nCP2',primero_ultimo(lista2))
except Exception as error:
    print('CP2', error)
print('------------------------------')

# No se pasa una lista
lista3 = 1
try:
    print('\nCP3',primero_ultimo(lista3))
except Exception as error:
    print('CP3', error)
print('------------------------------')