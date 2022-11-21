# Problem Statement

# No fim da 2ª temporada de Stranger Things, Eleven precisa fechar um portal para impedir que o Devorador de Mentes fuja do Mundo Invertido, e conta com que você, Steve, Lucas, Mike, Dustin e Max distraiam os Demodogs incendiando o centro do labirinto de túneis que estão abaixo da Fazenda do Merril e escapar dos Demodogs que irão persegui-los até a saída do labirinto.

# O problema é que está muito escuro e a turma se separou porque você se atrasou. Só um dos personagens ficou junto com você para te acompanhar. Para escapar do labirinto, você recebe uma indicação do pessoal que já conseguiu chegar no fim quanto a ordem que você deve seguir para conseguir escapar. “Sempre siga pela direita, caso não dê para andar pela direita, siga por baixo, depois cima e esquerda respectivamente, mas jamais volte para trás, ou seja, faça um movimento oposto ao que você está indo antes”.

# Essas foram as indicações, agora você deve juntar todo o seu conhecimento em computação e criar um código que mostre o passo-a-passo de como você e o seu parceiro conseguirão chegar no fim do túnel (ou não).

# O Demodog também está perseguindo vocês e se movimenta igual a você. O objetivo dele é passar pelo portal, mas se ele encontrar vocês no meio do caminho irá pegá-los. Eleven usou um poder mental e conseguiu projetar na sua mente um esboço do mapa, que é atualizado a cada passo seu e do Demodog até que algum dos dois passe.

# Input

# Você receberá o nome do personagem que está junto com você.

# Você receberá 8 linhas, as quais terão as informações de cada parte do mapa, que está criptografado, no qual você deve primeiramente encontrar as posições onde cada um está. O ponto que está com 'p' são vocês, 'd' significa o Demodog, e 'o' a saída do subsolo. '|' e '_' são paredes e os ' . ' representam áreas livres (que podem ser um caminho). Para isso, você deve, assim que receber a linha, convertê-la para lista e adicioná-la dentro de outra lista para, assim, criar uma matriz.

# Output

# As saídas deverão ser "fotos" do mapa após a sua movimentação e a do Demodog (mas quando você chegar no portal o Demodog não irá mais se mover).

# No fim, você deve exibir a mensagem final que poderá ser das seguintes formas:

# 1 - Se vocês conseguiram passar pelo portal antes do Demodog, a seguinte mensagem deve ser exibida:

# "UFA!!! Você e {player} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal."

# 2 - Se vocês não conseguiram chegar antes do Demodog, vocês deverão exibir a mensagem:

# "Ah não, você e {player} não foram rápidos o bastante e o demodog passou pelo portal."

# 3 - Se vocês forem pegos pelo Demodog, a seguinte mensagem deve ser exibida:

# "Ah não, você e {player} foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos."

# Dica: Você pode organizar o mapa em uma matriz (lista de listas) e imprimir uma linha com “print(*linha)”.

# OBS:: A pessoa tentando escapar não vai fazer o movimento se esse movimento colocá-la em cima do Demodog

# Examples

# Case: 1

# Input

# Max
# ___________
# |d|.....|.o
# |.|.....|.|
# p.|.....|.|
# |.|.....|.|
# |.|_____|.|
# |.........|
# |_________|

# Output

# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | d | . . . . . | . |
# . p | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . d | . . . . . | . |
# | p | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | d | . . . . . | . |
# | p | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | d | _ _ _ _ _ | . |
# | p . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | d p . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . d p . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . d p . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . d p . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . d p . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . . d p . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . . . d p . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . d p |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | p |
# | . . . . . . . . d |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | p |
# | . | _ _ _ _ _ | d |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | p |
# | . | . . . . . | d |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | p |
# . . | . . . . . | d |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | p o
# | . | . . . . . | d |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | d |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# UFA!!! Você e Max conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.

# Case: 2

# Input

# Dustin
# ___________
# |d|.....|.o
# |.|.....|.|
# p.|.....|.|
# |.|.....|.|
# |.|_____|.|
# |.....|...|
# |_________|

# Output

# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | d | . . . . . | . |
# . p | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . . | . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . d | . . . . . | . |
# | p | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . . | . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | d | . . . . . | . |
# | p | _ _ _ _ _ | . |
# | . . . . . | . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | d | _ _ _ _ _ | . |
# | p . . . . | . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | d p . . . | . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . d p . . | . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . d p . | . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . d p | . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . . . . . | . o
# | . | . . . . . | . |
# . . | . . . . . | . |
# | . | . . . . . | . |
# | . | _ _ _ _ _ | . |
# | . . . . d | . . . |
# | _ _ _ _ _ _ _ _ _ |
# Ah não, você e Dustin foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos.

# Case: 3

# Input

# Lucas
# ___________
# |d|.__|...o
# |.||....|.|
# p.||.|__|_|
# |.||......|
# |.|_____|.|
# |.........|
# |_________|

# Output

# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | d | | . . . . | . |
# . p | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . d | | . | _ _ | _ |
# | p | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | d | | . . . . . . |
# | p | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | d | _ _ _ _ _ | . |
# | p . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | d p . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . d p . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . d p . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . d p . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . d p . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . d p . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . d p . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . d p |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | p |
# | . . . . . . . . d |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . p |
# | . | _ _ _ _ _ | d |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . p d |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . p d . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . p d . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . p d . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | p d . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . . . | . |
# . . | | p | _ _ | _ |
# | . | | d . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | p . . . | . |
# . . | | d | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | d p . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . d p . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . . . o
# | . | | . . d p | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | p . . o
# | . | | . . . d | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | d p . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . d p o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# _ _ _ _ _ _ _ _ _ _ _
# | . | . _ _ | . d . o
# | . | | . . . . | . |
# . . | | . | _ _ | _ |
# | . | | . . . . . . |
# | . | _ _ _ _ _ | . |
# | . . . . . . . . . |
# | _ _ _ _ _ _ _ _ _ |
# UFA!!! Você e Lucas conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.

jogador = input()
mapa = []

for i in range(8):
	linha = list(input())
	mapa.append(linha)

# posições de p, d e o
	for y in range(len(mapa)):
		for x in range(len(mapa[y])):
			if mapa[y][x] == 'p':
				posicao_p = [y,x]
			if mapa[y][x] == 'd':
				posicao_d = [y,x]
			if mapa[y][x] == 'o':
				posicao_o = [y,x]

posicao_anterior_p = None
posicao_anterior_d = None

while (posicao_p !=posicao_d and posicao_p!=posicao_o and posicao_d!=posicao_o):
# movendo p 
# para direita
	y = posicao_p[0]
	x = posicao_p[1]
	if (mapa[y][x+1] == '.' and  posicao_anterior_p!=[y,x+1]):
		mapa[y][x] = '.'
		mapa[y][x+1] = 'p'
		x=x+1
		y=y
	elif (mapa[y][x+1] == 'o'):
		mapa[y][x] = '.'
		for linha in mapa:
			print(*linha)
		print(f'UFA!!! Você e {jogador} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
		break

# para baixo
	elif (mapa[y+1][x] == '.' and posicao_anterior_p!=[y+1,x]):
		mapa[y][x] = '.'
		mapa[y+1][x] = 'p'
		x=x
		y=y+1
	elif (mapa[y+1][x] == 'o'):
		mapa[y][x] = '.'
		for linha in mapa:
			print(*linha)
		print(f'UFA!!! Você e {jogador} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
		break

# para cima
	elif (mapa[y-1][x] == '.' and  posicao_anterior_p!=[y-1,x]):
		mapa[y][x] = '.'
		mapa[y-1][x] = 'p'
		x=x
		y=y-1
	elif (mapa[y-1][x] == 'o'):
		mapa[y][x] = '.'
		for linha in mapa:
			print(*linha)
		print(f'UFA!!! Você e {jogador} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
		break

# para esquerda
	elif (mapa[y][x-1] == '.' and  posicao_anterior_p !=[y,x-1]):
		mapa[y][x] = '.'
		mapa[y][x-1] = 'p'
		x=x-1
		y=y
	elif (mapa[y][x-1] == 'o'):
		mapa[y][x] = '.'
		for linha in mapa:
			print(*linha)
		print(f'UFA!!! Você e {jogador} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
		break

# movimento d
# para direita

	y = posicao_d[0]
	x = posicao_d[1]
	if (mapa[y][x+1] == '.'or mapa[y][x+1] == 'p') and (posicao_anterior_d != [y,x+1]):
		mapa[y][x] = '.'
		mapa[y][x+1] = 'd'
		x=x+1
		y=y
	elif (mapa[y][x+1] == 'o'):
		mapa[y][x] = '.'
		for linha in mapa:
			print(*linha)
		print(f'Ah não, você e {jogador} não foram rápidos o bastante e o demodog passou pelo portal.')
		break

# para baixo
	elif (mapa[y+1][x] == '.' or mapa[y+1][x] == 'p') and  (posicao_anterior_d  != [y+1,x]):
		mapa[y][x] = '.'
		mapa[y+1][x] = 'd'
		x=x
		y=y+1
	elif (mapa[y+1][x] == 'o'):
		mapa[y][x] = '.'
		for linha in mapa:
			print(*linha)
		print(f'Ah não, você e {jogador} não foram rápidos o bastante e o demodog passou pelo portal.')
		break

# para cima
	elif (mapa[y-1][x] == '.' or mapa[y-1][x] == 'p') and (posicao_anterior_d  != [y-1,x]):
		mapa[y][x] = '.'
		mapa[y-1][x] = 'd'
		x=x
		y=y-1
	elif (mapa[y-1][x] == 'o'):
		mapa[y][x] = '.'
		for linha in mapa:
			print(*linha)
		print(f'Ah não, você e {jogador} não foram rápidos o bastante e o demodog passou pelo portal.')
		break

# para esquerda
	elif (mapa[y][x-1] == '.' or mapa[y][x-1] == 'p') and (posicao_anterior_d != [y,x-1]):
		mapa[y][x] = '.'
		mapa[y][x-1] = 'd'
		x=x-1
		y=y
	elif (mapa[y][x-1] == 'o'):
		mapa[y][x] = '.'
		for linha in mapa:
			print(*linha)
		print(f'Ah não, você e {jogador} não foram rápidos o bastante e o demodog passou pelo portal.')
		break

	for linha in mapa:
		print(*linha)

	posicao_anterior_p = posicao_p
	posicao_anterior_d = posicao_d

# posições de p, d e o
	for y in range(len(mapa)):
		for x in range(len(mapa[y])):
			if mapa[y][x] == 'p':
				posicao_p = [y,x]
			if mapa[y][x] == 'd':
				posicao_d = [y,x]
			if mapa[y][x] == 'o':
				posicao_o = [y,x]

if posicao_d == posicao_p:
	print(f'Ah não, você e {jogador} foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos.')
