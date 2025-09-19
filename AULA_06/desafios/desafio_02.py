# O cinema “CineMais” cobra **R$ 20,00 o ingresso**.

# 1. Pergunte a idade do cliente.
# 2. Se a idade for **menor que 12 anos**, o ingresso custa **R$ 10,00**.
# 3. Se a idade for **60 anos ou mais**, o ingresso custa **R$ 12,00**.
# 4. Caso contrário, o ingresso custa o valor normal (**R$ 20,00**).

# Preço padrão
preco = 20.00

# Entrada de dados
idade = int(input("Qual a sua idade? "))

# Condicional para verificar desconto
if idade < 12:
    preco = 10.00
elif idade >= 60:
    preco = 12.00

print(f"O valor do ingreso é R$ {preco:.2f}")