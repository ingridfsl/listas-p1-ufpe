# Problem Statement

# Alien é uma série de filmes de terror e ficção científica com 7 filmes, que ficou muito popular nos anos 80 e teve filmes originais a partir de 2010. Iniciado em Alien: O 8° Passageiro, e indo até Alien Convent. Em Prometheus, 6° filme da série, inicia a história do primeiro contato dos humanos com os xenomorfos, onde ao chegar num planeta desconhecido, a procura de entender a origem da vida na terra, sem tomar os devidos cuidados, os tripulantes acabam sendo infectados ou mortos pelo xenomorfos, restando apenas a Doutora Elizabeth Shawn e o android David, e a sequência dessa história é contada no Alien Convent. Porém, algo que não é contado é que, na verdade, nesse intervalo de tempo, você conseguiu chegar no filme e participou dos eventos.

# Nesse tempo que você esteve com a dupla, uma situação muito inusitada aconteceu: vocês chegaram em um planeta que possuía as cápsulas com xenomorfos, e você ajudou o David a encontrar a sala onde estavam elas. Quando você chegou lá, percebeu que ao chegar em cada sala há sempre 3 portas, uma à esquerda, uma à direita e uma no meio, parecido como uma busca binária. Como na imagem a seguir:

# Nesse caso aqui você foi procurar a sala 19. Primeiro, analisamos a porta central (18) e nesse caso você foi para a direita, pois a porta da direita levam aos números acima de 18 (sem incluir 18), depois, analisando a porta do meio desse novo intervalo (27), você escolhe a porta da esquerda, onde ficam os números menores que 27 (sem incluir 27), em seguida, analisamos a porta central 21, e como nosso intervalo ainda tem tamanho maior que 1, vamos para a porta da esquerda, e até que enfim, o novo intervalo tem como porta do meio a 19, então, sua escolha é essa e você chega a ela seguindo essa rota: Direita -> Esquerda -> Esquerda -> Meio. Lembre-se: o meio de uma lista com um número par de elementos é o elemento central de maior índice. Em caso do tamanho da lista ser ímpar, o meio é o elemento central. Ex. O meio de [1,2,3,4] é 3, pois entre 2 e 3, 3 tem maior índice. Já em [1,2,3] o meio é 2

# E por fim, quando você foi avisar ao David como ele podia fazer para chegar, você teve que dizer o número da sala em binário com uma quantidade x de bits, pois no momento ele estava com um defeito. Caso você tenha esquecido como você fez isso, lembre-se que para converter um número em binário nós pegamos o número e fazemos várias divisões por inteiro e armazenamos o resto até a divisão ser igual a zero. Ex:

# 25 // 2 = 12 (resto 1), 12 // 2 = 6 (resto 0), 6 // 2 = 3(resto 0), 3//2 = 1 (resto 1), 1 // 0 → fim (resto 1), lendo os restos de trás para frente, temos o número binário 11001 que é o 25. Porém ainda falta converter para o tamanho de bits que o David entende, que nesse caso seria 8, para isso inserimos “0” ate o tamanho chegar a 0, assim: 00011001. Porém nem todos os números conseguem ser representados em uma certa quantidade de bits, pois 1 bit representa até numero 1, 2 bits até o 3, 3 bits até 7, 8 bits ate 15 e assim por diante.

# Você deverá criar um código que faça a mesma busca que você fez e as informações que passou para o David.

# Input

# A primeira linha vai ser uma série de números ordenados que representam a numeração da sala, onde você irá fazer a busca. Logo após, você receberá o número da sala que a Doutora lhe deu a dica. E por fim você receberá a quantidade de bits que o Dave está recebendo no momento.

# numeros_das_salas

# numero_escolhido

# qnt_bits

# Output

# Caso tudo dê certo, você deverá imprimir:

# “Coord_x -> … Coord_n Meio, seguindo por essas coordenadas você vai chegar no número {num_bin}.”

# Em que Coord_x ... Coord_n representam as direções que foram escolhidas durante a busca: Esquerda, Direita ou Meio
# Mas se você conseguiu achar o item, e David não suporta o tamanho de bits, você deverá pintar:

# “Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.”

# Se o item não estiver na lista por ser menor que o primeiro item ou maior que o último, você deverá dizer:

# “Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.”

# E se o item não estiver na lista, apesar de estar entre o intervalo do primeiro e do último, você deverá colocar o caminho que você foi e uma mensagem que não conseguiu encontrar

# Coord_x -> … Coord_n, mas não consegui achar.

# Se você não conseguiu achar o item e David não suporta o tamanho de bits, deverá dizer:

# 'Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.’

# Examples

# Case: 1

# Input

# 1 2 3 4 5 6 7 8 9 10
# 7
# 4

# Output

# Direita -> Esquerda -> Esquerda -> Meio, seguindo por essas coordenadas você vai chegar no número 0111.

# Case: 2

# Input

# 5 6 7 8 9
# 10
# 3

# Output

# Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.

# Case: 3

# Input

# 4 5 7 12 17 27 30
# 27
# 3

# Output

# Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.


#função de busca binária
def busca_binaria(arr,  x, caminho):
	mid = len(arr) // 2
	if len(arr) >= 1:
		if arr[mid] == x or len(arr) == 1:
			caminho.append("Meio")
			return caminho
		elif x < arr[mid]:
			caminho.append('Esquerda')
			return busca_binaria(arr[:mid], x, caminho)
		else:
			caminho.append('Direita')
			return busca_binaria(arr[mid+1:], x, caminho)
	else:
		return caminho

#função transformar número pra decimal
def decimal_para_binario(x):
	return int(format(x, "b"))

numeros_das_salas = input()
numero_escolhido = int(input())
qnt_bits = int(input())

a = [int(item) for item in numeros_das_salas.split()]

#encontrando o caminho e o binário do número caso ele esteja dentro da lista

caminho = busca_binaria(a,numero_escolhido, [])
binario = decimal_para_binario(numero_escolhido)


#organizando o print do caminho
if caminho != -1:
	cam = ''
	for i in range(len(caminho) -1):
			cam += caminho[i] + ' -> '
	cam += caminho[-1]

#organiznado o print do binário
binario = str(binario)

if len(binario) < qnt_bits:
	while len(binario) != qnt_bits:
		binario = '0' + binario

#prints
if (numero_escolhido in a) and (len(binario) == qnt_bits):
	print(f'{cam}, seguindo por essas coordenadas você vai chegar no número {binario}.')

elif (numero_escolhido in a) and (len(binario) > qnt_bits):
	print(f'Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.')

elif ((numero_escolhido < min(a)) or (numero_escolhido > max(a))):
	print('Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.')

elif (numero_escolhido not in a) and (len(binario) > qnt_bits):
	print('Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.')

elif (numero_escolhido not in a):
	print(f'{cam}, mas não consegui achar.')
