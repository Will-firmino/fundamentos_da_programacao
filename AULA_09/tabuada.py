# ☑️ Tabuada de multiplicação:

# Peça ao usuário para digitar um `número inteiro`. Em seguida, use o `laço for` para imprimir a `tabuada` desse número, `de 1 a 10`.

numero_tabuada = int(input("Digite um número para ver a tabuada: "))

print(f"🔢Tabuada de {numero_tabuada}")
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")
