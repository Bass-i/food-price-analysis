def merge_sort(lista):
    """
    Ordena una lista utilizando el algoritmo
    Merge Sort implementado de forma recursiva.

    Parámetros
    ----------
    lista : list
    """

    # Caso base.
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2

    izquierda = merge_sort(lista[:mitad])
    derecha = merge_sort(lista[mitad:])

    return fusionar(izquierda, derecha)


def fusionar(izquierda, derecha):
    """
    Fusiona dos listas ordenadas.

    Parámetros
    ----------
    izquierda : list

    derecha : list
    """

    resultado = []

    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):

        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado