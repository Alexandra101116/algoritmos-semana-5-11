"""
Vamos a utilizar un ciclo infinito, pues no sabemos cuántas líneas de texto va a introducir 
el usuario. Además, debemos saber cuándo introdujo una línea en blanco para de esa forma salir
del ciclo usando break. Todas las líneas debemos guardarlas en una lista y convertirlas a mayúsculas.
"""
lineas = []
print ("Escriba algunas lineas. Deje en blanco para finalizar: ")
while True:
    s = input()
    if s:
        lineas.append(s.upper())
    else:
        break;

for refran in lineas:
    print (refran)
1
2
3
4
5
6
7
8
9
10
11
lineas = []
print ("Escriba algunas lineas. Deje en blanco para finalizar: ")
while True:
    s = input()
    if s:
        lineas.append(s.upper())
    else:
        break;
 
for refran in lineas:
    print (refran)