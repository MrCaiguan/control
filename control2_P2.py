lista=[]
for x in range(7):
    nombres=input(" ingrese un nombre a la lista: ")
    lista.append=(nombres)
lista_2=[]
for nombre in lista:
    if nombre.endswith("a"):
        lista_2.append(nombre)

print("la lista es :",lista_2)