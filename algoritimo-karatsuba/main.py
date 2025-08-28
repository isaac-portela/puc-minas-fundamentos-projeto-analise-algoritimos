
# Karatsuba (u, v, n)
# 1  se n ≤ 3
# 2  devolva u × v e pare
# 3  m := ⌈n/2⌉
# 4  p := ⌊u/10^m⌋
# 5  q := u mod 10^m
# 6  r := ⌊v/10^m⌋
# 7  s := v mod 10^m
# 8  pr := Karatsuba(p, r, m)
# 9  qs := Karatsuba(q, s, m)
# 10 y := Karatsuba(p+q, r+s, m+1)
# 11 uv := pr × 10^(2m) + (y − pr − qs) × 10^m + qs
# 12 devolva uv

from typing import Optional, Tuple


def contar_digitos(n: int) -> int:
    """
    Conta quantos dígitos decimais possui um inteiro não negativo.
    Observação: por convenção, 0 tem 1 dígito.
    """
    if n == 0:
        return 1
    cont = 0
    while n > 0:
        n //= 10
        cont += 1
    return cont


def separar_em_altobaixo(numero: int, m: int) -> Tuple[int, int]:
    """
    Separa 'numero' em duas partes usando 10^m:
      alto = floor(numero / 10^m)
      baixo = numero mod 10^m
    Retorna (alto, baixo).
    """
    base = 10 ** m
    alto = numero // base
    baixo = numero % base
    return alto, baixo


def karatsuba(u: int, v: int, n: Optional[int] = None) -> int:

    # Trata sinais (permite inteiros negativos)
    sinal = 1
    if u < 0:
        u = -u
        sinal *= -1
    if v < 0:
        v = -v
        sinal *= -1

    # Se algum é zero, retorno imediato
    if u == 0 or v == 0:
        return 0

    # Define n (número de dígitos do maior operando)
    if n is None:
        n = max(contar_digitos(u), contar_digitos(v))

    # Caso-base: para números pequenos, multiplicação direta é mais eficiente
    if n <= 3:
        return sinal * (u * v)

    # m = ceil(n/2)
    m = (n + 1) // 2

    # Divide u e v em partes alta (p, r) e baixa (q, s)
    p, q = separar_em_altobaixo(u, m)  # u = p*10^m + q
    r, s = separar_em_altobaixo(v, m)  # v = r*10^m + s

    # Três multiplicações recursivas (Karatsuba)
    pr = karatsuba(p, r, m)             # p * r (partes altas)
    qs = karatsuba(q, s, m)             # q * s (partes baixas)
    y  = karatsuba(p + q, r + s, m + 1) # (p+q) * (r+s)

    # Termo do meio: (p*q cruzado) = y - pr - qs
    meio = y - pr - qs

    # Combinação final:
    # uv = pr * 10^(2m) + meio * 10^m + qs
    resultado = (pr * (10 ** (2 * m))) + (meio * (10 ** m)) + qs

    return sinal * resultado


# ----------------- Exemplo de uso / Teste rápido -----------------
if __name__ == "__main__":
    x = 145623
    y = 653324

    produto_karatsuba = karatsuba(x, y)
    produto_direto = x * y

    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Karatsuba: {produto_karatsuba}")
    print(f"Produto Direto    : {produto_direto}")
    print("E igual?", produto_karatsuba == produto_direto)

    # Alguns testes adicionais
    casos = [
        (0, 123456),
        (123, 456),
        (9999, 9999),
        (-12345, 67890),
        (-1234567, -8901234),
        (10**20 + 12345, 10**18 + 67890),
    ]
    for a, b in casos:
        assert karatsuba(a, b) == a * b, f"Falhou em {a} * {b}"
    print("Todos os testes adicionais passaram!")
