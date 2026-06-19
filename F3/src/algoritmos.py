def merge_sort(lista):
    """
    Ordena una lista de elementos comparables utilizando el algoritmo
    Merge Sort implementado de forma recursiva.

    Aplica la estrategia divide y vencerás: divide la lista en dos
    mitades, ordena cada mitad de forma recursiva y luego fusiona
    los resultados en orden ascendente.

    Parámetros
    ----------
    lista : list
        Lista de elementos comparables entre sí (números, strings, etc.).
        Puede estar vacía o contener un único elemento.

    Retorna
    -------
    list
        Nueva lista con los mismos elementos ordenados de menor a mayor.
        No modifica la lista original.

    Excepciones
    -----------
    TypeError
        Si los elementos de la lista no son comparables entre sí
        (por ejemplo, mezcla de strings y números).

    Complejidad
    -----------
    Temporal: O(n log n) en todos los casos (mejor, promedio y peor).
    Espacial: O(n) por el uso de listas auxiliares en cada nivel
    de recursión.

    Ejemplos
    --------
    >>> merge_sort([])
    []
    >>> merge_sort([5])
    [5]
    >>> merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
    [1, 1, 2, 3, 4, 5, 6, 9]
    >>> merge_sort([-3, 0, -1, 5])
    [-3, -1, 0, 5]
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
    Fusiona dos listas previamente ordenadas en una única lista ordenada.

    Recorre ambas listas simultáneamente comparando elementos de a uno,
    agregando siempre el menor al resultado. Los elementos restantes de
    la lista que no se agotó se agregan al final.

    Parámetros
    ----------
    izquierda : list
        Primera lista ordenada de menor a mayor.
    derecha : list
        Segunda lista ordenada de menor a mayor.

    Retorna
    -------
    list
        Nueva lista ordenada que contiene todos los elementos
        de izquierda y derecha.

    Complejidad
    -----------
    Temporal: O(n + m) donde n y m son los tamaños de izquierda y derecha.
    Espacial: O(n + m) por la lista resultado auxiliar.

    Ejemplos
    --------
    >>> fusionar([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> fusionar([], [1, 2])
    [1, 2]
    >>> fusionar([1], [])
    [1]
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

def insertion_sort(lista):
    """
    Ordena una lista de elementos comparables utilizando el algoritmo
    Insertion Sort (ordenamiento por inserción).

    Recorre la lista desde el segundo elemento. Para cada elemento,
    lo desplaza hacia la izquierda hasta encontrar su posición
    correcta entre los elementos ya ordenados.

    Se incluye como segunda implementación propia para comparar
    eficiencia frente a merge_sort en distintos tamaños de entrada.

    Parámetros
    ----------
    lista : list
        Lista de elementos comparables entre sí.
        No modifica la lista original; opera sobre una copia.

    Retorna
    -------
    list
        Nueva lista con los mismos elementos ordenados de menor a mayor.

    Excepciones
    -----------
    TypeError
        Si los elementos de la lista no son comparables entre sí.

    Complejidad
    -----------
    Temporal: O(n²) en el caso promedio y peor caso.
              O(n) en el mejor caso (lista ya ordenada).
    Espacial: O(n) por la copia interna de la lista.

    Ejemplos
    --------
    >>> insertion_sort([])
    []
    >>> insertion_sort([5])
    [5]
    >>> insertion_sort([3, 1, 4, 1, 5])
    [1, 1, 3, 4, 5]
    """

    resultado = lista[:]

    for i in range(1, len(resultado)):
        clave = resultado[i]
        j = i - 1

        while j >= 0 and resultado[j] > clave:
            resultado[j + 1] = resultado[j]
            j -= 1

        resultado[j + 1] = clave

    return resultado