# Criação de um dicionário vazio:
aluno = {}

# Pedir ao usuário para digitar as informações:
aluno['nome'] = input('Digite o nome do aluno: ')
aluno['idade'] = input('Digite a idade do aluno: ')
aluno['curso'] = input('Digite o curso do aluno: ')

# Imprime o dicionário completo:
print('\nDicionário completo: ')
print(aluno)

# Mostra apenas o nome e o curso:
print('\nInformações específicas: ')
print(f'Nome: {aluno["nome"]}') # Acessando a chave ele retorna o valor.
print(f'Curso: {aluno["curso"]}') 
