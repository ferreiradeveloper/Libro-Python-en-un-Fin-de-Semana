# las listas son colecciones ordenadas de datos y por tanto el orden en que se encuentran sus elementos es importante,
# la promera posición ocupada es la 0 (tipico en los vectores). La listas en python son mutables, tu type es list y se crean
# con corchetes y y sus elementos son separados por coma ([item1, item2....]).
# los elementos de las listas pueden ser de cualquier tipo
# Ejemplo:
nombre_lista = [1,'Francisco',True,21.10, ['a','b','c'], {'edad': 54, 'apellido': 'ferreira', 'casado': True}, (1,1,2,2,5,5)]

print(nombre_lista)
print(nombre_lista[4]) # este elemento es una lista
print(nombre_lista[-1]) # este elemento es una tupla
print(nombre_lista[-2]) # este elemento es un diccionario

# lsitas vacias
lista_vacia = []
lista_vacia2 = list()
print(lista_vacia,lista_vacia2)

# Se genera una lista a partir de un rango.
pares = list(range(0, 30, 2))
print('\nPares menores a 30:', pares)

impares = list(range(29, 0, -2))
print('\nImpares menores a 30:', impares)

# Se genera una lista con los caracteres de una cadena de caracteres.
caracteres = list('2020 es bisiesto')
print('\nLista de caracteres:', caracteres)

# Se genera una lista con subcadenas de una cadena de caracteres.
frase = '''La emigración no solo se hace para huir de la opresión en casa, 
sino también para llegar a lo más hondo de nuestra alma.'''  # Autor: Orhan Pamuk
palabras = frase.split()  # Si no se da parámetro, se toma el ' '.
print('\nLista de palabras:', palabras)

# Se genera una lista con los elementos de una tupla.
con_tuplas = list((6, 3, 8, 12, 15))
print('\nLista con los elementos de la tupla:', con_tuplas)

# operaciones con listas: 
# acceso a los elementos: se accede meniante su indice y esta como se comento con anterioridad en pieza en cero,
# y para acceder al ultimo elemento ademas de su incide podemos colocar [-1], python en uno de los pocos lenguajes
# que aceptan indices negativos
lista_colores = ['rojo','azul','verde','negro']
print(lista_colores[0])
print(lista_colores[-1])

# Operadores de sobre carga (Opradores+ y*)
# el efecto del primero (y) es concatenar o pegar los elementos de una lista al final de otra lista y el segundo (*) se usa para
# repetir la seguencia de elementos de la lista tantas veces como lo indique el valor que acompaña al operador

mas_colores= ['rosado','magenta']
colores_add = lista_colores+mas_colores
print(colores_add)
colores_add_por_2 = colores_add*2
print(colores_add_por_2)

