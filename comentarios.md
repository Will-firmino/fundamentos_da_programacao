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