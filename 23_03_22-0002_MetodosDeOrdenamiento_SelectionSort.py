# Jaime Santiago Garci­a - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Internos ---> SelectionSort

import random

# Creamos una lista de numeros al azar
numeros = [random.randint(1, 1000) for i in range(100)]
print("Lista original: ", numeros)

# Iteramos sobre la lista, seleccionando el numero más pequeño y moviendolo a la posicion correcta
for i in range(len(numeros)):
    # Encontramos el indice del numero mas pequeño en la porción de la lista que no ha sido ordenada aun
    indice_minimo = i
    for j in range(i+1, len(numeros)):
        if numeros[j] < numeros[indice_minimo]:
            indice_minimo = j
    
    # Intercambiamos el numero actual con el numero mas pequeño encontrado
    numeros[i], numeros[indice_minimo] = numeros[indice_minimo], numeros[i]

print("Lista ordenada: ", numeros)
