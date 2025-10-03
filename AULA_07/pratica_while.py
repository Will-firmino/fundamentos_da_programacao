# Faça um programa em python utilizando while onde você irá perguntar ao usuário qual o sabor da pizza que ele quer. Continue perguntando até que o cliente digite sair. 
#pedido = "" # Força explicitamente a variável pedido a ser do tipo string.


while True: 
    pedido = input(" Faça seu pedido (digite 'sair' para encerrar):") 
    if pedido.lower() == "sair":
        print(" ❌ Saindo do sistema ...")
        break
    print(f"🍕 {pedido} adicionado com sucesso.")
    break

print(" 🖖 Agradecemos a preferência. Volte sempre.")



