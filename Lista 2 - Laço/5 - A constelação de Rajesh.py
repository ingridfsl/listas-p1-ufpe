#Problem Statement

#Sabemos que o doutor Rajesh Koothrappali, “Raj” para os mais íntimos, é um Ph.D em astrofísica.

#Em um belo dia, durante sua rotina de trabalho noturno, Raj estava observando o céu quando se deparou com um grupo de estrelas nada familiar. 

#Observando mais um pouco, Raj notou que a distância entre as estrelas do grupo parecia seguir um padrão Fibonacci e ficou muito empolgado, pois se as estrelas estiverem mesmo seguindo esse padrão, ele pode ter descoberto uma mini constelação. Então ele decidiu pegar seu melhor telescópio e utilizar o método paralax para estimar os pontos de localização de cada estrela do grupo. Depois de ter feito todos os cálculos, Raj fez um plano cartesiano e anotou os eixos X e Y de cada estrela. Feito isso, agora ele precisa saber se descobriu uma nova constelação, então ele tem que criar um programa capaz de verificar se a distância entre uma estrela e outra pertence à sequência de Fibonacci. 

#Mas, como Raj não sabe programar, ele solicitou a sua ajuda.

#Você pode usar distância euclidiana para verificar a distância entre as estrelas. Nessa questão, o código deve trabalhar apenas com números inteiros, então o resultado da distância deve ser convertido para inteiro antes de ser checado se pertence ou não a sequência.

#Distância euclidiana: D² = (X1 - X2)² + (Z1 - Z2)²

#Obs: Você deve resolver esse problema utilizando apenas o que foi dado na disciplina até o dado momento. (estruturas de repetição, estruturas condicionais e operações básicas.)

#Input

#Você receberá a quantidade de estrelas
#N: Quantidade de estrelas

#Em seguida, receberá o eixo x seguido pelo eixo_y de cada N estrela.
#star1_x: Eixo X da estrela 1

#star1_y: Eixo Y da estrela 1

#star2_x: Eixo X da estrela 2

#star2_y: Eixo Y da estrela 2

#...

#starN_x: Eixo X da estrela N

#starN_y: Eixo Y da estrela N

#Os eixos da localização das estrelas serão sempre maior que zero.

#Output

#Para cada distância calculada, você deve imprimir
#Distância [star{a} <-> star{b}]: {dist}

#Sendo a e b as posições das estrelas na ordem de entrada, começando a contagem apartir de 1 e dist a distância euclidiana transformada em inteiro entre as duas estrelas

#Ao final das entradas, seu código deve ser capaz de retornar corretamente o inteiro de cada distância e uma das 5 saídas possíveis. Se cair em uma das duas últimas condições, você não precisará imprimir as distâncias.
#Se todas as distâncias pertencerem à sequência de Fibonacci mas a soma das disâncias não for um número primo:

#Yes! Eu consegui!

#Se todas as distâncias pertencerem à sequência de Fibonacci e a soma das distâncias for um número primo

#Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!

#Se apenas uma das distâncias não pertencer a sequência:

#Oh, não! Eu quase consegui!

#Se duas ou mais distâncias não pertencerem à sequência e a soma das distâncias não for um número primo:

#Eu vou acabar como o Stuart :/

#Se duas ou mais distâncias não pertencerem à sequência mas a soma das distâncias for um número primo:

#Pelo menos o programa está funcionando...

#Se N for menor ou igual a 0

#Isso está quebrado, acho que Howard pode me ajudar.

#Se N for menor que 3 e maior que zero

#Acho que bebi demais, eu juro que tinha mais estrelas!

#Nesses dois casos, o programa deve ser encerrado sem calcular nenhuma distância ou imprimir outras mensagens

#Examples

#Case: 1

#Input

#5
#10
#4
#12
#6
#15
#7
#18
#2
#20
#4

#Output

#Distância [star1 <-> star2]: 2
#Distância [star2 <-> star3]: 3
#Distância [star3 <-> star4]: 5
#Distância [star4 <-> star5]: 2
#Yes! Eu consegui!

#Case: 2

#Input

#-5

#Output

#Isso está quebrado, acho que Howard pode me ajudar.

#Case: 3

#Input

#7
#18
#36
#54
#85
#68
#95
#15
#68
#47
#56
#10
#28
#45
#35

#Output

#Distância [star1 <-> star2]: 60
#Distância [star2 <-> star3]: 17
#Distância [star3 <-> star4]: 59
#Distância [star4 <-> star5]: 34
#Distância [star5 <-> star6]: 46
#Distância [star6 <-> star7]: 35
#Pelo menos o programa está funcionando...


entrada = int(input())
x1= 0
z1 = 0
contador = 0
soma_distancia = 0
nao_fibonacci = 0

if (entrada >3):
	while (contador < entrada):
		x = int(input())
		z = int(input())
		if (contador !=0):
			distancia = int(((x1-x)**2 + (z1-z)**2)**0.5)
			print (f'Distância [star{contador} <-> star{contador+1}]: {distancia}')
			soma_distancia += distancia

			ultimo = 1
			penultimo = 1
			if distancia > 2:
				termo = 3
				while termo < distancia:
					termo = ultimo + penultimo
					penultimo = ultimo
					ultimo = termo
				if termo != distancia:
					nao_fibonacci += 1
		x1 = x
		z1 = z
		contador += 1

	soma_primo = False
	multiplos=0
	for i in range(2,soma_distancia):
		if (soma_distancia % i == 0):
			multiplos += 1
	if (multiplos ==0):
			soma_primo = True

	if (nao_fibonacci==0 and not soma_primo):
			print('Yes! Eu consegui!')
	elif (nao_fibonacci==0 and soma_primo):
		print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')
	elif (nao_fibonacci == 1):
		print('Oh, não! Eu quase consegui!')
	elif (not soma_primo and nao_fibonacci >= 2):
		print('Eu vou acabar como o Stuart :/')
	elif (soma_primo and nao_fibonacci >= 2):
		print('Pelo menos o programa está funcionando...')

elif (3 > entrada > 0):
	print('Acho que bebi demais, eu juro que tinha mais estrelas!')
else:
	print('Isso está quebrado, acho que Howard pode me ajudar.')

