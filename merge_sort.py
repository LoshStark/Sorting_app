def merge_sort(arr):
    def merge(left, right):
        result = []
        i = j = 0
        print(f"Merge: izquierda {left} derecha {right}")
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        print(f"Resultado después de merge: {result}")
        return result

    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])
        return merge(left, right)

    print("Arreglo original:", arr)
    sorted_arr = merge_sort_recursive(arr)
    print("Lista ordenada:", sorted_arr)
    return sorted_arr






def main(arr):
    elementos = arr.split(",")
    for i in range(len(elementos)):
        if elementos[i].isdigit():
           elementos[i] = int(elementos[i])
           
    res =  merge_sort(elementos)
    sorted_elements = [str(x) for x in res]
    elements_sorted = ",".join(sorted_elements)
     #print("Lista de números después del ordenamiento: ",res)
    return elements_sorted