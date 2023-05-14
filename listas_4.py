# Copiado de Listas
'''
    Python cuenta con dos tipos de copiado de listas.
    Copia Superficial: se crea una nueva lista y luego se copian en ella las referencias a los elementos de la
    lista original.
    Copia Deep (profunda): se crea una nueva lista y luego se copian en ella los elementos de la lista original.

    La copia en elementos inmutables es practicamente ya que estos pueden modificarse una vez definidos. La
    diferencia se manifiesta cuan se tiene datos mutables, ya que con la superficial es el mismo dato (objeto) al
    cual se accede a través de dos variables distintas y por lo tanto cualquier cambio realizado en una repecurtira en 
    la otra. En el caso de la copia profunda, se crean copias de los elementos y por tanto los cambios aplicados a la
    lista original no repercuten en la copia y viceversa, Cada una de estas formas de copiado tiene una función a sociada,
    que son las funciones copy() y deepcopy(), respectivamente. Ambas forman parte del modulo de Python llamado copy.
    La operación slicing tambien permite copiar una lista, En este caso hace un copiado superficia y es de tener en cuenta 
    cuando se implemente con listas de datos mutables.
'''

# =============================================================================
# Ejemplos de copias superficiales y profundas de listas con datos inmutables.
# =============================================================================
dias_laborables = ["lunes", "martes", "miércoles", "jueves", "viernes"]
precios = [205.30, 107.18, 25, 450, 310.89]

dias = copy.copy(dias_laborables)  # Copiado superficial.
print('\nListas luego de la copia superficial'.upper())
print('Lista original:', dias_laborables)
print('Copia:', dias)

# Se modifica la lista original y la copia.
dias_laborables.pop(0)
dias.remove('viernes')
tit1 = '''\nListas luego de hacer modificaciones en ambas: 
    cada una conserva sus cambios.'''.upper()
print(tit1)
print('Lista original:', dias_laborables)
print('Copia:', dias)

copia_precios = copy.deepcopy(precios)  # Copiado profundo.
print('\nListas luego de la copia profunda'.upper())
print('Lista original:', precios)
print('Copia:', copia_precios)

# Se modifica la lista original y la copia.
precios.append(720.14)
copia_precios.pop(2)
print(tit1)
print('Lista original:', precios)
print('Copia:', copia_precios)

# =============================================================================
# Ejemplos de copias superficiales y profundas de listas con datos 
# mutables (listas).
# =============================================================================
lista1 = [[2, 3], [9, 8]]  # Lista formada por elementos mutables.
copial1= copy.copy(lista1)  # Copiado superficial.
print('\nListas luego de la copia superficial'.upper())
print('Lista original:', lista1)
print('Copia:', copial1)

# Se modifica el primer elemento de la lista que es, a su vez, 
# el primer elemento de lista1. El valor 2 se reemplaza por el valor 25. 
lista1[0][0] = 25
tit2 = '''\nListas luego de la modificación de la lista original: 
    ambas listas reflejan el cambio'''.upper()
print(tit2)
print('Lista original:', lista1)
print('Copia:', copial1)

lista2 = [['verde', 'rojo'], ['blanco', 'azul']]  
copial2= copy.deepcopy(lista2)  # Copiado profundo.
print('\nListas luego de la copia profunda'.upper())
print('Lista original:', lista2)
print('Copia:', copial2)

# Se modifica el primer elemento de la lista que es, a su vez, el primer 
# elemento de lista2: el valor verde se reemplaza por el valor amarillo.
lista2[0][0] = 'amarillo'
tit3 = '''\nListas luego de la modificación de la lista original: 
    solo la original se afectó'''.upper()
print(tit3)
print('Lista original:', lista2)
print('Copia:', copial2)

# =============================================================================
# Copiado de listas por medio de partir o dividir listas (slice).
# Igual efecto que el copiado superficial.
# =============================================================================
lis1 = lista1[:]
print('\nListas luego del slice'.upper())
print('Lista original:', lista1)
print('Copia:', lis1)

lista1[0][0] = 92
print(tit2)
print('Lista original:', lista1)
print('Copia:', lis1)