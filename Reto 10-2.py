def productoPunto(lista1:list,lista2:list)->int: #Se declara la función 
    o = 0
    for i in range(len(lista1)): # i va a tomar los valores del 0 a la longitud de la lista
        o += lista1[i]*lista2[i] #Se multiplica los mismos indices de ambas listas y se guardan en o
    return o #Devuelve o

if __name__=="__main__":
    a = int(input("Ingrese la cantidad de números que quiere ingresar a las listas: ")) #Cantidad de números en las listas
    #Listas vacias
    lista1 = [] 
    lista2 = []
    #Se pregunta según en indice que número quiere que este en la lista
    for i in range(a):
        f = int(input("Ingrese el indice "+str(i)+" de la primera lista: ")) 
        lista1.append(f)
    for n in range(a):
        o = int(input("Ingrese el indice "+str(n)+" de la segunda lista: "))
        lista2.append(o)
print(productoPunto(lista1, lista2))#Se llama la función y se le ponen las listas