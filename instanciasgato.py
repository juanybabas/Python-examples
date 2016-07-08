# -*- coding: utf-8 -*-
"""La programación orientada a objetos es un paradigma
el cual propone modelar todo en base a clases y a objetos.
Este paradigma consiste en el uso de los conceptos de  herencia,
cohesión, abstracción, polimorfismo, acoplamiento y encapsulamiento."""

class Gato:
    def __init__(self, energia, hambre):
        self.energia = energia
        self.hambre = hambre
        print ('Se creo un gato')

    def tomar_leche(self, leche_en_litros):
        self.hambre += leche_en_litros
        print ('el gato toma su leche ñam ñam')

    def acariciar(self):
        print ('prrrrr...')

    def jugar(self):
        if self.energia <= 0 or self.hambre <= 1:
            print ('el gato no quiero jugar')
        else:
            self.energia -= 1
            self.hambre -= 2
            print ('al gato le encanta jugar')

    def dormir(self, horas):
        self.energia += horas
        print ('el gato tomo una siesta')


gato = Gato(1, 1)
gato.acariciar()
gato.jugar()
gato.jugar()
gato.jugar()
gato.jugar()
gato.jugar()
gato.jugar()
gato.acariciar()
gato.acariciar()
gato.acariciar()
gato.acariciar()
gato.acariciar()
gato.tomar_leche(4)
gato.jugar()
gato.dormir(1)



"""La herencia es uno de los tres conceptos básicos que tiene todo lenguaje orientado a objetos.
La herencia consiste en que una clase pueda heredar de otra clase, en otras palabras la clase puede ser extendida.
Siguiendo con nuestro ejemplo de gatos,
la clase Gato podría heredar de una clase Felino.
"""

class Felino:
    def __init__(self):
        print ('se creo el felino')

    def rugido(self):
        print ('El felino dio un rugido')


class Gato(Felino):
    def __init__(self, energia, hambre):
        self.energia = energia
        self.hambre = hambre
        print ('Se creo un gato')

    def tomar_leche(self, leche_en_litros):
        self.hambre += leche_en_litros
        print ('el gato toma su leche')

    def acariciar(self):
        print ('prrrrr...')

    def jugar(self):
        if self.energia <= 0 or self.hambre <= 1:
            print ('el gato no quiero jugar')
        else:
            self.energia -= 1
            self.hambre -= 2
            print ('al gato le encanta jugar')

    def dormir(self, horas):
        self.energia += horas
        print ('el gato tomo una siesta')

gato = Gato(3, 3)
gato.rugido()
"""Además en python tenemos algo llamado herencia múltiple.
Es decir nuestra clase puede heredar de varias clases.
Por ejemplo nuestro Gato puede heredar de Felino y Mascota"""

class Mascota:
        def __init__(self):
            print ('se creo la mascota')
        def sientate(self):
            print ('La mascota se sentó')
class Felino:
        def __init__(self):
            print ('se creo el felino')
        def rugido(self):
            print ('El felino dio un rugido')
class Gato(Felino, Mascota):
    def __init__(self, energia, hambre):
            self.energia = energia
            self.hambre = hambre
            print ('Se creo un gato')
    def tomar_leche(self, leche_en_litros):
            self.hambre += leche_en_litros
            print ('el gato toma su leche')
    def acariciar(self):
            print ('prrrrr...')
    def jugar(self):
            if self.energia <= 0 or self.hambre <= 1:
                print ('el gato no quiero jugar')
            else:
                self.energia -= 1
                self.hambre -= 2
                print ('al gato le encanta jugar')
    def dormir(self, horas):
                self.energia += horas
                print ('el gato tomo una siesta')
gato = Gato(3,3)
gato.sientate()

"""Polimorfismo
palabra polimorfismo viene del griego y significa varias formas.
La teoría indica que se trata de la habilidad
de responder a una misma función de manera distinta.
Haremos un ejemplo con una clase Gato y una clase Perro. """

class Gato:
    def ruge(self):
        print('El gato maulla')
class Perro:
    def ruge(self):
        print ('El perro ladra')
def rugir(animal):
    animal.ruge()


gato = Gato()
perro = Perro()

rugir(gato)
# 'El gato maulla'

rugir(perro)
# 'El perro ladra'

"""Encapsulación
Lo que hace el encapsulamiento
es impedir la visualización o acceso de las variables de manera directa.
En otros lenguajes esto se logra al momento de declarar la variable como public y private
sin embargo en python es algo distinto.
Para declarar una variable o función como privada,
el nombre de la función o variable a ser declarado debe comenzar con doble guion abajo.
Esto bastará para que lo declarado sea reconocido como privado. """


class ClaseOtroEjemplo:
    def __init__(self):
        self.publico = ('variable publica')
        self.__privado = ('variable privada')
    def obtener_privado(self):
        print  (self.__privado)


otro_ejemplo = ClaseOtroEjemplo()

print (otro_ejemplo.publico)
# 'variable publica'

otro_ejemplo.obtener_privado()
# variable privada