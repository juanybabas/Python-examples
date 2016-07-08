#-*-coding: utf8-*-
import os


def Cabecera():
    print ("************************************")
    print ("Calculadora")
    print ("************************************")
    print ("1) Suma")
    print ("2) Resta")
    print ("3) Multiplicacion")
    print ("4) Division")
    print ("5) Salir")
    return int(input("Selecione Opcion -> "))


def Calculadora():
    os.system('cls')
    opcion = Cabecera()

    while (opcion > 0 and opcion < 5):

        numero1 = int(input("Ingrese Primer Numero -> "))
        numero2 = int(input("Ingrese Segundo Numero -> "))

        if (opcion == 1):
            os.system('cls')
            print ("************************************")
            print ("El resultado de su operacion")
            print ("************************************")
            print ("La Suma de " + str(numero1) + " y " + str(numero2) + " es:", numero1 + numero2)
            opcion = Cabecera()

        elif (opcion == 2):
            os.system('cls')
            print ("************************************")
            print ("El resultado de su operacion")
            print ("************************************")
            print ("La Resta de " + str(numero1) + " y " + str(numero2) + " es:", numero1 - numero2)
            opcion = Cabecera()

        elif (opcion == 3):
            os.system('cls')
            print ("************************************")
            print ("El resultado de su operacion")
            print ("************************************")
            print ("La Multiplicacion de " + str(numero1) + " y " + str(numero2) + " es:", numero1 * numero2)
            opcion = Cabecera()

        elif (opcion == 4):
            os.system('cls')
            print ("************************************")
            print ("El resultado de su operacion")
            print ("************************************")
            print ("La Division de " + str(numero1) + " y " + str(numero2) + " es:", numero1 / numero2)
            opcion = Cabecera()


Calculadora()