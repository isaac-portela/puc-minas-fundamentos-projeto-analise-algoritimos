#!/usr/bin/env python3
"""
MaxMin Select (Divide and Conquer) — main.py

Este módulo implementa a seleção simultânea do menor e do maior
elementos de uma sequência usando divisão e conquista.

A ideia:
- Divide o problema em duas metades;
- Resolve recursivamente cada metade (menor e maior de cada subarray);
- Combina os resultados com APENAS 2 comparações:
    * min_global = min(min_esq, min_dir)   -> 1 comparação
    * max_global = max(max_esq, max_dir)   -> 1 comparação

Número de comparações (quando n é potência de 2): T(n) = 2T(n/2) + 2,
com base T(2) = 1 e T(1) = 0, resultando em T(n) = 3n/2 - 2.
Para n geral, o algoritmo continua Θ(n).
"""

from typing import Iterable, Tuple, List
import random


def maxmin_divide_and_conquer(arr: List[float]) -> Tuple[float, float, int]:
    """
    Retorna (menor, maior, comparacoes) para a lista arr.
    Implementação recursiva por divisão e conquista, minimizando comparações.

    Regras de base:
      - n == 0: levanta ValueError (não há min/max de vazio);
      - n == 1: (x, x) e 0 comparações;
      - n == 2: 1 comparação para decidir qual é min e qual é max.

    Para n > 2:
      - Divide em duas metades;
      - Resolve recursivamente cada metade;
      - Combina com 2 comparações (min e max globais).
    """
    n = len(arr)
    if n == 0:
        raise ValueError("Sequência vazia: não é possível obter menor/maior.")
    if n == 1:
        return arr[0], arr[0], 0
    if n == 2:
        # 1 comparação apenas
        if arr[0] < arr[1]:
            return arr[0], arr[1], 1
        else:
            return arr[1], arr[0], 1

    mid = n // 2
    minL, maxL, cL = maxmin_divide_and_conquer(arr[:mid])
    minR, maxR, cR = maxmin_divide_and_conquer(arr[mid:])

    # Combinação com 2 comparações
    comparisons = cL + cR
    if minL < minR:        # 1ª comparação
        minG = minL
    else:
        minG = minR

    if maxL > maxR:        # 2ª comparação
        maxG = maxL
    else:
        maxG = maxR

    return minG, maxG, comparisons + 2


def maxmin_pairwise(arr: List[float]) -> Tuple[float, float, int]:
    """
    Variante clássica por 'pairing' (comparando os elementos em pares).
    Também obtém no máximo ~ 3n/2 - 2 comparações para n >= 2.
    Útil para comparar os contadores de comparação.
    """
    n = len(arr)
    if n == 0:
        raise ValueError("Sequência vazia.")
    if n == 1:
        return arr[0], arr[0], 0

    # Inicialização: se n é par, comparamos os dois primeiros (1 comparação)
    # Se n é ímpar, começamos com o primeiro como min=max e 0 comparações.
    count = 0
    if n % 2 == 0:
        if arr[0] < arr[1]:
            mn, mx = arr[0], arr[1]
        else:
            mn, mx = arr[1], arr[0]
        count += 1
        i = 2
    else:
        mn = mx = arr[0]
        i = 1

    # Itera de 2 em 2: 1 comparação para decidir a ordem do par,
    # depois 1 comparação com mn e 1 com mx => 3 comparações a cada 2 elementos.
    while i < n:
        a, b = arr[i], arr[i+1] if i+1 < n else arr[i]
        if a < b:
            count += 1  # a vs b
            if a < mn:
                mn = a
            else:
                # ainda assim precisa comparar b com mx
                if b > mx:
                    mx = b
            count += 2  # a vs mn, (b vs mx) — contabiliza como duas
        else:
            count += 1  # a vs b
            if b < mn:
                mn = b
            else:
                if a > mx:
                    mx = a
            count += 2  # b vs mn, (a vs mx)

        i += 2

    return mn, mx, count


def _demo():
    print("Demonstração rápida do MaxMin Select (divisão e conquista):")
    arr = [7, -2, 9, 4, 0, 11, 3, 5]
    mn, mx, comps = maxmin_divide_and_conquer(arr)
    print(f"Entrada: {arr}")
    print(f"Menor = {mn}, Maior = {mx}, Comparações = {comps}")

    # Comparação com a variante 'pairwise'
    mn2, mx2, comps2 = maxmin_pairwise(arr)
    print("\nVariante pairwise:")
    print(f"Menor = {mn2}, Maior = {mx2}, Comparações = {comps2}")


if __name__ == '__main__':
    _demo()
