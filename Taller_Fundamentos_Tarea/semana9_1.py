"""
Un profesor necesita sacar el promedio y la suma de las 5 notas de su alumno, 
diseña un algoritmo que promedie las 5 notas y las sume.

"""

#declaracion de variables
suma =0.0
notas=0.0

#entrada 
for i in range(5):
    notas =float (input("Ingrese la nota: "))
    suma = suma + notas
    promedio= suma/5
#Proceso

#salida
print ("la suma es: ", suma)
print ("el promediomes : ", promedio)