# Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF's que establezcan True o False a la condición


print("Hola")


operador1=input("Introduce una letra: ")



if operador1.islower():
    print(f"La letra es minúscula")

elif operador1.isupper():
    print(f"La letra es mayúscula")

elif operador1.isnumeric():
    print(f"El valor introducido es un número")
    
else :
   print("La letra es mayúscula ¿?")



