# Desenvolva um módulo Python chamado `adicionando_carrinho.py` que contenha uma função para adicionar
# produtos a um carrinho de compras em uma loja online. A função deve receber o nome do produto,
# como parâmetros e armazenar essas informações em uma lista. Além disso, a função
# deve exibir uma mensagem confirmando que o produto foi adicionado com sucesso.
# Os produtos de exemplo são:
# 1. Nome: "Camiseta"
# 2. Nome: "Calça Jeans" 
# 3. Nome: "Tênis Esportivo"

# Função responsável por adicionar produtos no carrinho
def adicionar_produto():
    # Criar uma lista representando o carrinho
    carrinho = []

    while True:
        novo_produto = input("Informe qual o produto você deseja adicionar ao carrinho ou 'sair': ")
        # Caso o usuário escreva sair
        if novo_produto == 'sair':
            break

        # Lógica se o usuário digitar o nome do produto
        carrinho.append(novo_produto)
        print(f" Produto {novo_produto} adicionado com sucesso no carrinho. 🛒")

    # Exibir os produtos que estão no carrinho
    for produto in carrinho:
        print(produto)

adicionar_produto() 


    
        






#   {"id": 1, "nome": "Camiseta", "descricao": "Camiseta de algodão confortável", "preco": 29.90},
#   {"id": 2, "nome": "Calça Jeans", "descricao": "Calça jeans azul escura", "preco": 99.90},
#   {"id": 3, "nome": "Tênis Esportivo", "descricao": "Tênis para corrida e caminhada", "preco": 149.90},