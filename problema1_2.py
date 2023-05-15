'''
    escriba una funcion que reciba una cadena de caracteres (nom,bre de un fichero) y que forme
    y regrese una lista en la cual cada elemento sera una kinea del fichero.  
'''

def carga_lista(nombre_fichero):
    try:
        resultado = []
        with open(nombre_fichero,'r') as fichero:
            for dato in fichero:
                resultado.append(dato.strip()) # quita el salto de línea.
            return resultado
    except FileNotFoundError:
        raise FileNotFoundError('No se pudo abrir el Fichero'.upper())
    
# Testeos de la función
# CP1: fichero con datos
lista1 = carga_lista('escritores')
print('nCP1:',lista1)
print('------------------------------')
# CP1: fichero con datos
lista2 = carga_lista('pintores')
print('nCP2:',lista2)
print('------------------------------')

# CP3: fichero no existente
try:
    lista3 = carga_lista('manicuristas')
    print('nCP3:',lista3)
except Exception as error:
    print('CP3:', error)
print('------------------------------')
