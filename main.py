# -*- coding: cp1252 -*-
# Lenguajes de Programaci�n
# Grupo 3
# Programa 4
# Hecho por: 
# Nava Luj�n Francisco Jos�
# Real Badillo Sandra Ang�lica
# Zintzun Garc�a Jonatan Salvador
# De San Pedro Vazquez Luis Daniel

# Programa que, dado un n�mero en base 10 con punto decimal,
# obtiene su representaci�n en punto flotante de simple pre-
# cisi�n y viceversa

import math
import os
import sys

sisOperativo = sys.platform
clear = ""

if sisOperativo == "darwin" or sisOperativo == "linux2":
	clear = lambda : os.system("clear")
else:
	clear = lambda : os.system("cls")

# Funci�n que convierte un n�mero decimal a binario
def conversor_a_binario(numero):
    resultado = []
    while numero != 0:
        resultado.append(numero % 2)
        numero = numero / 2
    return list(reversed(resultado))

# Funci�n que convierte un n�mero binario a decimal
def conversor_a_decimal(numero):
    decimal = 0
    exponente = 1
    numero = list(reversed(numero))
    for i in numero:
        if int(i) == 1:
            decimal += exponente
        exponente *= 2
    return decimal

# Funcion que se encarga de agregar bits al arreglo
def agrega(numBin,numBits):
    diferencia = numBits - len(numBin)
    for i in range(0,diferencia):
        numBin.insert(0,0)
    return numBin

# Funci�n que determina si un n�mero es binario
def verificar_numero_binario(numBin):
    for i in numBin:
        if int(i) != 1:
            if int(i) != 0:
                return False
    return True

# Funci�n que obtiene la representaci�n en punto flotante de simple
# precisi�n de un n�mero decimal
def flotar():
    flotante = []
    entrada = float(raw_input("N�mero: "))
    if entrada < 0:
        flotante.insert(0,1)
        entrada *= -1
    else:
        flotante.insert(0,0)
    decimal,numero=math.modf(entrada)
    numero = conversor_a_binario(int(numero))
    if numero != 0:
        indice = conversor_a_binario((len(numero)-1)+127)
    else:
        indice = conversor_a_binario(127)
    indice = agrega(indice,8)
    for x in range(0, 8):
        flotante.insert(x+1,indice[x])
    for y in range(1,len(numero)):
        flotante.insert(y+9,numero[y])
    flotante.extend(mantisa(decimal))
    while(len(flotante)<32):
        flotante.append(0)
    print("El n�mero en punto flotante es: ")
    for z in range(0,32):
        sys.stdout.write(flotante[z])

# Funci�n que obtiene la representaci�n en decimal de un punto flotante
# de simple precisi�n
def aterrizar():
    entrada = list(raw_input("N�mero: "))
    if not(verificar_numero_binario(entrada)):
        print("ERROR: No es un n�mero binario"),
        return
    if len(entrada) < 32:
        print("ERROR: Faltan d�gitos"),
        return
    exponente = []
    for x in range(0, 8):
        exponente.insert(x,entrada[x+1])
    expDecimal = conversor_a_decimal(exponente) - 127
    respFinal = pow(2,expDecimal)
    expDecimal = expDecimal - 1
    for y in range(0, 23):
        respFinal += (float(entrada[9+y])*(pow(2,(expDecimal-y))))
    if int(entrada[0]) == 0:
        print(respFinal),
    elif int(entrada[0]) == 1:
        print(-respFinal),

# Algoritmo que devuelve la parte fraccionaria de un n�mero en su represen-
# taci�n binaria
def mantisa(numero):
    resultado = []
    while math.floor(numero) != numero:
        numero *= 2
        if numero >= 1:
            resultado.append(1)
            numero -= 1
        else:
            resultado.append(0)
    return list(resultado)

def main():
    # try:
    while 1:
        clear()
        opcion = int(raw_input("1.- Decimal a flotante\n2.- Flotante a decimal\n3.-Salir\nOpcion: "))
        if opcion == 1:
            flotar()
        elif opcion == 2:
            aterrizar()
        elif opcion == 3:
            print("Fin de la ejecuci�n :D")
            exit()
        else:
            print("Opci�n no reconocida.")
        raw_input("\n\nPresione enter para continuar.")
        
if __name__ == '__main__':
    main()
