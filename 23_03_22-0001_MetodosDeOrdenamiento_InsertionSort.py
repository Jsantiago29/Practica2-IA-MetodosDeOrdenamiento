# Jaime Santiago Garci�a - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Internos ---> InsertionSort

# Este modulo nos sirve para poder generar listas aleatorias de numeros
import random

def insertion_sort(arr):
    
    # Estamos recorriendos desde el segundo valor hasta el ultimo de las lista. 
    for i in range(1, len(arr)):
        
        # Tomamos el elemento actual como el valor a insertar en la posicion correcta
        key = arr[i]
        
        # Definimos una variable j que nos permite iterar hacia atrás a traves de la lista
        # para encontrar la posicion correcta para insertar el elemento actual
        j = i - 1
        
        # Mientras que j sea mayor o igual a cero y el elemento actual sea menor que el elemento
        # en la posicion j-enesima de la lista, seguimos iterando hacia atras
        while j >= 0 and key < arr[j]:
            
            # Desplazamos los elementos mayores que key una posicion hacia la derecha
            # para hacer espacio para insertar el elemento actual en la posicion correcta
            arr[j+1] = arr[j]
            j -= 1
            
        # Insertamos el elemento actual en la posicion correcta
        arr[j+1] = key

# Generamos una lista de 100 números aleatorios
arr = [random.randint(1, 1000) for i in range(100)]
print("Lista desordenada:", arr)

# Ordenamos la lista con el algoritmo de insercion
insertion_sort(arr)
print("Lista ordenada:", arr)
