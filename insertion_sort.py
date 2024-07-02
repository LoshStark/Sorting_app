def insertion_sort(arr):
    # Recorremos toda la lista empezando por el segundo elemento
    print("Arreglo original:", arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nComenzando iteración {i}: intentando insertar {key}")

        # Movemos los elementos del arreglo que son mayores que la clave, una posición adelante de su posición actual
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            print(f"Moviendo {arr[j]} de posición {j} a {j + 1}")
            j -= 1

        arr[j + 1] = key
        print(f"Inserta {key} en su posición correcta en {j + 1}")
        print("Estado actual del arreglo:", arr)
    
    return arr

def main(arr):
 
    elementos = arr.split(",")
    for i in range(len(elementos)):
        if elementos[i].isdigit():
           elementos[i] = int(elementos[i])
           
    res =  insertion_sort(elementos)
    sorted_elements = [str(x) for x in res]
    print("Elementos ordenados: " + ", ".join(sorted_elements))
    elements_sorted = ",".join(sorted_elements)
     #print("Lista de números después del ordenamiento: ",res)
    return elements_sorted