# - Gasolina: **R$ 5,50/litro**
# - Etanol: **R$ 4,00/litro**

# 1. Pergunte ao cliente qual combustível deseja (Gasolina ou Etanol).
# 2. Pergunte quantos litros deseja abastecer.
# 3. Calcule e mostre o valor a pagar.
# 4. Se o cliente abastecer mais de **20 litros de etanol**, ele ganha **5% de desconto**.

# Preços dos combustíveis
PRECO_GASOLINA = 5.50
PRECO_ETANOL = 4.00

# Variável do desconto
desconto_etanol = 0.05

# Entrada de dados
combustivel = input("Qual o combustível deseja (gasolina/etanol)").lower()
litros = float(input("Quantos litros você deseja abastecer? "))

# Condicional para calcular o valor
if combustivel == "gasolina":
    total = litros * PRECO_GASOLINA
elif combustivel == "etanol":
    total = litros * PRECO_ETANOL
    if litros > 20:
        desconto = total * desconto_etanol
        total -= desconto
        # total = total - desconto
else:
    total = 0
    print("Combustível inválido.")

print(f"Valor a pagar R$ {total:.2f}")

