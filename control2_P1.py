mayor=[]
menor=[]
lista=[]
for x in range(15):
   puntaje=int(input("ingrese puntaje diario del alumno (de 1 a 100) :"))
   if puntaje>=60:
    mayor.append(x)
   else:
        menor.append(x)
print(mayor)
print(menor)


