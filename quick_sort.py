def quick_sort(arr):
    # Función auxiliar para particionar el arreglo
    def partition(low, high):
        pivot = arr[high]  # Elegimos el último elemento como pivote
        i = low - 1  # Índice del elemento más pequeño
        for j in range(low, high):
            if arr[j] <= pivot:  # Si el elemento actual es menor o igual al pivote
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Intercambiamos elementos
                print(f"Intercambiando: {arr[i]} y {arr[j]} - {arr}")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Colocamos el pivote en la posición correcta
        print(f"Colocando el pivote {arr[i + 1]} en la posición correcta - {arr}")
        return i + 1  # Devolvemos el índice del pivote

    # Función recursiva principal del Quick Sort
    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)  # Obtenemos el índice de partición
            print(f"Partición en índice {pi} - {arr}")
            quick_sort_recursive(low, pi - 1)  # Ordenamos los elementos antes de la partición
            quick_sort_recursive(pi + 1, high)  # Ordenamos los elementos después de la partición

    # Llamada inicial a la función recursiva
    quick_sort_recursive(0, len(arr) - 1)
    return arr
# Ejemplo de uso
def main(arr):
    elementos = arr.split(",")
    for i in range(len(elementos)):
        if elementos[i].isdigit():
           elementos[i] = int(elementos[i])
           
    res =  quick_sort(elementos)
    sorted_elements = [str(x) for x in res]
    print("Elementos ordenados: " + ", ".join(sorted_elements))
    elements_sorted = ",".join(sorted_elements)
     #print("Lista de números después del ordenamiento: ",res)
    return elements_sorted