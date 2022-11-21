# Problem Statement

# Para conseguir chegar ao único local que ainda não foi consumido pelos zumbis e pelas criaturas sobrenaturais, você e seus amigos nerds terão que embarcar em uma desafiadora aventura pela cidade do Recife, indo em rumo ao Centro Imbatível de Normais (CIN). Porém, para conseguir realizar o percurso completo vocês precisarão preparar as suas mochilas com tudo que é necessário para a sobrevivência do grupo.

# Cada mochila pertence a uma pessoa diferente, elas podem ter tamanhos diferentes ou iguais e TODAS já começam com dois itens essenciais para a expedição: Uma “Lanterna” e um “Omega 3 da top therm”, ou seja uma mochila de tamanho 4 ela já será iniciada com menos 2 espaços com os dois itens contidos nela. Durante o trajeto itens que estão dentro da mochila podem ser utilizados (removidos da mochila) e itens podem ser encontrados no meio do caminho e guardados na mochila.

# Input

# A primeira parte da entrada é composta por várias linhas de código, contendo: Quantidade M de mochilas, Uma linha com o nome dos amigos responsável por cada mochila, M linhas com o tamanho de cada mochila, Número N de itens que serão adicionados seguidos de N nome de itens e N números representando a mochila que o item será adicionado:

# quantidade M de mochilas

# nome_1 nome_2 nome_3

# tamanho_mochila_0

# tamanho_mochila_1

# …

# tamanho_mochila_M

# quantidade N de itens

# nome_item_1

# mochila_item_1

# nome_item_2

# mochila_item_2

# …

# nome_item_N

# mochila_item_N

# PS1: As mochilas começam no índice 0, ou seja se são 3 mochilas será: mochila 0, mochila 1 e mochila 2.

# PS2: Se a mochila estiver cheia ao tentar adicionar um item mostrar “Mochila cheia. Não vai dar para levar.” na tela e ignorar esse item.

# PS3: Toda mochila terá tamanho maior ou igual a 2.

# PS4: o primeiro amigo é responsável pela mochila 0, o segundo pela mochila 1 e assim em diante, ou seja a quantidade de amigos sempre será igual a quantidade de mochilas.

# A segunda parte da entrada consiste em várias linhas de código compostas por: X ações, que podem ser válidas ou inválidas, e em seguida as entradas da ação.

# ação_1

# item_ação_1

# mochila_item_ação_1

# ação_2

# item_ação_2

# mochila_item_ação_2

# ação_3

# ação_X

# …

# ação_final

# PS: As três ações possíveis são:

# “Tirar da mochila” → consiste em você fazer a retirada de um item X de dentro de uma mochila Y específica que caso o item não esteja presente na mochila informar que “Você não tem X na mochila Y.”. Se a ação for bem sucedida informar que “X usado com sucesso da mochila Y.”.
# “Guardar na mochila” → consiste em você guardar um item X dentro de uma mochila Y específica que caso a mochila esteja cheia informar que “Mochila Y cheia!”. Se a ação for bem sucedida informar que “X adicionado na mochila Y.”.
# “CHEGAMOS NO CIN!” → serve apenas para sinalizar a finalização das ações e a conclusão da expedição.
# QUALQUER OUTRA AÇÃO deve mostrar “Ação inválida.” na tela!

# DICA: Tentem utilizar uma lista de listas para armazenar as mochilas e os conteúdos de dentro delas. Ex: [[a, b], [a, b]]

# Output

# Além das saídas de “mochila cheia” da primeira parte do input e as saídas das ações deve ser mostrado no final “Mochila de {nome} chegou assim:” e os itens que tem dentro da sua mochila na ordem.

# mochila_fulano

# item_1_mochila_fulano

# item_2_mochila_fulano

# item_3_mochila_fulano

# mochila_cicrano

# item_1_mochila_cicrano

# item_2_mochila_cicrano

# item_3_mochila_cicrano

# …

# PS1: Se a mochila estiver vazia mostrar normalmente o output.

# PS2: “{nome}” é o nome da pessoa responsável pela mochila em questão.

# Examples

# Case: 1

# Input

# 3
# Pedro João Clara
# 4
# 5
# 6
# 5
# Remédios
# 0
# Pão
# 0
# Livro
# 0
# Fruta
# 1
# Inseticida
# 2
# Tirar da mochila
# Pão
# 0
# Tirar da mochila
# Prova de P1/IP
# 0
# Jogar mochila fora
# Guardar na mochila
# Bolinho bacia
# 0
# CHEGAMOS NO CIN!

# Output

# Mochila cheia. Não vai dar para levar.
# Pão usado com sucesso da mochila 0.
# Você não tem Prova de P1/IP na mochila 0.
# Ação inválida.
# Bolinho bacia adicionado na mochila 0.
# Mochila de Pedro chegou assim:
# Lanterna
# Omega 3 da top therm
# Remédios
# Bolinho bacia
# Mochila de João chegou assim:
# Lanterna
# Omega 3 da top therm
# Fruta
# Mochila de Clara chegou assim:
# Lanterna
# Omega 3 da top therm
# Inseticida

# Case: 2

# Input

# 3
# Alan Felipe Carol
# 4
# 5
# 6
# 0
# Tirar da mochila
# Lanterna
# 0
# Tirar da mochila
# Omega 3 da top therm
# 0
# CHEGAMOS NO CIN!

# Output

# Lanterna usado com sucesso da mochila 0.
# Omega 3 da top therm usado com sucesso da mochila 0.
# Mochila de Alan chegou assim:
# Mochila de Felipe chegou assim:
# Lanterna
# Omega 3 da top therm
# Mochila de Carol chegou assim:
# Lanterna
# Omega 3 da top therm

quantidade = int(input())
nomes = input().split(" ")
tamanho_mochila = []
itens_mochila = []

for i in range(quantidade):
	tamanho= int(input())
	tamanho_mochila.append(tamanho)
	itens_mochila.append(["Lanterna","Omega 3 da top therm"])

itens = int(input())
for i in range (itens):
	nome_item = input()
	numero_mochila = int(input())
	if (len(itens_mochila[numero_mochila]) < (tamanho_mochila[numero_mochila])):
		itens_mochila[numero_mochila].append(nome_item)
	else: 
		print("Mochila cheia. Não vai dar para levar.")

acao = ' '

while (acao != "CHEGAMOS NO CIN!") :
	acao = input()
	if (acao == "Tirar da mochila") :
		item_acao = input()
		numero_mochila = int(input())
		if (item_acao in itens_mochila[numero_mochila]):
			print(f'{item_acao} usado com sucesso da mochila {numero_mochila}.')
			itens_mochila[numero_mochila].remove(item_acao)
		else:
			print(f'Você não tem {item_acao} na mochila {numero_mochila}.')
	elif (acao == "Guardar na mochila") :
		item_acao = input()
		numero_mochila = int(input())
		if len(itens_mochila[numero_mochila]) >= tamanho_mochila[numero_mochila]:
			print(f'Mochila {numero_mochila} cheia!')
		else:
			print(f'{item_acao} adicionado na mochila {numero_mochila}.')
			itens_mochila[numero_mochila].append(item_acao)
	elif (acao == "CHEGAMOS NO CIN!"):
		pass
	else:
		print("Ação inválida.")

for i in range (len(itens_mochila)):
		print(f'Mochila de {nomes[i]} chegou assim:')
		for item in itens_mochila[i]:
			print(item)

