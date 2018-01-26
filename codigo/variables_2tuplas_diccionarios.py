# Archivo: variables_2tuplas_diccionarios.py
# Autor: Javier Garcia Algarra 
# Fecha: 25 de enero de 2018
# Descripción: Manejo de listas


# Diccionarios

print("Un diccionario es una lista con clave valor")
dict_a  = {
		"iphone" : 2007,
		"iphone 3G" : 2008,
		"iphone 3GS" : 2009,
		"iphone 4" : 2010,
		"iphone 4S" : 2011,
		"iphone 5" : 2012
	}
print("Contenido del diccionario dict_a")
print(dict_a)

print("Podemos referirnos a un campo concreto del diccionario usando la clave")
print("Contenido de dict_a['iphone 4']:",dict_a["iphone 4"])
print("Contenido de dict_a['iphone 3G']:",dict_a["iphone 4"])

dummy = input()

# Una tupla es una lista inmodificable
print("Una tupla es una lista que no puede modificarse")
tupla_a = ("hola","mundo","hasta","luego")

# Si imprimimos la lista por la pantalla aparecerán los elementos individuales
print(tupla_a)

print("La tupla tiene",len(tupla_a),"elementos")

# Los elementos de la tupla se direccionan igual que los de una lista
print("El primer elemento de la tupla es",tupla_a[0])
print("El último elemento es",tupla_a[len(tupla_a)-1])

# Podemos agregar elementos al final de una lista con el método append. Es muy
# sencillo
print("Si intentamos modificar el contenido tenemos un problema")
otro_elemento = input("Escribe el valor de un nuevo elemento para la tupla: ")
tupla_a.append(otro_elemento)
