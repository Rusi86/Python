# Modifica el programa anterior y haz que se repita el ciclo automaticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural. Con While


print("Hola")

total=0
totalsuma=0
contador=0

continuar=input("Quieres introducir valores para empezar a sumar? s/n: ")
while continuar=="s":

    valor1=int(input("Introduce el primer valor: "))
    valor2=int(input("Introduce el segundo valor: "))
    total=valor1+valor2
    totalsuma+=total
    contador+=1
    print(f"El resultado de la suma es: {total}")
    print(f"El total acumulado es: {totalsuma} y llevas {contador} {"operacion realizada" if contador==1 else "operaciones realizadas"}" )
    if totalsuma>=50:
        break

print("Fin del programa")
