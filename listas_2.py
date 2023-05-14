# Funciones asociadas a las listas
''''
Funciones para el manejo de listas
lista.append(elemento): --> agrega elementos al final de la fila
lista.count(elemento): --> regresa el número de veces que eel elemento se encueltra en la lista
len(lista): --> regresa el total de elementos en la lista
lista.insert(index,value): --> Agrega en la posición indicada por el índice el nuevo valor,
                               desplazando los demás elementos hacia la derecha. Si el índice
                               es mayor que el tamaño de la lista entonces lo agrega al final
lista.extend(otra_lista): --> Agrega al final de la lista todos los elementos de la otra lista.
lista.remove(elemento): --> Quita el elemento de la lista, Si este no esta lanza la Excepción:
                            ValueError: list.remove(x): x not in list
lista.index(elemento): --> Regresa la posición del elemento dentro de la lista (0 <= posición <= longitud -1)
lista.index(elemento, inicio, fin): --> Busca el elelemento desde la posición de inicio a la pocisión fin.
                                        Si el elemento no está lanza la excepción: ValueError: XXX is not in list.
lista.sort(): --> Ordena los elementos de la lista en orden creciente (el primero es el más grande)
lista.sort(key=funcion): --> Ordena los elementos de la lista en orden creciente (el primero es el más grande)
lista.sort(reverse = True): --> Ordena la lista de mayor a menor
lista.sorted: --> ordena de manera temporal la lista, pero no afecta a la lista original
lista.clear() --> Quita todos los elementos de la lista, dejandola vacia.
lista.pop(n) --> Quita y regresa el elemento a pa sosición n.
                 de no especificarse n quita y regresa el ultimo elemento.
                 Si n está fuera del rango de la lista, lanza la excepción IndexError: pop index out of range.
                 Si no de da n y la lista está vacía lanza la excepción IndexError: pop from empty list.
del lista(n) --> Elimina de la lista el elemento de la posición n.
                 Si n está fuera del rango de la lista, lanza la excepción: IndexError: list assignment index out of range.
del lista --> Elimina la lista completa.
'''
"""
Funciones predefinidas para trabajar con  listas.
Ejemplos de uso.
""" 
dias_laborables = ["lunes", "martes", "miércoles", "jueves", "viernes"]
colores_primarios = ['rojo', 'verde', 'azul']
precios = [205.30, 107.18, 25, 450, 310.89, 170.23, 340]
pares = list(range(0, 30, 2))
impares = list(range(29, 0, -2))
colores_repetidos = colores_primarios * 2 

# =============================================================================
# Algunas funciones para el manejo de listas.
# =============================================================================
dias_laborables.append('sábado')  # Agrega sábado al final de la lista.
print('\nSemana laborable con un día extra =', dias_laborables)
# Cuenta el número de veces que aparece lunes en la lista. 
print(f"\nEl lunes aparece = {dias_laborables.count('lunes')} vez (veces).")
# Regresa el total de elementos que tiene la lista.
print('Total de precios =', len(precios))
# Agrega en la primera posición el valor blanco.
colores_primarios.insert(0, 'blanco')  
print('\nLista con un nuevo elemento:', colores_primarios)
# No existe la posición 10. Lo inserta al final.
colores_primarios.insert(10, 'amarillo')  
print('Lista con un nuevo elemento:', colores_primarios)
# Agrega al final de la lista todos los elementos de la lista impares.
pares.extend(impares)  
print('\nLista de pares extendida con la lista impares:', pares)
# Quita el valor sábado de la lista.
dias_laborables.remove('sábado')
print('\nVolviendo a la normalidad =', dias_laborables)
# Regresa la posición de rojo dentro de la lista.
print('\nPosición del rojo:', colores_primarios.index('rojo'))
print('Posición del segundo azul:', colores_repetidos.index('azul', 3))
# Da el error: ValueError: 'gris' is not in list
# print('Posición del gris:', colores_repetidos.index('gris'))  
# Ordena los elementos de la lista de menor a mayor.
precios.sort()
print('\nPrecios ordenados de menor a mayor:', precios)
# Ordena los elementos de la lista de mayor a menor.
colores_repetidos.sort(reverse = True)
print('Colores ordenados de mayor a menor:', colores_repetidos)
# Genera una nueva lista ordenada, sin alterar la lista original.
lista_ordenada = sorted(dias_laborables)
lis_ord_long = sorted(dias_laborables, key = len)
print('\nDías laborables sin alterar:', dias_laborables)
print('Días laborables ordenados:', lista_ordenada)
print('Días laborables ordenados por longitud:', lis_ord_long)
# Invierte el orden de los elementos de la lista.
impares.reverse()
print('\nImpares en orden inverso:', impares)
# Quita y regresa el elemento de la posición 0.
quitado = colores_primarios.pop(0)
print('\nEl elemento quitado es:', quitado)
print('La lista quedó:', colores_primarios)
rescatado = dias_laborables.pop()  # Sin posición: quita el último.
print('Se rescató para el fin de semana:', rescatado)
print('Los días laborables quedaron:', dias_laborables)
# print(precios.pop(10))  # IndexError: pop index out of range
# Quita todos los elementos de la lista, dejándola vacía.
precios.clear()
print('\nLa lista de precios quedó vacía:', precios)
# print(precios.pop())  IndexError: pop from empty list
# Quita el segundo elemento de la lista.
del colores_primarios[1]
print('\nColores primarios luego de quitar el segundo elemento:', colores_primarios)

'''
    Según se muestra en el ejemplo anterior tanto sort() como sorted() permiten un parámetro extra (key), utilizado para indicar
    el criterio de ordenación, En el ejemplo se usó para señalar que los días se ordenen según su longitud, no alfabeticamente.
    Si una lista almacena datos númericos y cadenas de caracteres y se debe ordenar, con este parámetro se puede pedir que todos 
    los datos se conviertan a cadenas (key = str) y luego se ordenen. Es importante señalar que los datos de la lista original no
    se modifican, la alteración es solo para efectos de la ordenación. En el caso de listas con cadenas en mayúsculas y otras
    en minúsculas se podriá usar key = str.lower para lograr una ordenación más uniforme.
'''

