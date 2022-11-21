# Problem Statement

# Clank, nosso robô preferido da saga de jogos Ratchet & Clank está desatualizado e precisa de um programador especializado em Python para atualizá-lo!

# Enquanto estava em uma de suas aventuras pela Solana Galaxy, um dos vilões, Doctor Nefarious danificou o Clank e fez com que ele perdesse a capacidade de avaliar as estruturas de sentenças matemáticas, isto é, ele não consegue determinar se a quantidade de parênteses está no mínimo adequada para ser uma sentença verídica.

# Sua tarefa será consertar o Clank criando um código que resolva o problema supramencionado.

# Para cada entrada, você deverá determinar se a quantidade de parênteses ‘(’ é igual a quantidade de parênteses ‘)’, não importa se a sentença matemática está escrita erroneamente, como por exemplo: “)(2 + 3)) - 2”, no caso, estamos nos preocupando somente com a quantidade.

# Obs(1).: você deverá usar recursão para verificar as equações;

# Obs(2).: não poderá usar funções que retornam o index de um elemento de um string, como por exemplo: find() e index(); e nem funções que contam as quantidades de ocorrências em listas ou strings, como count()

# Obs(3).: não poderá ser usado loops dentro das funções que forem criadas;

# Input

# Para avaliar a capacidade do seu código, Clank receberá um inteiro N que indica a quantidade de sentenças que serão recebidas.

# N

# Em seguida, você receberá N sentenças matemáticas;

# exp1

# exp2

# ...

# expN

# Output

# Para cada entrada, você deverá retornar se há uma igualdade na quantidade de parênteses, o código deverá apresentar as seguintes respostas:

# → Se a quantidade de parênteses '(' for igual a quantidade de parênteses ')':

# “Essa sentença está com os parênteses balanceados, HOORAY!”

# →Se a quantidade de parênteses '(' for maior que a quantidade de parênteses ')':

# ”A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la”

# →Se a quantidade de parênteses ')' for maior que a quantidade de parênteses '(':

# ”A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la”

# Obs.: para printar aspas dentro da função print, você pode digitar ** (contra-barra) + ' (aspa) junto ou colocar como aspas mais externas as aspas duplas "

# Examples

# Case: 1

# Input

# 5
# (x + 14)/12
# (x*24))21()
# (x**6(12+y))
# )(23+xy)(
# h+(f*3(-13*x)

# Output

# Essa sentença está com os parênteses balanceados, HOORAY!
# A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la
# Essa sentença está com os parênteses balanceados, HOORAY!
# Essa sentença está com os parênteses balanceados, HOORAY!
# A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la

def verificacao_parenteses(entrada, char): 
	if entrada == '':  
		return 0
		else: 
		if entrada[0]== char:
			return 1 + verificacao_parenteses( entrada[1:], char )
		
		else:
			return 0 + verificacao_parenteses( entrada[1:], char )


n = int(input())
sentencas = []
for i in range(n):
	entrada = input()
	sentencas.append(entrada)

for sentenca in sentencas:
	a = verificacao_parenteses(sentenca, '(')
	b = verificacao_parenteses(sentenca, ')')
	if a == b:
		print(f'Essa sentença está com os parênteses balanceados, HOORAY!')
	elif a>b:
		print(f'A quantidade de parênteses \'(\' está maior que a de \')\', vamos descartá-la')
	elif b>a:
		print(f'A quantidade de parênteses \')\' está maior que a de \'(\', vamos descartá-la')
