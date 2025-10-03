# 1ª Possibilidade - Com condição lógica
nome_usuario = input("Digite o seu nome: ")

while nome_usuario != "jose": # Enquanto o nome_do_usuario for diferente de jose.
    print(f"Seja bem vindo {nome_usuario}")
    nome_usuario = input("Digite o seu nome: ")

# 2ª Possibilidade - Com condição lógica mas sem perguntar ao usuário a condição.
nome_usuario = True
while nome_usuario:
    nome_usuario = input("Digite o seu nome: ")
    print(f"Seja bem vindo {nome_usuario}")
    if nome_usuario == "jose":
        break # Quebra o laço de repetição mais próximo

# 3ª Possibilidade - Sem precisar passar condição lógica
while True:
    nome_usuario = input("Digite o seu nome: ")
    print(f"Seja bem vindo {nome_usuario}")
    if nome_usuario == "jose":
        break # Quebra o laço de repetição mais próximo

