def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Array para el resultado
    count = [0] * 10  # Array para el conteo de dígitos

    # Contamos las ocurrencias de cada dígito en exp
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    print(f"Conteo de dígitos en exp={exp}: {count}")

    # Cambiamos count[i] para que contenga la posición actual de este dígito en output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    print(f"Posiciones actualizadas: {count}")

    # Construimos el array de salida
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copiamos el array de salida a arr[], para que arr[] contenga los números ordenados
    for i in range(n):
        arr[i] = output[i]

    print(f"Array ordenado por exp={exp}: {arr}")

def radix_sort(arr):
    # Encuentra el número con el máximo valor para saber el número de dígitos
    max1 = max(arr)

    # Hacemos counting sort para cada dígito. En lugar de pasar el número del dígito,
    # pasamos exp que es 10^i donde i es el número del dígito actual
    exp = 1
    while max1 // exp > 0:
        print(f"\nProcesando dígitos en exp={exp}")
        counting_sort(arr, exp)
        exp *= 10

    return arr



def main(arr):
    elementos = arr.split(",")
    for i in range(len(elementos)):
        if elementos[i].isdigit():
           elementos[i] = int(elementos[i])
           
    res =  radix_sort(elementos)
    sorted_elements = [str(x) for x in res]
    print("Elementos ordenados: " + ", ".join(sorted_elements))
    elements_sorted = ",".join(sorted_elements)
     #print("Lista de números después del ordenamiento: ",res)
    return elements_sorted