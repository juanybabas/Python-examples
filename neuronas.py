import random


class neurona(object):
    def __init__(self, cantidadEntradas=0, factorAprendizaje=0):
        self.factorAprendizaje = factorAprendizaje
        self.cantidadEntradas = cantidadEntradas

    def inicializaPesos(self):
        pesos = []
        for x in range(self.cantidadEntradas):
            pesos.append(random.uniform(0, 1))
        pesos.append(random.uniform(0, 1))
        print "Pesos Iniciales:\n", pesos
        self.obtenerEntradas(pesos)

    def obtenerEntradas(self, pesos):
        entradas = []
        salida = 0

        while True:
            opcion = raw_input("Desea continuar si o no: ")
            if opcion == "no":
                break
            print "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            for x in range(self.cantidadEntradas):
                entradas.append(int(raw_input("Ingrese la entrada: ")))
            entradas.append(-1)
            salidaDeseada = int(raw_input("Ingresa la salida deseada: "))
            sumatoria = self.funcionActivacion(entradas, pesos)
            if sumatoria >= 0:
                salida = 1
            elif sumatoria < 0:
                salida = -1
            if salidaDeseada - salida != 0:
                print "Salida Obtenida: ", salida
                print "Pesos Nuevos:\n"
                for i, x in enumerate(pesos):
                    pesos[i] = pesos[i] + (2.0 * self.factorAprendizaje) * (salidaDeseada * entradas[i])
                print pesos
                self.obtenerEntradas(pesos)
            else:
                print "Salida Obtenida: ", salida
                entradas = []

    def funcionActivacion(self, entradas, pesos):
        sumatoria = 0
        for i, entrada in enumerate(entradas):
            sumatoria = sumatoria + (entradas[i] * pesos[i])
        return sumatoria


def main():
    factorAprendizaje = raw_input("Ingresa el factor de aprendizaje: ")
    cantidadEntradas = raw_input("Cuantas seran las entradas: ")
    neurona1 = neurona(int(cantidadEntradas), float(factorAprendizaje))
    pesos = neurona1.inicializaPesos()


main()