"""
Un profesor necesita sacar el promedio de las 3 notas de su alumno, 
diseña un algoritmo que promedie las 3 notas.
Para sacar el promedio se aplica la formula:
nota_1 + nota_2 + nota_3 / 3
"""

#declaracion de variables
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
promedio = 0.0
#entrada
print ("Es momento de que ingrese las 3 notas")

nota1 = float (input ("Ingrese la primera nota: "))
nota2= float (input("Ingrese la segunda nota: "))
nota3= float (input("Ingrese la tercera nota: "))

#proceso
promedio = nota1 + nota2 + nota3
promedio = promedio / 3
#salida
print ("su promedio es de: ", promedio)