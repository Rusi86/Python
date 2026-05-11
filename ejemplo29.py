#Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i.Presenta por pantalla los siguientes resultados

longitud=0
listanumeros=[]
listaletras=[]
listamayuscula=[]


lista1=["a","b","D","x","r","X","3","h","w","2","i"]

longitud=len(lista1)

print(f"Número de valores: {longitud}")

for i in lista1:
    if i.isnumeric():
        listanumeros.append(int(i))
    else:
        listaletras.append(i)

print(f"Cantidad de números: {len(listanumeros)}")
print(f"Cantidad de letras: {len(listaletras)}")


for x in lista1:
    if x.isupper():
        listamayuscula.append(x)

print(f"Cantidad de mayúsculas: {len(listamayuscula)}")

print(f"Suma total de números : {sum(listanumeros)}")
