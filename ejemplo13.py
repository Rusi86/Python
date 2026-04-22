# Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif

print("Hola")


operador1=input("Introduce una frase: ")
longitud=len(operador1)


if longitud<11:
    print("La frase tiene menos de 11 caracteres")

elif longitud==11:
    print("La frase tiene 11 caracteres")

else:
    print("La frase tiene 11 o mas caracteres")