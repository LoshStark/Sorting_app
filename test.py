def ordenamiento_por_seleccion(lista):
  """
  Función que ordena una lista de elementos usando el método de ordenamiento por selección.

  Parámetros:
    lista: La lista de elementos a ordenar.

  Retorno:
    La lista ordenada.
  """
  n = len(lista)
  for i in range(n):
    indice_minimo = i
    for j in range(i + 1, n):
      if lista[j] < lista[indice_minimo]:
        indice_minimo = j
        print(lista)
        print(f"{lista[i]} intercambia con: --> {lista[indice_minimo]}")
    lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
  return lista

# Solicitar al usuario ingresar los elementos separados por comas
elementos_str = input("Ingrese elementos separados por comas: ")

# Convertir la cadena de entrada en una lista de elementos
elementos = elementos_str.split(",")

# Ordenar la lista de elementos
elementos_ordenados = ordenamiento_por_seleccion(elementos)

# Imprimir la lista ordenada
print("Lista ordenada:", elementos_ordenados)