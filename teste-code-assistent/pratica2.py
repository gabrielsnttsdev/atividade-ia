# ==============================
# PRÁTICA 2 — REFATORAÇÃO
# ==============================

# 🔴 Código original (ruim)
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn


# 🟢 Código refatorado (boas práticas)
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


# 🔹 Exemplo de uso
if __name__ == "__main__":
    lista = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

    resultado = calcular_estatisticas(lista)

    print("total:", resultado["total"])
    print("media:", resultado["media"])
    print("maior:", resultado["maior"])
    print("menor:", resultado["menor"])


# ==============================
# 🧠 ANÁLISE DAS MELHORIAS
# ==============================

# 1. Nomes mais descritivos:
#    - c -> calcular_estatisticas
#    - l -> numeros
#    - t -> total
#    - m -> media
#    - mx -> maior
#    - mn -> menor

# 2. Remoção de range(len()):
#    - Substituído por funções nativas (sum, max, min)

# 3. Retorno estruturado:
#    - Antes: vários valores soltos
#    - Agora: dicionário com chaves descritivas

# 4. Código mais limpo:
#    - Menos loops
#    - Menos repetição

# 5. Adição de docstring:
#    - Explica o que a função faz

# 6. Melhor legibilidade:
#    - Organização clara
#    - Fácil manutenção
