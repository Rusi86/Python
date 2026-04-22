# Crea un programa que cuente todos los números hasta el número 50


contador = 0

for numero in range(0, 50):
    if numero % 2 == 0:
        contador += 1

print("El total de pares es:", contador , "El total de impares es:", contador)