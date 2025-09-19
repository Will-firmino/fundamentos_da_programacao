# A loja “Doce Sabor” vende balas a **R$ 0,50 cada** e chocolates a **R$ 2,00 cada**.

# 1. Pergunte ao cliente quantas balas e quantos chocolates ele deseja comprar.
# 2. Calcule o valor total da compra.
# 3. Se o valor total for **maior que R$ 20**, mostre a mensagem:
#     **"Parabéns, você ganhou um desconto de 10%!"** e aplique o desconto.
# 4. Mostre o valor final da compra.

# Constantes de preços
PRECO_BALA = 0.50
PRECO_CHOCOLATE = 2.00

# Entrada de dados
balas = int(input("Quantas balas você deseja? "))
chocolates = int(input("Quantas chocolates você deseja? "))

# Cálculo do valor total
total = (balas * PRECO_BALA) + (chocolates * PRECO_CHOCOLATE)

# Condicional do desconto
if total > 20:
    desconto = total * 0.10
    total = total - desconto
    print(f"Parabéns, você ganhou 10% de desconto! Valor final: R${total:.2f}")
else:
    print(f"Valor final da compra: R$ {total:.2f}")
