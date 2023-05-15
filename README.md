# Reto_10

## Punto 1

Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

```
lista1 = [5,6,8,7,1] #Se hizo la lista con los números
sum = 0 
for i in lista1: #Se toma cada número de la lista 
    sum += i #Se suman todo y se guarda en sum
prom = sum/len(lista1) #El total de la suma divido la cantidad de números en la lista
print("El promedia de la lista "+str(prom)) #Se imprime el promedio de la lista

```

## Punto 2

Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

```
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
```

## Punto 3

Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

```
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
```
