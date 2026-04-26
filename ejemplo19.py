# Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que si a<b la secuencia será incremental y si a>b la secuancia será en descenso. Respeta el foamto de salida


print("Hola")


intervalo1=int(input("Introduce el primer intervalo: "))
intervalo2=int(input("Introduce el segundo intervalo: "))
resultado=""

if intervalo1 < intervalo2:
    for x in range(intervalo1, intervalo2 + 1):
        resultado=resultado + str(x) + "-"

else:
    for x in range(intervalo1, intervalo2 -1, -1):
        resultado=resultado + str(x) + "-"

print(resultado[:-1])
