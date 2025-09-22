# MaxMin Select (Divisão e Conquista) — Python

> Seleção simultânea do **menor** e do **maior** elemento de uma sequência, com **número mínimo de comparações**.

---

## 📌 Descrição do projeto

Este projeto implementa, em `main.py`, o algoritmo **MaxMin Select** por **divisão e conquista**. A estratégia é:
1. **Dividir** a sequência ao meio;
2. **Resolver recursivamente** cada metade (obtendo menor e maior de cada subproblema);
3. **Combinar** os resultados com **apenas 2 comparações** (uma para o mínimo global e outra para o máximo global).

Essa abordagem reduz o número total de comparações em relação à solução ingênua (`2(n-1)`), atingindo, no caso ideal (quando `n` é potência de 2), **`3n/2 - 2`** comparações — que é assintoticamente **Θ(n)**.

---

## 🗂 Estrutura do repositório

```
.
├── main.py
└── assets/
    └── maxmin_recursion_tree.png   # Diagrama da recursão e das comparações por nível
```

---

## ▶️ Como executar o projeto (ambiente local)

### Requisitos
- Python 3.8+

### Passos
```bash
# 1) (opcional) criar e ativar venv
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 2) Executar
python main.py
```

A saída mostrará uma **demonstração** com:
- menor e maior da lista de exemplo,
- **contador** de comparações,
- e comparação com a variante **pairwise** (em pares).

---

## 🧠 Lógica do algoritmo (linha a linha)

A implementação principal está em `maxmin_divide_and_conquer(arr)`:

```py
if n == 0: raise ValueError(...)       # não há min/max de lista vazia
if n == 1: return (x, x, 0)            # 0 comparações
if n == 2:                             
    # 1 comparação para decidir quem é min e quem é max
    return (min(x,y), max(x,y), 1)
```

Para `n > 2` (passos centrais):
```py
mid = n // 2
minL, maxL, cL = maxmin_divide_and_conquer(arr[:mid])    # resolve esquerda
minR, maxR, cR = maxmin_divide_and_conquer(arr[mid:])    # resolve direita

# Combinação com exatamente 2 comparações
if minL < minR:       # 1ª comparação     -> minG = min(minL, minR)
    minG = minL
else:
    minG = minR

if maxL > maxR:       # 2ª comparação     -> maxG = max(maxL, maxR)
    maxG = maxL
else:
    maxG = maxR

return minG, maxG, cL + cR + 2
```

**Por que 2 comparações na combinação?**  
Os subproblemas já retornam os pares `(min, max)`. Para compor a resposta global, basta:
- comparar os **mínimos locais** para obter o **mínimo global** (1 comparação),
- comparar os **máximos locais** para obter o **máximo global** (1 comparação).

Total no *merge*: **2** comparações, independentemente do tamanho dos subarrays.

---

##  Relatório técnico — Análise de complexidade

## Contagem de comparações — MaxMin Select

**Casos base**
- $T(1)=0$ → com 1 elemento, ele é min e max.
- $T(2)=1$ → 1 comparação decide quem é min e quem é max.

**Para $n>2$**: dividimos o vetor em duas metades e, no *merge*, fazemos **2 comparações** (uma para o min global e outra para o max global):
$$
T(n)=T(\lfloor n/2 \rfloor)+T(\lceil n/2 \rceil)+2.
$$

Quando $n$ é potência de 2 ($n=2^k$), fica:
$$
T(n)=2\,T\!\left(\frac{n}{2}\right)+2,\qquad T(2)=1.
$$

**Expansão até a base**:
$$
\begin{aligned}
T(n) &= 2^{\,k-1}\,T(2) + 2\,(2^{\,k-1}-1) \\
     &= \frac{n}{2} + 2\!\left(\frac{n}{2}-1\right) \\
     &= \frac{3n}{2} - 2.
\end{aligned}
$$

**Resumo**: o algoritmo faz cerca de $\frac{3n}{2}-2$ comparações (quando $n$ é potência de 2) e, no geral, o custo é **linear**: $\Theta(n)$.

> Comparando: a versão “ingênua” (duas varreduras) faz $2(n-1)$ comparações.  
> As versões *pairwise* e *divide-and-conquer* ficam por volta de $1{,}5n$.

---

## Teorema Mestre — MaxMin Select

Recorrência no formato padrão:
$$
T(n)=a\cdot T\!\left(\frac{n}{b}\right)+f(n).
$$

Para este algoritmo:
$$
a=2,\qquad b=2,\qquad f(n)=\Theta(1).
$$

Logo:
$$
\log_b a=\log_2 2=1
\quad\Rightarrow\quad
f(n)=\Theta(1)=O(n^{1-\varepsilon})\;(\varepsilon=1).
$$

**Caso 1 do Teorema Mestre**:
$$
T(n)=\Theta\!\big(n^{\log_b a}\big)=\Theta(n).
$$

**Conclusão**: a ordem de tempo é **$\Theta(n)$**, o que bate com a conta de $\frac{3n}{2}-2$ comparações no caso ideal.


## 🖼 Diagrama da recursão 

O arquivo `assets/maxmin_recursion_tree.png` ilustra a **árvore de recursão** para `n = 8` elementos, mostrando:
- Divisões por nível (cada nó é um subproblema);
- **2 comparações** em cada *merge* (nó interno);
- Total por nível e soma ao longo dos níveis.



![Diagrama de recursao](assets/img_1.png))

---

## ✍ Referências didáticas (materiais do professor)

- *AULA 01 — Análise de complexidade de algoritmos.pdf*  
- Pasta de PDFs: repositório de apoio do professor


---

## 📎 Licença

Este projeto é de uso educacional.
