# Jaime Santiago Garci­a - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Internos ---> RadixSort

import random

# Generamos una lista de números aleatorios
lista_numeros = [random.randint(1, 1000) for i in range(100)]

# Función de RadixSort que toma una lista como entrada y devuelve la lista ordenada
def radix_sort(lista):
    # Obtenemos el número máximo de dígitos en la lista
    max_dig = len(str(max(lista)))
    
    # Realizamos el ordenamiento por cada dígito
    for dig in range(max_dig):
        # Creamos 10 cubetas para cada dígito
        cubetas = [[] for i in range(10)]
        # Colocamos cada número en la cubeta correspondiente según su dígito actual
        for num in lista:
            digito = (num // (10 ** dig)) % 10
            cubetas[digito].append(num)
        # Juntamos las cubetas en una sola lista
        lista = []
        for cubeta in cubetas:
            lista.extend(cubeta)
    
    return lista

# Imprimimos la lista original
print("Lista original:")
print(lista_numeros)

# Ordenamos la lista usando RadixSort
lista_ordenada = radix_sort(lista_numeros)

# Imprimimos la lista ordenada
print("Lista ordenada:")
print(lista_ordenada)


