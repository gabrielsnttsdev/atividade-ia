# ==============================
# PRÁTICA 1 — NÚMERO PRIMO
# ==============================

# 🔹 Versão simples
def eh_primo_simples(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


# 🔹 Versão otimizada (clean code)
def eh_primo(n: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é divisível apenas por 1 e por ele mesmo.
    """

    if n < 2:
        return False

    if n in (2, 3):
        return True

    if n % 2 == 0:
        return False

    limite = int(n ** 0.5) + 1

    for divisor in range(3, limite, 2):
        if n % divisor == 0:
            return False

    return True


# 🔹 Testes (demonstração de uso)
if __name__ == "__main__":
    numeros_teste = [1, 2, 3, 4, 7, 10, 13, 16]

    print("=== Testando versão simples ===")
    for num in numeros_teste:
        print(f"{num}: {eh_primo_simples(num)}")

    print("\n=== Testando versão otimizada ===")
    for num in numeros_teste:
        print(f"{num}: {eh_primo(num)}")
