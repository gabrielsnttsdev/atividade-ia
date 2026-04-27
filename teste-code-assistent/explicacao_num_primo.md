# 🔢 Verificação de Número Primo em Python

Este documento explica, passo a passo, o funcionamento de uma função em Python que verifica se um número é primo.

---

##  Código Versão Simples


def eh_primo(n):
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
🧠 Explicação linha por linha
def eh_primo(n):
Define a função que recebe um número n.
if n <= 1:
Verifica se o número é menor ou igual a 1.
return False
Números menores ou iguais a 1 não são primos.
if n == 2:
Verifica se o número é igual a 2.
return True
O número 2 é primo.
if n % 2 == 0:
Verifica se o número é divisível por 2.
return False
Se for par (e diferente de 2), não é primo.
for i in range(3, int(n ** 0.5) + 1, 2):
Percorre possíveis divisores até a raiz quadrada do número.
if n % i == 0:
Verifica se há algum divisor.
return False
Se encontrar divisor, não é primo.
return True
Se nenhum divisor for encontrado, o número é primo.
📊 Resumo

A função evita verificações desnecessárias e utiliza a raiz quadrada como limite, tornando o algoritmo mais eficiente.

🔢 Versão Otimizada Clean Code
📌 Código
def eh_primo(n: int) -> bool:
    """
    Verifica se um número inteiro é primo.
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
🚀 Melhorias aplicadas
Uso de tipagem (int -> bool)
Inclusão de docstring
Código mais legível
Uso de variável limite
Menos verificações desnecessárias
⚡ Complexidade
Tempo: O(√n)
Espaço: O(1)
📌 Exemplo de uso
numero = 29

if eh_primo(numero):
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")
🧾 Conclusão

A versão otimizada mantém a eficiência do algoritmo e melhora a organização do código, facilitando sua manutenção e entendimento.
