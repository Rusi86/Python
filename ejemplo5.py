#Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso (raíz y división)

import math

print("Hola")

valor=int(input("Introduce un valor:"))

total1=math.sqrt(valor)
total2= total1 // 2

print(f"El resultado de la raíz es:", round(total1, 1))

print(f"El resultado de la división es:", total2)
