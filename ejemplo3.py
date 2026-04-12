# programa que calcule dos numeros operando con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tnga dos decimales?

print("hola")

valor1=int(input("Introduce un valor:"))
valor2=int(input("Introduce otro valor:"))


print("Suma")
total1=valor1 + valor2
print(f"La suma de {valor1} y {valor2} es:", total1)


print("Resta")
total2=valor1 - valor2
print(f"La resta de {valor1} y {valor2} es:", total2)


print("Multiplicación")
total3=valor1 * valor2
print(f"La multiplicación de {valor1} y {valor2} es:", total3)


print("División")
total4=valor1 / valor2
print(f"La división de {valor1} y {valor2} es:", round(total4, 2))


print("Potencia")
total5=valor1 ** valor2
print(f"El exponente de {valor1} y {valor2} es:", total5)


print("División entera")
total6=valor1 // valor2
print(f"La división entera de {valor1} y {valor2} es:", total6)