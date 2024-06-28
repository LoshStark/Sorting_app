def selection_sort(lista):
 n = len(lista)
 for i in range(n):
    indice_minimo = i
    for j in range(i + 1, n):
      if lista[j] < lista[indice_minimo]:
        indice_minimo = j
        print(lista)
        print(f"{lista[i]} intercambia con: --> {lista[indice_minimo]}")
    lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]


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