lista=[]
palabra=input("Ingrese una palabra en la lista : ")
while palabra!= "":
    lista.append(palabra)
    palabra=str(input("ingresar palabra (Enter para finalizar):"))
if lista:
    palabra=max(lista, key=len)
print(len(palabra))

  
 

