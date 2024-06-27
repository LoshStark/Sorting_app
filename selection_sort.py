def selection_sort(arr):
    for i in range(len(arr) - 1):
     indice_menor = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[indice_menor]:
        indice_menor = j
        arr[i], arr[indice_menor] = arr[indice_menor], arr[i]


def main(input_string):
    #input_string = input("Ingrese números y letras separados por comas: ")
    input_string = input_string
    # Separar la entrada por comas y eliminar espacios en blanco
    elements = [x.strip() for x in input_string.split(',')]
    
    # Convertir elementos numéricos a enteros para una comparación correcta
    for i in range(len(elements)):
        if elements[i].isdigit():
            elements[i] = int(elements[i])
    
    # Aplicar bubble sort a la lista
    selection_sort(elements)
    
    # Convertir los elementos de vuelta a cadena para la visualización
    sorted_elements = [str(x) for x in elements]
    
    # Mostrar el resultado
    print("Elementos ordenados: " + ", ".join(sorted_elements))
    elements_sorted = ",".join(sorted_elements)
    
    return elements_sorted