# ==============================
# PRÁTICA 3 — DEBUG COM IA
# ==============================

# 🔴 Código com erros (original)
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input(Preço do item 1? ))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)


# ==============================
# ❌ ERROS IDENTIFICADOS
# ==============================

# 1. Erro de sintaxe:
#    Falta de indentação no bloco do "if"
#    A linha do print deveria estar indentada.

# 2. Erro de tipo (TypeError):
#    desconto_cupom é uma string (input),
#    mas está sendo usado em cálculo matemático.

# 3. Erro de sintaxe:
#    Falta de aspas na linha:
#    item1 = float(input(Preço do item 1? ))

# 4. Erro de formatação:
#    print(" Item 2:        R$ {total_item2:.2f}")
#    não usa f-string


# ==============================
# 🧠 EXPLICAÇÃO DOS ERROS
# ==============================

# - Python exige indentação correta após estruturas como "if"
# - input() sempre retorna string, então precisa converter para float/int
# - Strings devem estar entre aspas
# - Para formatar variáveis, deve-se usar f-string (f"")


# ==============================
# ✅ CÓDIGO CORRIGIDO
# ==============================

# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))  # converter quantidade para inteiro para usar em cálculo de valor
item1 = float(input("Preço do item 1? "))  # preço pode ter centavos, por isso float

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3  # soma dos valores antes de impostos e descontos
imposto = subtotal * 0.10  # alíquota fixa de 10%

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))  # permite valores decimais no percentual
# converte o percentual de desconto em fração antes de aplicar sobre o subtotal
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto  # valor final considera imposto adicionado e desconto subtraído

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:  # só exibe linha de desconto quando existe desconto aplicado
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
