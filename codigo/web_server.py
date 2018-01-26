# Archivo: web_server.py
# Autor: Javier Garcia Algarra 
# Fecha: 26 de enero de 2018
# Descripción: Ejemplo de web server. Conectándose con
#              navegador a localhost:8000 mostrará todos
#              los ficheros del directorio de código
#              Buen ejemplo de potencia de Pyhton, pésimo de seguridad

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor levantado en el puerto", PORT)
    httpd.serve_forever()
    
dummy = input()