# Problem Statement

# Em Stranger Things, Dustin e seus melhores amigos Mike, Lucas, Will Max e Steve se envolvem em uma trama sobrenatural na pacata cidade de Hawkins, enfrentando criaturas de uma dimensão “invertida”. 
# Na terceira temporada, Dustin foi ao Acampamento Know Where e conheceu uma garota chamada Suzie, que se tornou sua namorada.
# Enquanto o casal teve que se separar quando o acampamento terminou, eles concordaram em continuar se comunicando.
# Suzie possuía certas habilidades com hacking, em determinado momento da série, Dustin precisava imensamente da ajuda de “Suzie-Linda” para poder decifrar a senha de uma das portas do Laboratório Secreto Russo onde estava infiltrado, Suzie não perdeu tempo para ajudar seu Dustinzinho, mas para isso ela precisará da sua ajuda, estudante do maior centro de informática do planeta terra e do mundo invertido.

# O problema consiste em, dada uma matriz NxN você deverá descobrir qual será o par com maior soma para cada sentido da matriz horizontal (todas as linhas), vertical (todas as colunas) e diagonal principal (
# clique aqui para saber sobre as diagonais principais
# ). Por exemplo:
# Dada essa matriz, temos que:

# Você deve analisar todas as linhas dessa matriz e formar os pares como informado na figura acima. Você deve checar todos os pares da primeira linha, depois da segunda linha e assim por diante. No exemplo acima temos que o par (5, 6) [nesta ordem] → 5 + 6 = 11, possui a maior soma dentre todos os outros pares mapeando apenas as linhas.

# Você deve analisar todas as colunas, checando todos os pares da primeira coluna para só assim checar os pares da segunda e assim por diante. Portanto, temos que o par (6, 4)[nesta ordem] → 6 + 4 = 10, possui a maior soma dentre os todos pares formados olhando apenas para as colunas.

# Atenção à ordem com que os pares das linhas e colunas devem ser lidos

# Você deve analisar a diagonal principal. Nela, temos que o par (5,3)** [nesta ordem]** → 5 + 3 = 8, possui a maior soma dentro dessa diagonal.

# OBS: [Nesta ordem] Mapear os pares da matriz sempre começando de cima para baixo.

# Depois de mapear todos os pares que possuem a maior soma de cada sentido separadamente, temos que a senha será formada pela concatenação desses pares, ou seja, dado os pares do exemplo acima: (5,6) - (6,4) - (5,3), iremos ter uma senha neste formato: 566453.

# OBS:

# A senha deve ser sempre concatenada seguindo a ordem:

# (par da linha+par da coluna+par da diagonal principal).

# O mapeamento dos pares deve ser feito de acordo como está informado na figura, ou seja, checar o elemento N1 + N1+1, N2 + N2+1 etc.

# Você deverá manter o primeiro par com a maior soma, ou seja, caso tenha um par com soma igual a um par já encontrado, você deverá manter o par anterior.

# Input

# Você receberá um número inteiro N >= 2, que representará o tamanho da sua matriz NxN:

# N

# Logo após, você receberá N entradas que representaram a sua matriz:

# n1 n2 …. N

# .

# .

# .

# n4 n5 …. N → Os números que compõem a matriz estão no intervalo de [0-9]

# Output

# A saída consiste em uma mensagem onde foi decifrado a senha da porta secreta e obviamente a senha formata:

# Falei que era fácil Dustinzinho...
# Pegando todas os números que formam as combinações dos pares de cada sentido temos...
# Password: {senha}

# Observe que existe uma quebra de linha para cada mensagem

# Examples

# Case: 1

# Input

# 4
# 2 4 5 8
# 3 8 5 9
# 1 2 3 4
# 5 8 9 7

# Output

# Falei que era fácil Dustinzinho...
# Pegando todas os números que formam as combinações dos pares de cada sentido temos...
# Password: 898983

# Case: 2

# Input

# 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# Output

# Falei que era fácil Dustinzinho...
# Pegando todas os números que formam as combinações dos pares de cada sentido temos...
# Password: 455545

n = int(input())
matriz =[]

for i in range(n):
	linha = input().split(' ')
	matriz.append(linha)

soma_linhas = []
pares_linhas = []

for linha in matriz:
	somas = []
	pares = []
	for i in range(len(linha)-1):
		soma = int(int(linha[i])+int(linha[i+1]))
		par = [linha[i], linha[i+1]]
		somas.append(soma)
		pares.append(par)

	index = somas.index(max(somas))
	soma_linhas.append(somas[index])
	pares_linhas.append(pares[index])

index = soma_linhas.index(max(soma_linhas))
par_linha_max = pares_linhas[index]

#coluna

colunas = []
for i in range(len(matriz)):
	coluna = []
	for j in range(len(matriz)):
		numero = matriz[j][i]
		coluna.append(numero)
	colunas.append(coluna)

soma_colunas = []
pares_colunas = []

for coluna in colunas:
	somas = []
	pares = []
	for i in range(len(coluna)-1):
		soma = int(int(coluna[i])+int(coluna[i+1]))
		par = [coluna[i],coluna[i+1]]
		somas.append(soma)
		pares.append(par)
	index = somas.index(max(somas))
	soma_colunas.append(somas[index])
	pares_colunas.append(pares[index])

index = soma_colunas.index(max(soma_colunas))
par_coluna_max = pares_colunas[index]

#diagonal
diagonal = []
soma_diagonal = []
pares_diagonal = []
for i in range(len(matriz)):
	numero = matriz[i][i]
	diagonal.append(numero)

somas = []
pares = []

for i in range(len(diagonal)-1):
	soma = int(int(diagonal[i])+int(diagonal[i+1]))
	par = [diagonal[i], diagonal[i+1]]
	somas.append(soma)
	pares.append(par)

	index = somas.index(max(somas))
	soma_diagonal.append(somas[index])
	pares_diagonal.append(pares[index])

index = soma_diagonal.index(max(soma_diagonal))
par_diagonal_max = pares_diagonal[index]

senha = par_linha_max[0]+par_linha_max[1]+par_coluna_max[0]+par_coluna_max[1]+par_diagonal_max[0]+par_diagonal_max[1]

print(f'Falei que era fácil Dustinzinho...')
print(f'Pegando todas os números que formam as combinações dos pares de cada sentido temos...')
print(f'Password: {senha}')


