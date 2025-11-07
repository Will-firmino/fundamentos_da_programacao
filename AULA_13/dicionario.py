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
print(f'📚 Catálogo atualizado: {catalogo_precos}')

# 4. For, in, .items(), iterar:
