"""
Diseña un algoritmo en el que se ingrese 2 digitos para sumarlos
y el programa los contabilice y los acumule usando el while.
"""
#declaracion de variables
acu = 0 
cont = 0

#entrada
#proceso
rpt = "si"
while (rpt != "no"):
    num1 = int (input ("ingrese el primer digito: "))
    num2 = int (input ("ingrese el segundo digito: "))
    acu = acu + num1 + num2
    cont = cont + 2
    suma = num1 + num2
    print ("la suma es: ", suma)
    print ("la acumulacion: ", acu)
    print ("contador: ",cont)

    rpt = str (input ("desea realizar otra suma? si/no: "))

#salida
