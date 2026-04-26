#A partir del código anterior, haz que aparezca al finalizar el programa por pamtalla el total de las sumas y el número de repeticiones. Con While.


print("Hola")

total=0
totalsuma=0
contador=0

continuar=input("Quieres introducir valores para empezar a sumar? s/n: ")
while continuar=="s":

    valor1=int(input("Introduce el primer valor: "))
    valor2=int(input("Introduce el segundo valor: "))
    total=valor1+valor2
    print(f"El resultado de la suma es: {total}")
    continuar=input("Deseas repetir la operación? s/n:")
    totalsuma+=total
    contador+=1

print("Resumen:")
print("la suma total es: ", totalsuma ,"y el número de repeticiones es: ", contador)
