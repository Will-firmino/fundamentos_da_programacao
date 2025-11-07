# Declaração do dicionário.
catalogo_precos = {
    "notebook": 3599.90,
    "mouse": 149.90,
    "teclado": 499.50
}
# print("📚Catalogo da Loja: ", catalogo_precos)

# Operações:
# 1. Acessar o valor
# print(f'🖱️ Preço do mouse R$ {catalogo_precos["mouse"]:.2f}')

# 2. Adicionar itens:
catalogo_precos["headset"] = 299.55
# print(f'📚 Catálogo atualizado: {catalogo_precos}')

# 3. Alterar valores:
catalogo_precos["notebook"] = 3499.90
# print(f'📚 Catálogo atualizado: {catalogo_precos}')

# 4. For, in, .items(), iterar:
# for produto, preco in catalogo_precos.items():
#     print(f' 🤑 O produto {produto} custa R$ {preco:.2f}')

# 5. .pop(), remove e retorna o valor
# preco_headset = catalogo_precos.pop("headset")
# print(f' Produto removido: Headset, custava R${preco_headset}')
# print(catalogo_precos)

# 6. del, remove o item
# del catalogo_precos["teclado"]
# print(f'Catálogo após o uso do del: {catalogo_precos}')

# 7. obter as chaves
nome_dos_produtos = catalogo_precos.keys()
print(nome_dos_produtos)

# 8. obter os valores
preco_dos_produtos = catalogo_precos.values()
print(preco_dos_produtos)