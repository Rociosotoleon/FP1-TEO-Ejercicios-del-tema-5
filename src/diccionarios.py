from collections import Counter


def sustituye_palabras(texto: str, diccionario: dict[str, str]) -> str:
    """Sustituye en el texto las palabras que aparecen en el diccionario como claves por sus valores asociados.

    Parámetros:
        texto: Texto en el que se van a sustituir las palabras.
        diccionario: Diccionario con las palabras a sustituir como claves y las palabras sustitutas como valores.

    Devuelve:
        Texto resultante de las sustituciones.
    """
    palabras = texto.split()
    palabras_sustituidas = []
    for palabra in palabras:
        if palabra in diccionario: #si palabra es una clave de diccionario
            palabras_sustituidas.append(diccionario[palabra])
        else:
            palabras_sustituidas.append(palabra) 
        #res += diccionario.get(palabra, palabra)
    
    return " ".join(palabras_sustituidas) 



def indexa_por_iniciales(texto: str) -> dict[str, set[str]]:
    """
    Construye un diccionario que indexa las distintas palabras del texto
    (pasado a minúsculas) por sus iniciales.
    
    Parámetros:
        texto: Texto del que se van a extraer las palabras.
    
    Devuelve:
        Diccionario que asocia a cada inicial el conjunto de palabras
         que comienzan por dicha inicial.
    
    """
    # TODO: se puede hacer sin el if? no x ahora
    res = {}
    for palabra in texto.lower().split():
        clave = palabra[0]
        
        if clave in res:
            res[clave].add(palabra)
        else:
            res[clave] = {palabra}
    return res

def construye_frecuencias_bigramas_sin_counter(texto: str) -> dict[str, float]:
    """
    Construye un diccionario con las frecuencias normalizadas de cada bigrama 
    en el texto dado, ignorando mayúsculas y minúsculas.

    Un bigrama es una secuencia de dos letras consecutivas en el texto.

    Cada frecuencia estará contenida entre 0 y 1.
    
    Parámetros:
        texto: Texto del que se van a contar los bigramas.
    Devuelve:
        Diccionario que asocia a cada bigrama su frecuencia normalizada en el texto.
    """
    bigramas = []
    texto = texto.lower()
    for c1, c2 in zip(texto, texto[1:]):
        if c1.isalpha() and c2.isalpha():
                bigramas.append(c1 + c2)
                contador[bigrama] 
    contador = Counter(bigramas)
    total_bigramas = len(bigramas)
    res = {}
    for bigrama, conteo in contador.items():
        res[bigrama] = conteo / total_bigramas
    return res 
    #TODO: defauldict y arreglar el sin counter


def construye_frecuencias_bigramas(texto: str) -> dict[str, float]:
    """
    Construye un diccionario con las frecuencias normalizadas de cada bigrama 
    en el texto dado, ignorando mayúsculas y minúsculas.

    Un bigrama es una secuencia de dos letras consecutivas en el texto.

    Cada frecuencia estará contenida entre 0 y 1.
    
    Parámetros:
        texto: Texto del que se van a contar los bigramas.
    Devuelve:
        Diccionario que asocia a cada bigrama su frecuencia normalizada en el texto.
    """
    
    bigramas = []
    texto = texto.lower()
    for c1, c2 in zip(texto, texto[1:]):
        if c1.isalpha() and c2.isalpha():
            bigramas.append(c1 + c2)
    #haremos este counter sin crear en memoria la lista bigramas
    contador = Counter(bigramas)
    total_bigramas = len(bigramas)
    res = {}
    for bigrama, conteo in contador.items():
        res[bigrama] = conteo / total_bigramas
    return res 


def calcula_distancia_media_frecuencias(freq1: dict[str, float], freq2: dict[str, float]) -> float:
    """
    Calcula la distancia media entre las frecuencias normalizadas
    representadas por dos diccionarios de frecuencias.

    Parámetros:
        freq1: Primer diccionario de frecuencias.
        freq2: Segundo diccionario de frecuencias.

    Devuelve:
        Distancia media entre los dos vectores de frecuencias, o 0.0 si ambos diccionarios están vacíos.
    """
    if len(freq1) == 0 and len(freq2) == 0:
        return 0.0
    
    todos_bigramas = set(freq1).union(set(freq2))
    suma_bigramas = 0 
    for bigrama in todos_bigramas:
        suma_diferencias += abs(freq1.get(bigrama, 0) - freq2.get(bigrama, 0))
    return suma_diferencias / len(todos_bigramas)

def identifica_idioma(textos_ejemplo: dict[str, str], texto_a_identificar: str) -> str:
    """
    Identifica el idioma de un texto comparando sus frecuencias de bigramas
    con las frecuencias de bigramas de textos de ejemplo en distintos idiomas.

    Parámetros:
        textos_ejemplo: Diccionario que asocia a cada idioma (por ejemplo 'es') un texto de ejemplo en ese idioma.
        texto_a_identificar: Texto cuyo idioma se quiere identificar.

    Devuelve:
        El idioma identificado del texto.
    """
    #obtener el disccionario de frecuencia de texto a identificar (dic_objetivo)
    #recorrer el diccionario textos_ejemplo
    #obtener del diccionario frcuencias para el idioma actual (dic_idioma)
    #Para cada diccionario, calcular la distancia con el diccionario dic_objetivo
    #Guardamos en una lista(distancia, identificador_idioma)
    #devolver el identificador de idioma


    dic_objetivo = construye_frecuencias_bigramas(texto_a_identificar)
    distancias_idiomas = []
    for idioma, texto_idioma in textos_ejemplo.items():
        dic_idioma = construye_frecuencias_bigramas(texto_idioma)
        distancia = calcula_distancia_media_frecuencias(dic_objetivo, dic_idioma)
        distancias_idiomas.append((distancia, idioma))
    _, idioma= min(distancias_idiomas) #se usa _ cuando esa variable no se usa para nada 
    return idioma







