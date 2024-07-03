def heapify(arr, n, i):
    largest = i  # Inicializamos el nodo más grande como raíz
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Si el hijo izquierdo es más grande que la raíz
    if left < n and arr[i] < arr[left]:
        largest = left

    # Si el hijo derecho es más grande que el mayor actual
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Si el mayor no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambia
        print(f"Intercambiando {arr[i]} con {arr[largest]}")
        print(f"Array después del intercambio: {arr}")
        
        # Heapify la raíz.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construir un maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(f"Maxheap después de heapify en índice {i}: {arr}")

    # Extraer elementos uno por uno
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambia
        print(f"Intercambiando {arr[i]} con {arr[0]}")
        print(f"Array después del intercambio: {arr}")
        heapify(arr, i, 0)
        print(f"Heapify después de remover el elemento {i}: {arr}")

    return arr


def main(arr):
    elementos = arr.split(",")
    for i in range(len(elementos)):
        if elementos[i].isdigit():
           elementos[i] = int(elementos[i])
           
    res =  heap_sort(elementos)
    sorted_elements = [str(x) for x in res]
    print("Elementos ordenados: " + ", ".join(sorted_elements))
    elements_sorted = ",".join(sorted_elements)
     #print("Lista de números después del ordenamiento: ",res)
    return elements_sorted