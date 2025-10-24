# ☑️ Média de notas:

# Crie uma `lista com 5 notas` de um aluno. Use um `laço for` para calcular a `média` dessas notas e `imprima o resultado`.

notas = [8.5, 9.0, 7.5, 10.0, 6.0]
soma_notas = 0

# Calcula a soma de todas as notas
for nota in notas:
    soma_notas += nota

media = soma_notas / len(notas)
print(f"A média das notas é: {media:.2f}")
