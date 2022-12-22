"""
Una persona necesita sacar la acumulación de los ahorros que tuvo,
diseñe un algoritmo que acumule los ahorros ingresados y que 
digite cuantos se ingresaron.

"""

#declaracion de variables
acu = 0.0
ahorros = 0.0
cont = 0

#entrada

#proceso
cantidad= int (input("Escriba los ahorros que desee ingresar"))
for i in range (cantidad):
    ahorros = float (input ("Ingresa el ahorro: "))
    acu = acu + ahorros
    cont = cont + 1
#salida
print ("La acumulacion de ahorro es de: ", acu)
print ("Contador de ahorros: ", cont )
