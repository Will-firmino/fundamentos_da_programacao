usuario = {
    'nome': 'Marina', 
	'email': 'marina@email.com',
    'telefone': '21985653623'
}

# Tentando acessar a chave "telefone" com um valor padrão:
telefone = usuario.get('telefone', 'não informado')

# Mostra o resultado no console:
print(f"Nome: {usuario['nome']}")
# print(f'Telefone: {telefone}')
