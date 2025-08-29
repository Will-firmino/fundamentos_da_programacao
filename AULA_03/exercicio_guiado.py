# Faça um programa aonde o cliente irá escolher o sabor de pizza e o sistema irá exibir o valor.
print(f"""
    ===================================
     🍕 Bem-vindo à pizzaria SABORES
            Escolha a sua pizza.
        1 - Mussarela (R$ 30)
        2 - Calabresa (R$ 32)
        3 - Frango com Catupiry (R$ 40)
    ===================================
""")
opcao = int(input("Digite o número do sabor desejado:"))
if opcao == 1:
    print("Você escolheu Mussarela - R$ 30,00")
elif opcao == 2:
    print("Você escolheu Calabresa - R$ 32,00")
elif opcao == 3:
    print("Você escolheu Frango com Catupiry - R$ 40,00")
else:
    print("❌ Opção inválida. Escolha um sabor do cardápio!")
