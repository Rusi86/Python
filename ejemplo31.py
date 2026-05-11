#Modifica el programa anterior para que sea el usuario quien adivine la palabra escogida al azar de la lista, indicando si es correcto o no. El programa no finaliza hasta adivinar la palabra.

import random

lista1=["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]

eleccion=random.choice(lista1)
intentos=0

print("Estoy pensando una palabra al azar, a ver si la adivinas")

while True:
    intento=input("Introduce la palabra secreta: ")
    intentos+=1

    if intento==eleccion:
        print("ACERTASTE")

    else:
        print("SIGUE JUGANDO")

