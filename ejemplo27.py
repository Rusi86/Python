# Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menos a mayor.

numero=[]

i=int(input("Introduce un número de vueltas: "))

for vuelta in range (0,i):
    intro=int(input("Introducir un número: "))
    numero.append(intro)
    numero.sort()

print(numero)

