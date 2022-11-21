# Problem Statement

# Jiro Horikoshi, engenheiro de aviões, gasta grande parte do seu tempo trabalhando com cálculos matemáticos, e muitos desses cálculos são operações envolvendo matrizes. 

# Em busca de diminuir a quantidade de cálculos que ele precisa fazer à mão e salvar tempo para que ele trabalhe em outras áreas, assim como reduzir possíveis erros de calculo, Jiro quer sua ajuda para construir um programa de uma calculadora de matrizes, tendo as operações de soma, subtração e multiplicação de matrizes assim como multiplicação de uma matriz por um escalar. 

# A sua calculadora precisa funcionar apenas com matrizes quadradas e mesmo tamanho.

# Input

# A primeira linha de entrada é um inteiro que determina o tamanho das duas matrizes que vão ser usadas no programa

# N

# Em seguida, você vai receber a matriz quadrada de tamanho N m1, separadas por espaços

# m1_00 m1_01 . . . m1_0N
# m1_10 m1_11 . . . m1_1N
# . . .
# m1_N0 m1_N1 . . . m1_NN

# Depois, você vai receber a matriz quadrada de tamanho N m2, no mesmo formato

# m2_00 m2_01 . . . m2_0N
# m2_10 m2_11 . . . m2_1N
# . . .
# m2_N0 m2_N1 . . . m2_NN

# Após isso, você vai receber um inteiro representando a quantidade de operações que vão ser realizadas nas matrizes.

# qtd_op

# Em seguida, você vai receber qtd_op operações, se a operação for soma, subtração ou produto de matrizes (representadas por +, - e . respectivamente):

# mr = ma op mb

# onde mr (pode ter valor ‘m1’ ou ‘m2’) é a matriz que vai receber o resultado, ma e mb (pode ter valor ‘m1’ ou ‘m2’, podem ser matrizes diferentes ou iguais) são as matrizes que vão ser usadas na operação.

# Já se for uma multiplicação por escalar:

# mr = m * k

# ou

# mr = k * m

# onde k é o escalar (sempre um inteiro)

# Output

# A saída consiste em imprimir o resultado da última operação realizada, linha por linha e separando os valores com espaços:

# mr_00 mr_01 . . . mr_0N
# mr_10 mr_11 . . . mr_1N
# . . .
# mr_N0 mr_N1 . . . mr_NN

# Examples

# Case: 1

# Input

# 3
# 31 21 46
# 37 9 8
# 37 29 2
# 10 12 40
# 8 11 8
# 26 22 11
# 2
# m1 = m2 + m2
# m2 = m1 - m2

# Output

# 10 12 40
# 8 11 8
# 26 22 11

# Case: 2

# Input

# 3
# 2 6 2
# 5 2 5
# 4 9 1
# 8 6 8
# 3 7 7
# 6 2 8
# 4
# m2 = m1 + m2
# m2 = m1 * 2
# m1 = 3 * m2
# m2 = m1 . m2

# Output

# 504 504 432
# 480 948 300
# 684 612 648

def somar(m1, m2):
	matriz_soma = []
	for i in range(n):
		matriz_soma.append([])
		for j in range(n):
			soma = int(m1[i][j]) + int(m2[i][j])
			matriz_soma[i].append(soma)
	return matriz_soma

def subtrair(m1, m2):
	matriz_subtracao= []
	for i in range(n):
		matriz_subtracao.append([])
		for j in range(n):
			subtracao = int(m1[i][j]) - int(m2[i][j])
			matriz_subtracao[i].append(subtracao)
	return matriz_subtracao

def mult_escalar (m, escalar,):
	m_mult = []
	for i in range(n):
		linha = []
		for j in range(n):
			mult = escalar * int(m[i][j])
			linha.append(mult)
		m_mult.append(linha)
	return m_mult

def mult_matrizes(m1, m2):
	def getLinha(matriz, n):
		return [i for i in matriz[n]]  

	def getColuna(matriz, n):
		return [i[n] for i in matriz]

	m1lin = len(m2)
	m2col = len(m2[0])

	m_mult = []
	for i in range(m1lin): 
		linha = []
		for j in range(m2col):
			mult_matrizes = [int(x)*int(y) for x, y in zip(getLinha(m1, i), getColuna(m2, j))]
			linha.append(sum(mult_matrizes))
		m_mult.append(linha)

	return m_mult


n = int(input())
m1 =[]
m2 = []
escalar = 1

for i in range(n):
	linha = input().split(' ')
	m1.append(linha)
for i in range(n):
	linha = input().split(' ')
	m2.append(linha)

qtd_operacao = int(input())

operacoes = []
for op in range(qtd_operacao):
	linha = input().split(' ')
	operacoes.append(linha)

for i in range(qtd_operacao):
	m_r = operacoes[i][0]
	fator_1 = operacoes[i][2]
	operador = operacoes[i][3]
	fator_2 = operacoes[i][4]

	if fator_1 == 'm1':
		fator1 = m1
	elif fator_1 == 'm2':
		fator1 = m2
	else:
		escalar = int(fator_1)

	if fator_2 == 'm1':
		fator2 = m1
	elif fator_2 == 'm2':
		fator2 = m2
	else:
		escalar = int(fator_2)

	if operador == '+':
		mr = somar(fator1,fator2)
	elif operador == '-':
		mr = subtrair(fator1,fator2)
	elif operador == '.':
		mr = mult_matrizes(fator1, fator2)
	elif operador == '*':
		if fator_1 == 'm1' or fator_1 == 'm2':
			mr = mult_escalar(fator1,escalar)
		else:
			mr = mult_escalar(fator2,escalar)

	if m_r == 'm1': 
		m1 = mr
	else: 
		m2 = mr

for i in range(n):
	print(*mr[i])













