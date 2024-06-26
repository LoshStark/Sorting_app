def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Imprime el valor de arr[j] y arr[j+1] indicando que se intercambian
                print(arr)
                print(f"{arr[j]} intercambia con: --> {arr[j+1]}")
                    
                #Intercambio de valores en un arreglo
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    input_string = input("Ingrese números y letras separados por comas: ")
    
    # Separar la entrada por comas y eliminar espacios en blanco
    elements = [x.strip() for x in input_string.split(',')]
    
    # Convertir elementos numéricos a enteros para una comparación correcta
    for i in range(len(elements)):
        if elements[i].isdigit():
            elements[i] = int(elements[i])
    
    # Aplicar bubble sort a la lista
    bubble_sort(elements)
    
    # Convertir los elementos de vuelta a cadena para la visualización
    sorted_elements = [str(x) for x in elements]
    
    # Mostrar el resultado
    print("Elementos ordenados: " + ", ".join(sorted_elements))

if __name__ == "__main__":
    main()