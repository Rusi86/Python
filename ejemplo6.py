# Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso

print("Hola")


peso=float(input("Introduce el peso en kg:"))
altura=float(input("Introduce tu altura en metros:"))
imc=peso/(altura**2)

if imc < 25:
    print(f"Si pesas {peso} kilos y mides {altura} ,tu IMC es: {round(imc, 2)} ")

else:
    print(f"Si pesas {peso} kilos y mides {altura} ,tu IMC es:, {round(imc, 2)} .Hay sobrepeso")




