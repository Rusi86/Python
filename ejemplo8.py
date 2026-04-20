# A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclado números entre 0 y 10


print("Hola")

valor1=int(input("Introduce el primer valor: "))
valor2=int(input("Introduce el segundo valor: "))

if valor1<= 10:
    if valor2>= 0:
        if valor1 < valor2:
            print(f"El número {valor2} es mayor que el número {valor1}")

        elif valor1 > valor2:
            print(f"El número {valor1} es mayor que el número {valor2}")

        elif valor1==valor2:
            print(f"Ambos números son iguales")

else:
    print("Uno o los dos números están fuera de los límites establecidos")