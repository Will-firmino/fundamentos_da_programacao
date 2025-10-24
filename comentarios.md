# Tipos de cases em python
1. [variáveis] -> Podem ser cammelCase ou snake_case;
2. [constantes] -> Python não tem constantes, utilizamos uma forma com o case UPPER. 

# Estruturas condicionais
1. [if] -> Se, é obrigatório e só pode usar uma vez.
2. [else] -> Senão, é opcional e só pode usar uma vez.
3. [elif] -> Senão se, é opcional e pode ser utilizado várias vezes.

# LAÇOS
1. [while] -> Executa um bloco de código enquanto uma condição for verdadeira.

=> Utilizado quando você não sabe exatamente quantas vezes irá ocorrer a repetição.
=> O while espera uma condição lógica ou True para começar a rodar.
=> break, continue e in são funcionalidades que podem ser utilizadas no contexto do while.

2. [for] -> É uma das estruturas de repetição mais utilizadas e poderosas da linguagem. Ele serve para iterar sobre os itens de qualquer sequència (lista, tupla, string).

=> `range()` - Utilizado para quando precisamos executar um bloco de código um número específico de vezes.
- `range(5)` -> Toda vez que a função range é utilizada, o número passado será exclusivo(não será executado).
- range(2, 11, 2), range(inicio, fim, passo):
 * inicio -> primeiro número (inclusivo)
 * fim -> último número-1 (exclusivo)
 * passo -> é a variação da sequência

# ESTRUTURAS DE DADOS
## LISTA - [list]
=> São coleções de elementos ``mutáveis``, ou seja, podem ser modificadas após a criação (adicionar, remover ou modificar elementos).
=> São flexíveis e podem conter qualquer tipo de dado, misturando-os conforme necessário. [HETEROGÊNEA].
### Operações da lista
1. .append() -> Adiciona um elemento ao final da lista.
2. .insert() -> Insere um elemento em uma posição específica.
3. .remove() -> Remove o primeiro elemento encontrado com o valor especificado.
4. .sort() -> Ordena os elementos da lista em ordem crescente.
5. .reverse() -> Reverte a ordem dos elementos da lista.


## TUPLA - [tuple]
=> São coleções `imutáveis`, o que significa que uma vez criada, não podem ser alteradas.
=> Tuplas podem conter qualquer tipo de dado. [HETEROGÊNEA].

### Operações comuns: 
1. acesso por índice
=> O índice começa em `0`. E é acessado utilizando os `colchetes`.

2. slicing
=> O slicing permite `extrair` partes de uma lista ou tupla, criando uma subestrutura a partir de um `intervalo` de índices.

3. operador in
=> Permite verificar se um elemento está presente em uma lista ou tupla. Retornar `True` se o elemento estiver na coleção ou `False` caso contrário.

31/10/2025
## DICIONÁRIO - [dict]
## CONJUNTO - [set]

