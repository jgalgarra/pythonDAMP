# Archivo: objetos_clases.py
# Autor: Javier Garcia Algarra 
# Fecha: 25 de enero de 2017
# Descripción: Mini introudccion OOP en Python


class Person:
    def __init__(self, name):
        self.name = name

    def saluda(self):
        print('Hola, me llamo', self.name)
        
    def cambia_nombre(self, nuevo_nombre):
        self.name = nuevo_nombre

p = Person('Pepe')
p.saluda()

# Cambiamos el atributo nombre
p.cambia_nombre('Juan')
print("Ahora me llamo",p.name)

print()
print("Ahora vamos a ver como crear listas de nombres")
#Podemos crear listas de nombres
chico = Person('Adán')
chica = Person('Eva')

lista_obj = [chico,chica]
print(lista_obj)

print(lista_obj[0].name,"y",lista_obj[1].name,"se encontraron en la calle y se miraron...")

dummy=input()

class Pareja:
    def __init__(self):
        self.el = ''
        self.ella = ''
        self.apellido = ''

    def flechazo(self,el,ella):
        self.el = el
        self.ella = ella
        print('Flechazo total entre', self.el, "y", self.ella)
        
    def matrimonio(self,apellido):
        self.apellido = apellido
        self.senyoresde = self.el+" y "+self.ella+" son ahora los "+apellido
        print(self.senyoresde)
        

par = Pareja()
par.flechazo(lista_obj[0].name,lista_obj[1].name)
par.matrimonio("Pérez")


