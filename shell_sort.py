def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Inicialmente, el intervalo (gap) se reduce a la mitad en cada iteración
    while gap > 0:
        print(f"\nIntervalo (gap): {gap}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Realiza la inserción de elementos dentro de cada sublista creada por el intervalo
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                print(f"Moviendo {arr[j + gap]} a la posición {j + gap}")
            arr[j] = temp
            print(f"Inserta {temp} en la posición {j}")
            print(arr)

        gap //= 2

    return arr

def main(arr):
     elementos = arr.split(",")
     for i in range(len(elementos)):
        if elementos[i].isdigit():
           elementos[i] = int(elementos[i])
           
     res =  shell_sort(elementos)
     sorted_elements = [str(x) for x in res]
     print("Elementos ordenados: " + ", ".join(sorted_elements))
     elements_sorted = ",".join(sorted_elements)
     #print("Lista de números después del ordenamiento: ",res)
     return elements_sorted



