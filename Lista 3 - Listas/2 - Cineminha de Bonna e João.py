# Problem Statement

# Bonna e João adoram assistir filmes juntos nos finais de semana. 
# Todos os meses, eles escolhem um gênero diferente para assistirem durante o mês. 
# Para o mês de agosto, o gênero escolhido foi o de terror/suspense, e eles combinaram que, cada semana, um deles apresenta uma lista com sugestão de filmes e as notas que eles possuem no fórum de críticas a filmes dos alunos do CIn, o CInema.com.br. 
# Para melhor visualização, Bonna e João contam com a sua ajuda para colocar as listas em ordem decrescente em relação as notas.
# OBS: Está proibido o uso de funções de ordenação de listas. Além disso, não haverá casos de empate nas notas.

# Dica: Segue abaixo dois vídeos explicando a lógica do método de ordenação por flutuação (ou bubble sort):

# Bubble-sort dance
# Bubble-sort simulação
# Input

# O primeiro input será o nome de quem está enviando as listas com os filmes, sendo Bonna ou João:

# nome = Nome do dono da lista.

# O segundo, será a quantidade de filmes e notas que as listas possuem:

# quantidade = Quantidade de filmes e notas.

# Após isso, seu programa irá receber os nomes e as notas respectivamente, no formato:

# {nome_filme} - {nota_filme}

# OBS: você deve usar .split() para tratar as entradas

# Output

# Caso a dona da lista seja Bonna, você deverá printar a mensagem:

# "Os filmes sugeridos por Bonna são:”

# Caso o dono da lista seja João, você deverá printar a mensagem:

# "Os filmes sugeridos por João são:”

# Após isso, você deverá printar a lista com os filmes e as notas no seguinte formato:

# {filme} - {nota}

# Examples

# Case: 1

# Input

# João
# 5
# Psicose - 4.6
# Invocação do Mal 2 - 3.6
# Constantine - 4.4
# Invasão Zumbi - 3.7
# Um Lugar Silencioso - 4.3

# Output

# Os filmes sugeridos por João são:
# Psicose - 4.6
# Constantine - 4.4
# Um Lugar Silencioso - 4.3
# Invasão Zumbi - 3.7
# Invocação do Mal 2 - 3.6

# Case: 2

# Input

# Bonna
# 7
# Invocação do Mal 2 - 3.6
# Constantine - 4.4
# O Iluminado - 4.5
# O Homem nas Trevas - 3.5
# Sobrenatural: Capitulo 2 - 2.6
# Os Pássaros - 4.8
# Psicopata Americano - 3.9

# Output

# Os filmes sugeridos por Bonna são:
# Os Pássaros - 4.8
# O Iluminado - 4.5
# Constantine - 4.4
# Psicopata Americano - 3.9
# Invocação do Mal 2 - 3.6
# O Homem nas Trevas - 3.5
# Sobrenatural: Capitulo 2 - 2.6

nome = input()
quantidade = int(input())
filmes_notas = []

#separei o nome do filme e a nota 

for i in range(quantidade):
	filme = input().split(' - ')
	filmes_notas.append(filme)

#bubble sort
size = len(filmes_notas)
for i in range(size - 1, 0, -1):
	for j in range (size - 1):
		if filmes_notas[j][1] < filmes_notas[j + 1][1]:
			filmes_notas[j], filmes_notas[j + 1] = filmes_notas[j + 1], filmes_notas[j]

print(f'Os filmes sugeridos por {nome} são:')

for i in range(len(filmes_notas)):
		print(f'{filmes_notas[i][0]} - {filmes_notas[i][1]}')
