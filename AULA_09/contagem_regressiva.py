# Contagem regressiva:

# Peça ao usuário para inserir um `número inteiro positivo`. Use um `laço while` para fazer uma contagem regressiva a partir desse número até 1 e, no final, imprima `“FOGO!!!”`.

numero = int(input("🔢 Digite um número inteiro positivo para a contagem: "))

while numero > 0:
    print(numero)
    # numero = numero - 1 # Decrementa o número em 1 em cada iteração
    numero -= 1 
print("🔥FOGO!!!")