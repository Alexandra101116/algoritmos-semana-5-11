"""
Diseña un algoritmo que determine el Área (A) y el Perimetro (P) de un rectangulo 
del que se conoce su base (b) y su altura (h). Considera las siguientes formulas:
A = b x h
P = 2 x (b + h)
"""
#Declaracion de variables
b = 0.0
h = 0.0
A = 0.0
P = 0.0

#Entrada
b = float (input ("ingrese la base: "))
h = float (input ("ingrese la altura: "))

#Proceso
A = b * h
P = 2 * (b + h)

#Salida
print (f"El área del rectangulo es {A} y el perimetro es {P}")
