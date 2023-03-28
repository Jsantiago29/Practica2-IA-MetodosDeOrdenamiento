# Jaime Santiago Garcia - 20310369
# Inteligencia Artifical
# Algoritmos de ordenamiento: Externos  ---> Natural merging
import random

# Función para ordenar un arreglo utilizando el método natural merging
def natural_merge_sort(arr):
    
    # Dividir el arreglo en segmentos ordenados
    segments = []
    left, right = 0, 0
    
    # Mientras queden elementos por recorrer en el arreglo
    while left < len(arr):
        
        # Encontrar el final del segmento actual
        right = left + 1
        while right < len(arr) and arr[right] >= arr[right - 1]:
            right += 1
        
        # Agregar el segmento actual a la lista de segmentos
        segments.append(arr[left:right])
        
        # Mover el índice de inicio al inicio del siguiente segmento
        left = right
    
    # Combinar los segmentos ordenados en un solo arreglo ordenado
    while len(segments) > 1:
        
        # Crear una lista para los segmentos combinados
        merged_segments = []
        
        # Recorrer los segmentos adyacentes de dos en dos
        i = 0
        while i < len(segments) - 1:
            
            # Tomar dos segmentos adyacentes y comparar sus elementos para crear un nuevo segmento ordenado
            left_segment, right_segment = segments[i], segments[i + 1]
            merged_segment = []
            left_index, right_index = 0, 0
            while left_index < len(left_segment) and right_index < len(right_segment):
                if left_segment[left_index] <= right_segment[right_index]:
                    merged_segment.append(left_segment[left_index])
                    left_index += 1
                else:
                    merged_segment.append(right_segment[right_index])
                    right_index += 1
            
            # Agregar los elementos restantes del segmento izquierdo y del segmento derecho
            merged_segment += left_segment[left_index:]
            merged_segment += right_segment[right_index:]
            
            # Agregar el nuevo segmento combinado a la lista de segmentos combinados
            merged_segments.append(merged_segment)
            
            # Mover el índice al siguiente par de segmentos adyacentes
            i += 2
        
        # Si queda un segmento sin combinar, agregarlo a la lista de segmentos combinados
        if i == len(segments) - 1:
            merged_segments.append(segments[-1])
        
        # Actualizar la lista de segmentos para la siguiente iteración del bucle while
        segments = merged_segments
    
    # Devolver el arreglo ordenado
    return segments[0]

# Crear un arreglo de 100 números aleatorios
arr = [random.randint(1, 1000) for i in range(100)]

# Imprimir el arreglo desordenado
print("Arreglo original:", arr)

# Ordenar el arreglo utilizando el método natural merging
sorted_arr = natural_merge_sort(arr)

# Imprimir el arreglo ordenado
print("Arreglo ordenado:", sorted_arr)
