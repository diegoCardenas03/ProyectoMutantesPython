Detector de Mutantes

Este proyecto en Python implementa un algoritmo para detectar si un humano es mutante basándose en su secuencia de ADN.

Consigna:

Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Men. Te ha contratado para que desarrolles un proyecto que detecte si un humano es mutante basándose en su secuencia de ADN.

Debes crear un programa Python con una función con la siguiente firma:

def is_mutant(dna: List[str]) -> bool:
    pass

Donde recibirás como parámetro una lista de cadenas que representan cada fila de una tabla de (6x6) con la secuencia del ADN. Las letras de las cadenas solo pueden ser: (A, T, C, G), las cuales representan cada base nitrogenada del ADN.

Sabrás si un humano es mutante si encuentras más de una secuencia de cuatro letras iguales, de forma oblicua, horizontal o vertical.

Ejemplo:

dna = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]

Para la matriz anterior, el resultado debe ser True.
