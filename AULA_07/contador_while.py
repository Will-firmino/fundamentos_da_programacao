# Monte um sistema utilizando while onde uma mensagem será exibida para o usuário com o número atual até que o valor seja 0.
contador = 10
while contador > 0:
    print(f"O número atual é o {contador}")
    contador -= 1
    # contador = contador -1 # Decrementar
print("Contagem encerrada!")

# Monte um sistema utilizando while onde uma mensagem será exibida para o usuário com o número atual até que o valor seja 0. Quando o valor for 6, não exiba a mensagem.
contador = 10
while contador > 0:
    if contador == 6:
        continue
    print(f"O número atual é o {contador}")
    contador -= 1
    # contador = contador -1 # Decrementar
print("Contagem encerrada!")