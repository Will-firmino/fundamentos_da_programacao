# Desenvolva um módulo Python chamado `catalogo_produtos.py` que contenha uma função para exibir
# um catálogo de produtos disponíveis em uma loja online. 
# Cada produto deve ter um nome, descrição
# e preço. A função deve formatar a saída de maneira clara e organizada.
#   adicionar_produto(produtos, "Boné", "Boné esportivo ajustável", 39.90)
#   adicionar_produto(produtos, "Mochila", "Mochila resistente para uso diário", 89.90)
#   adicionar_produto(produtos, "Relógio", "Relógio digital à prova d'água", 199.90)


# Função responsável por exibir os produtos disponíveis no catálogo
def exibir_catalogo(produtos):  
    print("\n Catálogo de Produtos disponíveis: ")
    print("--------------------------------")
    for produto in produtos:
        print(f'ID: {produto["id"]}')
        print(f'Nome: {produto["nome"]}')
        print(f'Descrição: {produto["descricao"]}')
        print(f'Preço: {produto["preco"]}')
        print("--------------------------------")

produtos = [
    {"id": 1, "nome":"Boné", "descricao": "Boné esportivo ajustável", "preco": 39.90 },
    {"id": 2, "nome":"Mochila", "descricao": "Mochila resistente para uso diário", "preco": 89.90 },
    {"id": 3, "nome":"Relógio", "descricao": "Relógio digital à prova d'água", "preco": 199.90 }
    ]

print(f'ID: {[produtos][1]}')



exibir_catalogo(produtos)
