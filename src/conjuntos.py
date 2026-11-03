def elimina_duplicados(lista: list) -> list:
    """
    Devuelve la lista resultante de eliminar los elementos duplicados, 
    conservando para el resto de elementos el orden de la lista original.

    Parámetros:
    lista (list): Lista de elementos que puede contener duplicados.
    
    Devuelve:
    list: La lista sin elementos duplicados, manteniendo el orden original.
    """
    #para pasar de lista a conjunto set(lista)
    #sorted(set(lista))
    res = []
    vistos = set()
    for elem in lista:
        if elem not in vistos:
            res.append(elem)
            vistos.add(elem)
    return res

def une_conjuntos(lista_de_conjuntos: list[set]) -> set:
    """
    Devuelve el conjunto resultante de la unión de todos los conjuntos de la lista.

    Parámetros:
    lista_de_conjuntos (list[set]): Lista de conjuntos a unir.
    
    Devuelve:
    set: El conjunto resultante de la unión de todos los conjuntos.
    """
    res = set()
    for conjunto in lista_de_conjuntos:
        res = res | conjunto  #res = res.union(conjunto)
        #mas eficiente usar el metodo update
        res.update(conjunto)
    return res 
    

def intersecta_conjuntos(lista_de_conjuntos: list[set]) -> set:
    """
    Devuelve el conjunto resultante de la intersección de todos los conjuntos de la lista.

    Parámetros:
    lista_de_conjuntos (list[set]): Lista de conjuntos a intersectar.
    
    Devuelve:
    set: El conjunto resultante de la intersección de todos los conjuntos.
    """
    if len(lista_de_conjuntos) == 0:
        return set()
    
    res = lista_de_conjuntos[0]
    for conjunto in lista_de_conjuntos:
        res = res & conjunto #intersection 
    return res
# if not lista_de_conjuntos: no tiene elementos 