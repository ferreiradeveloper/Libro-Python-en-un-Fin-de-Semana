'''
Escriba una función que reciba una lista y un elemento a buscar y que regrese la posición del elemento
en la lista. Si no lo encuentra regrese -1.
Analice el problema y en posible no utilice index()
'''
def buscar_elemento(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
    else:
        return -1

#CP1 Se da lista de nombres y un nombre existente
lista1 = ['Juan','Jose','Pedro','Mario','Francisco', 'Manuel']
nombre = 'Francisco'
print('\nCP1 - Francisco esta en la Posición',buscar_elemento(lista1, nombre))

#CP1 Se da lista de nombres y un nombre no existente
nombre = 'Edward'
print('\nCP1 - Edward esta en la Posición',buscar_elemento(lista1, nombre))

#CP1 Se da lista vacia y un nombre
lista1.clear()
nombre = 'Francisco'
print('\nCP1 - Edward esta en la Posición',buscar_elemento(lista1, nombre))