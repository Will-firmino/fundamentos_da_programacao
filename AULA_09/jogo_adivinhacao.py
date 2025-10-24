# Jogo de adivinhação:

# Crie um jogo simples onde o computador “pensa” em um número de `1 e 20` (você pode definir o número secretamente no código). Peça ao usuário para adivinhar o número. Use um `laço while` eque continue pedindo um palpite até que o usuário acerte. A cada tentativa, diga se o palpite foi `“muito alto”` ou `“muito baixo”`.

numero_secreto = 17 # O computador "pensou" este número.

# Laço infinito que só será quebrado com o comando break.
while True:
    palpite = int(input("Adivinhe o número secreto entre 1 e 20: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!!! ✅")
        break # Encerrar o loop
    elif palpite < numero_secreto:
        print(" ❌ Muito baixo! Tente novamente.")
    else:
        print("❌ Muilto alto! Tente novamente.")
    