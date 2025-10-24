# Validação de senha:

# Peça ao usuário para criar uma `senha`. Use um `laço while` para continuar pedindo a senha até que ela atenda a um critério mínimo, por exemplo, `ter pelo menos 8 caracteres.`

while True:
    senha = input("🔒 Crie uma senha (deve ter no mínimo 8 caracteres): ")

    # Verifica se o comprimento da senha é maior ou igual a 8
    if len(senha) >= 8:
        print("✅ Senha criada com sucesso!")
        break # A senha é válida, então o laço é encerrado.
    else:
        print("❌ A senha precisa ter no mínimo 8 caracteres)! Tente novamente.")