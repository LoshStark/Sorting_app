def selection_sort(arr):
    # Recorremos toda la lista
    print("Arreglo original:", arr)
    for i in range(len(arr)):
        # Encontramos el índice del elemento más pequeño en la lista no ordenada
        min_index = i
        print(f"\nIteración {i+1}: buscando el elemento más pequeño desde la posición {i}")
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"Nuevo mínimo encontrado: {arr[min_index]} en la posición {min_index}")
        
        # Intercambiamos el elemento más pequeño con el primer elemento no ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Se ha seleccionado el elemento: {arr[i]} intercambia con: --> {arr[min_index]}")
        print("Estado actual del arreglo:", arr)
    return arr


def main(elementos_str):
     #elementos_str = input("Ingrese elementos separados por comas: ")
     elementos = elementos_str.split(",")
     for i in range(len(elementos)):
        if elementos[i].isdigit():
            elementos[i] = int(elementos[i])
     res =  selection_sort(elementos)
     sorted_elements = [str(x) for x in res]
    
    # Mostrar el resultado
     print("Elementos ordenados: " + ", ".join(sorted_elements))
     elements_sorted = ",".join(sorted_elements)
     #print("Lista de números después del ordenamiento: ",res)
     return elements_sorted
