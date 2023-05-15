lista1 = [5,6,8,7,1] #Se hizo la lista con los números
sum = 0 
for i in lista1: #Se toma cada número de la lista 
    sum += i #Se suman todo y se guarda en sum
prom = sum/len(lista1) #El total de la suma divido la cantidad de números en la lista
print("El promedia de la lista "+str(prom)) #Se imprime el promedio de la lista
