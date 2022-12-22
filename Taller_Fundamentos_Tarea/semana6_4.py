"""
Diseñe un algoritmo en el que una persona pueda saber 
en que etapa de desarrollo se encuentra según su edad
"""
#declaración de variables
edad = 0

#entrada
edad = float (input ("Ingrese la edad: "))

#proceso
if 5 >= edad:
    print ("Usted se encuentra en la infancia!")
elif 11>= edad:
    print ("Usted se encuentra en la niñez!")
elif 17 >= edad:
    print ("Usted se encuentra en la adolescencia")
elif 24 >= edad:
    print ("Usted se encuentra en la juventud")
elif 60 >= edad:
    print ("Usted se encuentra en la adultez")
elif 94 >= edad:
    print ("usted se encuentra en la vejez")
else:
    print ("Sigues vivo???")

#salida