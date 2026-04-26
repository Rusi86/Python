# Diseña un programa que "piense" un número aleatorio entre 0 y 1000 para que pida que intentemos adivinarlo. En cada intento, el prgrama nos dirá si el número introducido es mayor o menos del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos

print("Hola")


import random

numerosecreto=random.randint(0, 1000)
intentos=0

print("Estoy pensando un número aleatorio, a ver si lo adivinas")

while True:
    intento=int(input("Introduce un valor comprendido entre 0 y 1000: "))
    intentos+=1

    if intento < numerosecreto:
        print("El número que has introducido es menor")
    
    elif intento > numerosecreto:
        print("El número que has introducido es mayor")

    else:
        print(f"Acertaste, has realizado {intentos} intentos")
