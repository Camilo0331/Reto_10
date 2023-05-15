a = int(input("Ingrese la cantidad de números que quiere ingresar a la lista: "))#Se pide la cantidad de números en la lista
lista = [] #Lista vacia
#Según los indices se pregunta el número
for i in range(a): 
    f = int(input("Ingrese el indice "+str(i)+" de la primera lista: "))
    lista.append(f)
print("Lista con los números que ingreso "+str(lista))
for n in range(len(lista)): # n va a tomar de 0 hasta la longitud de la lista
    if lista[n] == 0: #Si un numero de la lista es igual a 0
        lista.append(lista[n]) #Se agrega al final
        lista.remove(lista[n]) #Se elimina el número de ese indice
print("La lista con los 0 al final"+str(lista)) #Se imprime la lista con los ceros al final de la lista