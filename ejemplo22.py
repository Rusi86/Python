# Realiza un programa que sume dos números enteros por teclado y prersente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While.


print("Hola")

total=0

continuar=input("Quieres introducir valores para empezar a sumar? s/n: ")
while continuar=="s":

    valor1=int(input("Introduce el primer valor: "))
    valor2=int(input("Introduce el segundo valor: "))
    total=valor1+valor2
    print(f"El resultado de la suma es: {total}")
    continuar=input("Deseas repetir la operación? s/n:")

print("Programa finalizado")