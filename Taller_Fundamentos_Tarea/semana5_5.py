"""
Una institución social ha recibido una donación en dinero que lo 
repartirá entre cinco áreas. Cada área recibirá una parte de la donación 
equivalente a: 
- Centro de salud: 25% de la donación. 
- Comedor infantil: 45% del monto recibido por la escuela infantil. 
- Escuela infantil: 35% de la donación. 
- Posta médica: 40% del monto recibido por el centro de salud.
- Asilo de ancianos: lo que queda de la donación. 
Dado el importe de la donación, diseñe un algoritmo que determine qué 
cantidad de dinero le corresponde a cada área.
"""
#declaracion de variables
donacion = 0.0
cs = 0.0
ei = 0.0
ci = 0.0
pm = 0.0
aa = 0.0

#entrada
donacion = float (input ("ingrese la donación: "))

#proceso
cs = 25/100*donacion
ei = 35/100*donacion
ci = 45/100*ei
pm = 40/100*cs
aa = donacion-cs-ei-ci-pm

#salida
print ("Donación para centro de salud: ", cs )
print ("Donación para escuela infantil : ", ei )
print ("Donación para comedor infantil : ", ci )
print ("Donación para posta médica : ", pm )
print ("Donación para acilo de ancianos: ",aa )
