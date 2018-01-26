# Archivo: web_scrap.py
# Autor: Javier Garcia Algarra 
# Fecha: 26 de enero de 2018
# Descripción: Ejemplo de web scrapping, leyendo la página del servidor simple

import requests

source = 'http://localhost:8000'

r = requests.get(source)

for line in r:
    print (line.strip())

print('\nDisplay all headers\n')
print(r.headers)

dummy = input()