# ☑️  Soma de números em uma lista:

# Crie uma `lista de números` (por exemplo, [10, 2, 8, 7, 5]) e use um `laço for` para calcular a `soma` de todos os elementos. Ao final, `imprima o resultado`.

numeros = [10, 2, 8, 7, 5] # Lista de números.
soma = 0 # Variável para acumular a soma, començando em 0.

# Laço for que percorre cada número na lista números
for numero in numeros:
    # soma = soma + numero
    soma += numero # Adiciona o número atual a variável soma

# Imprime o resultado final
print(f"➕ A soma dos números é: {soma}")