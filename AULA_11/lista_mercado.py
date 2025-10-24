despensa = ["arroz", "feijão", "óleo"]
item = input("➕ Digite o item que você quer verificar: ")
if item in despensa:
    print(f"✅ O item {item} já está disponível na despensa.")
else:
    print(f"❌ O item {item} precisa ser comprado.")
print(despensa)