# Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif

print("Hola")


operador1=input("Introduce una : ")



if operador1.islower():
    print(f"La letra es minúscula")

elif operador1.isupper():
    print(f"La letra es mayúscula")

elif operador1.isnumeric():
    print(f"El valor introducido es un número")
    
else:
   print("El valor introducido es un símbolo")
