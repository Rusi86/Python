# Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra

print("Hola")

palabra=input("Introduce una palabra: ")



for indice, letra in enumerate (palabra):
    
    print(f"En la posición {indice} esta la {letra}")