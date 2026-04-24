# Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes.

print("Hola")

texto=input("Introduce una palabra: ")
vocales="aeiouAEIOUáéíóúÁÉÍÓÚ"
vocales_encontradas=[]
consonantes_encontradas=[]


for letra in texto:
    if letra.isalpha():
        if letra in vocales:
            vocales_encontradas.append(letra)
            
        else:
            consonantes_encontradas.append(letra)


print(f"Las vocales de la palabra {texto} son: ", "".join(vocales_encontradas))
print(f"Las consonantes de la palabra {texto} son: ", "".join(consonantes_encontradas))  