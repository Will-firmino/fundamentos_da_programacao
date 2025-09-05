# Crie um programa que calcula o **valor final de um pedido**, aplicando um desconto específico caso a compra seja feita em um dia de promoção.

# - Terça-feira: Pedidos acima de R$ 40 recebem uma sobremesa grátis (exiba uma mensagem).
# - Quarta-feira: Todas as pizzas têm 15% de desconto.
# - Sábado e Domingo: Pedidos acima de R$ 100 têm a taxa de entrega grátis (considere a taxa fixa de R$ 5 que seria cobrada).
# - Para os outros dias, não há promoção.

TAXA = 5 # Constante FAKE

dia_semana = "sabado"
valor_pedido = 110
distancia = 0
valor_final = valor_pedido
valor_menor_5 = 1
valor_menor_10 = 2
taxa_entrega = 0

print(f'🍕 Dia: {dia_semana}, Valor do Pedido: R${valor_pedido:.2f}')
if dia_semana == "terça" and valor_pedido > 40:
    print(" 🍰 Promoção aplicada. Sobremesa grátis.")
    if distancia <= 5:
        taxa_entrega = taxa_entrega + TAXA + (distancia * valor_menor_5)
        valor_pedido = valor_pedido + taxa_entrega
    elif distancia <= 10:
        taxa_entrega = taxa_entrega + TAXA + (distancia * valor_menor_10)
        valor_pedido = valor_pedido + taxa_entrega
    print(f'Valor total do pedido: R$ {valor_pedido}')
elif dia_semana == "quarta":
    valor_pedido = valor_pedido * 0.15 # Variável local
    print(" 🤑 Promoção aplicada: 15% de desconto!")
    if distancia <= 5:
        taxa_entrega = taxa_entrega + TAXA + (distancia * valor_menor_5)
        valor_pedido = valor_pedido + taxa_entrega
    elif distancia <= 10:
        taxa_entrega = taxa_entrega + TAXA + (distancia * valor_menor_10)
        valor_pedido = valor_pedido + taxa_entrega
    print(f'Valor total do pedido: R$ {valor_pedido}')
elif dia_semana == "sabado" or dia_semana == "domingo" and valor_pedido > 100:
    taxa_entrega = 0  # Variável local
    valor_pedido = valor_pedido + TAXA 
    print(f'Valor total do pedido: R$ {valor_pedido}')
else:
    print(" 😢 Sem promoção!")
    if distancia <= 5:
        taxa_entrega = taxa_entrega + TAXA + (distancia * valor_menor_5)
        valor_pedido = valor_pedido + taxa_entrega
    elif distancia <= 10:
        taxa_entrega = taxa_entrega + TAXA + (distancia * valor_menor_10)
        valor_pedido = valor_pedido + taxa_entrega
    print(f'Valor total do pedido: R$ {valor_pedido}')


# Pegue o código atual e o código do desafio 2 e refatore o código para que a
# taxa de entrega seja calculada junto com o valor final do pedido, se houver taxa.
