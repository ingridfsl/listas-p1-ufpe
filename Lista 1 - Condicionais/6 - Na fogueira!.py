# Problem Statement

# Bruna e Frej organizaram no São João uma viagem com os amigos para Gravatá. O grupo passaria de quinta a domingo em uma casa, além de que no sábado iriam para a festa Carvalheira. 

# Todos estavam muito animados para o dia 25/06 pois iria tocar Jorge e Mateus, Xand Avião, Felipe Amorim e muito mais...

# Mas como a cidade estava um caos de trânsito e super lotação, nenhum deles queria ir dirigindo. 

# Como Bruna e Frej são os donos da casa e são muito inteligentes, eles fizeram uma competição com os outros 3 amigos (Artur, Rodrigo e Lucas) para saber quem iria dirigindo para o show.

# Os três começam com zero pontos e sua pontuação aumenta sempre que eles cometem um erro. Ou seja, VENCE AQUELE COM A MENOR PONTUAÇÃO.

# Em casos de empate, vence o jogador com o nome lexicograficamente menor e a ordem dos nomes pode mudar.

# Por mais que Bruna e Frej sejam muito espertos, eles querem ajuda em como organizar a ordem desses amigos nesse torneio do São João 2022, por isso chamaram você! Determine o primeiro, segundo e terceiro lugar, nessa ordem, dado os nomes e pontuações dos amigos em cada partida.

# Obs: não use max(), min() ou outras funções externas semelhantes. Não use funções externas para ordenação.

# Input

# A entrada consiste de seis linhas, contendo os nomes e pontuações finais de cada competidor.

# Nome e pontuação (inteiro) do primeiro amigo:

# nome_1

# pontuação_1

# Nome e pontuação (inteiro) do segundo amigo:

# nome_2

# pontuação_2

# Nome e pontuação (inteiro) do terceiro amigo:

# nome_3

# pontuação_3

# Output

# A saída consiste em três linhas, contendo os pares de nome e pontuação de cada amigo, em ordem do melhor candidato para o pior, com os critérios descritos no enunciado.

# nome e pontuação do primeiro colocado

# nome_primeiro pontuação_primeiro

# nome e pontuação do segundo colocado

# nome_segundo pontuação_segundo

# nome e pontuação do terceiro colocado

# nome_terceiro pontuação_terceiro

# Examples

# Case: 1

# Input

# Rodrigo
# 3
# Lucas
# 4
# Artur
# 1

# Output

# Artur 1
# Rodrigo 3
# Lucas 4

# Case: 2

# Input

# Artur
# 10
# Lucas
# 2
# Rodrigo
# 5

# Output

# Lucas 2
# Rodrigo 5
# Artur 10


n1 = input()
p1 = int(input())
n2 = input()
p2 = int(input())
n3 = input()
p3 = int(input())

if (p1< p2 < p3):
	print(f'{n1} {p1}')
	print(f'{n2} {p2}')
	print(f'{n3} {p3}')
elif (p1< p3 < p2):
	print(f'{n1} {p1}')
	print(f'{n3} {p3}')
	print(f'{n2} {p2}')
elif (p1< p2 == p3):
	if (n2 < n3):
		print(f'{n1} {p1}')
		print(f'{n2} {p2}')
		print(f'{n3} {p3}')
	elif (n2 > n3):
		print(f'{n1} {p1}')
		print(f'{n3} {p3}')
		print(f'{n2} {p2}')
elif (p2 == p3 < p1):
	if (n2 < n3):
		print(f'{n2} {p2}')
		print(f'{n3} {p3}')
		print(f'{n1} {p1}')
	elif (n2 > n3):
		print(f'{n3} {p3}')
		print(f'{n2} {p2}')
		print(f'{n1} {p1}')

if (p2< p1 < p3):
	print(f'{n2} {p2}')
	print(f'{n1} {p1}')
	print(f'{n3} {p3}')
elif (p2< p3 < p1):
	print(f'{n2} {p2}')
	print(f'{n3} {p3}')
	print(f'{n1} {p1}')
elif (p2< p1 == p3):
	if (n1 < n3):
		print(f'{n2} {p2}')
		print(f'{n1} {p1}')
		print(f'{n3} {p3}')
	elif (n1 > n3):
		print(f'{n2} {p2}')
		print(f'{n3} {p3}')
		print(f'{n1} {p1}')
elif (p1 == p3 < p2):
	if (n1 < n3):
		print(f'{n1} {p1}')
		print(f'{n3} {p3}')
		print(f'{n2} {p2}')
	elif (n1 > n3):
		print(f'{n3} {p3}')
		print(f'{n1} {p1}')
		print(f'{n2} {p2}')

if (p3< p1 < p2):
	print(f'{n3} {p3}')
	print(f'{n1} {p1}')
	print(f'{n2} {p2}')
elif (p3< p2 < p1):
	print(f'{n3} {p3}')
	print(f'{n2} {p2}')
	print(f'{n1} {p1}')
elif (p3< p1 == p2):
	if (n1 < n2):
		print(f'{n3} {p3}')
		print(f'{n1} {p1}')
		print(f'{n3} {p2}')
	elif (n1 > n2):
		print(f'{n3} {p3}')
		print(f'{n2} {p2}')
		print(f'{n1} {p1}')
elif (p1 == p2 < p3):
	if (n1 < n2):
		print(f'{n1} {p1}')
		print(f'{n2} {p2}')
		print(f'{n3} {p3}')
	elif (n1 > n2):
		print(f'{n2} {p2}')
		print(f'{n1} {p1}')
		print(f'{n3} {p3}')

if (p1==p2==p3):
	if(n1 < n2 <n3):
		print(f'{n1} {p1}')
		print(f'{n2} {p2}')
		print(f'{n3} {p3}')
	 elif(n1 < n3 < n3):
		print(f'{n1} {p1}')
		print(f'{n3} {p3}')
		print(f'{n2} {p2}')
	 elif(n2 < n1 <n3):
		print(f'{n2} {p2}')
		print(f'{n1} {p1}')
		print(f'{n3} {p3}')
	 elif(n2 < n3 <n1):
		print(f'{n2} {p2}')
		print(f'{n3} {p3}')
		print(f'{n2} {p2}')
	 elif(n3 < n1 <n2):
		print(f'{n3} {p3}')
		print(f'{n1} {p1}')
		print(f'{n2} {p2}')
	 elif(n3 < n2 <n1):
		print(f'{n3} {p3}')
		print(f'{n2} {p2}')
		print(f'{n1} {p1}')
