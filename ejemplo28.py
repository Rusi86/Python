#Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.


letras=[]

continuar=input("Quieres introducir una serie de letras? s/n: ")
while continuar=="s":
    letra=input("Introduce una letra: ")

    if not letra.isalpha():
        continue

    letras.append(letra)
    continuar=input("¿Deseas repetir? s/n: ")
    

print(letras)


