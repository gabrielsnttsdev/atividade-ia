# ==============================
# PRÁTICA 4 — IA EXPLICANDO CÓDIGO
# ==============================

def calcular_estatisticas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.

    Retorna:
    - total
    - média
    - maior valor
    - menor valor
    """

    total = sum(numeros)
    media = total / len(numeros)
    maior = max(numeros)
    menor = min(numeros)

    return {
        "total": total,
        "media": media,
        "maior": maior,
        "menor": menor
    }


# ==============================
# 🧠 EXPLICAÇÃO LINHA POR LINHA
# ==============================

# def calcular_estatisticas(numeros):
# Define uma função chamada calcular_estatisticas que recebe uma lista de números.

# """
# Docstring que explica o objetivo da função e o que ela retorna.

# total = sum(numeros)
# Soma todos os valores da lista.

# media = total / len(numeros)
# Calcula a média dividindo o total pela quantidade de elementos.

# maior = max(numeros)
# Encontra o maior valor da lista.

# menor = min(numeros)
# Encontra o menor valor da lista.

# return { ... }
# Retorna um dicionário contendo os resultados:
# total, média, maior e menor valor.
