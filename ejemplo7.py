#Programa que introduzca dos numeros y devuelva cual de los dos es mayor, menor o son iguales

print("Hola")

valor1=int(input("Introduce el primer valor: "))
valor2=int(input("Introduce el segundo valor: "))


if valor1 < valor2:
    print(f"El número {valor2} es mayor que el número {valor1}")

if valor1 > valor2:
    print(f"El número {valor1} es mayor que el número {valor2}")

if valor1==valor2:
    print(f"Ambos números son iguales")