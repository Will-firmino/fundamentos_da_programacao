# Crie um programa que calcule o valor do frete com base na distância:
# Até 5km, R$5
# De 6km até 10Km, R$10
# Acima de 10km, exibir que a entrega não é feita.

distancia = 20
if distancia <= 5:
    print("💰 O valor do frete é de R$5.")
elif distancia <= 10:
    print("💰 O valor do frete é de R$10.")
else:
    print("😢 Infelizmente, não entregamos nesta distância.")

