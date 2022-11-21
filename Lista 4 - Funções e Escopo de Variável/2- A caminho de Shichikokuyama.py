# Problem Statement

# Satsuki e Mei são duas irmãs que se mudaram com o pai para uma cidade rural do Japão enquanto a mãe se encontra hospitalizada. Num certo dia, andando pela floresta, elas descobrem diversos mistérios e conhecem Totoro, uma criatura espiritual habitante e protetora da floresta que é uma mistura de gato, coruja e raposa. Elas ficaram muito amigas desse ser e sempre o ajudavam na preservação da floresta. Depois de um tempo vivendo na zona rural, Satsuki e Mei sentiram muita falta da mãe e decidiram visitá-la, mas não lembram qual é o nome do hospital, porque é um nome grande e difícil de pronunciar. Na tentativa de ajudar, Totoro decide falar várias palavras em japonês para que elas identifiquem, nessas palavras, sílabas ou a palavra completa que fazem parte do nome do hospital.

# É obrigatório o uso de funções nessa questão

# Input

# A entrada será composta por várias palavras que Totoro irá dizer para as irmãs, até que elas completem o nome do hospital: shichikokuyama.

# palavra1

# palavra2

# …

# palavraN

# OBS: Uma sílaba em japonês terá sempre uma única vogal e ela é sempre a última letra da sílaba.

# Sílabas do nome do hospital: shi, chi, ko, ku, ya, ma

# OBS2: todas as palavras estarão sempre em minúsculo.

# Output

# Após Totoro dizer uma palavra, várias saídas serão possíveis, as quais são:

# Se a palavra dita por Totoro não tiver nenhuma sílaba pertencente ao nome do hospital, deve ser printado:

# “Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.”

# Já se a palavra dita por Totoro tiver apenas uma sílaba que está no nome do hospital, deve ser printado:

# “Lembrei! A sílaba {silaba} está no nome do hospital. Obrigada, Totoro!”

# Caso a palavra dita tenha 2 ou mais sílabas e estão no nome do hospital, mas a palavra completa na ordem certa não está no nome do hospital, deve ser printado:

# “Lembrei! As sílabas: {silaba1}, {silaba2}, {silabaN} estão no nome do hospital. Obrigada, Totoro!”

# *As sílabas estão sempre separadas por vírgula e espaço.

# OBS: A palavra “kochi”, por exemplo, entraria no caso acima, pois apesar de todas as sílabas dela estarem na palavra shichikokuyama, ela não está na ordem certa.

# Se a palavra inteira está no nome do hospital, está na ordem certa e não tem uma só sílaba, deve ser printada a seguinte frase.

# “A palavra {palavra} está toda no nome do hospital. Acertou em cheio, Totoro!”

# OBS: Um exemplo de entrada possível do caso acima é a palavra “yama”.

# OBS2: Se tiver uma palavra que contenha sílabas que já foram identificadas, ignore essa sílaba e a considere como uma sílaba que não faz parte da palavra.

# No fim, ao conseguir completar a palavra shichikokuyama, você irá printar a mensagem abaixo:

# “Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!”

# Examples

# Case: 1

# Input

# shika
# kochi
# kuya
# ma

# Output

# Lembrei! A sílaba shi está no nome do hospital. Obrigada, Totoro!
# Lembrei! As sílabas: ko, chi estão no nome do hospital. Obrigada, Totoro!
# A palavra kuya está toda no nome do hospital. Acertou em cheio, Totoro!
# Lembrei! A sílaba ma está no nome do hospital. Obrigada, Totoro!
# Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!

# Case: 2

# Input

# mizu
# sushi
# hachi
# chi
# ko
# kurama
# yamato

# Output

# Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.
# Lembrei! A sílaba shi está no nome do hospital. Obrigada, Totoro!
# Lembrei! A sílaba chi está no nome do hospital. Obrigada, Totoro!
# Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.
# Lembrei! A sílaba ko está no nome do hospital. Obrigada, Totoro!
# Lembrei! As sílabas: ku, ma estão no nome do hospital. Obrigada, Totoro!
# Lembrei! A sílaba ya está no nome do hospital. Obrigada, Totoro!
# Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!

# Case: 3

# Input

# kaka
# ume
# ha
# ya
# ya
# yama
# chishi
# kokuya

# Output

# Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.
# Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.
# Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.
# Lembrei! A sílaba ya está no nome do hospital. Obrigada, Totoro!
# Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.
# Lembrei! A sílaba ma está no nome do hospital. Obrigada, Totoro!
# Lembrei! As sílabas: chi, shi estão no nome do hospital. Obrigada, Totoro!
# Lembrei! As sílabas: ko, ku estão no nome do hospital. Obrigada, Totoro!
# Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lásilabas = []

# silabas = []

# def separador():
	# vogais = ['a', 'e', 'i', 'o', 'u']
	# count = 0
	# for index in range(len(palavra)):
		# if palavra[index] in vogais:
			# silabas.append(palavra[count:index + 1])
			# count = index + 1
	# return silabas

# palavra = input()
# separador(palavra)
# print(silabas)


#função separar em sílabas
def split_palavra(palavra):
	vogais = ['a', 'e', 'i', 'o', 'u']
	count = 0
	silabas = []
	for index in range(len(palavra)):
		if palavra[index] in vogais:
			silabas.append(palavra[count:index + 1])
			count = index + 1
	return silabas

nome_hospital = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']
silabas = []
silaba_certa = []

while (len(nome_hospital) != len(silaba_certa)):
	palavra = input()
	silabas = split_palavra(palavra)
	temp_silaba = []
	for silaba in silabas:
		if silaba in nome_hospital and silaba not in silaba_certa:
			silaba_certa.append(silaba)
			temp_silaba.append(silaba)
#verificando a ordem
	em_ordem = False
	if len(temp_silaba) == len(silabas):
		if palavra in 'shichikokuyama':
			em_ordem = True
#prints
	if (len(temp_silaba)>1 and em_ordem == True):
		print(f'A palavra {palavra} está toda no nome do hospital. Acertou em cheio, Totoro!')
	elif (len(temp_silaba) == 1):
		print(f'Lembrei! A sílaba {temp_silaba[0]} está no nome do hospital. Obrigada, Totoro!')
	elif (len(temp_silaba) > 1):
		s = ', '
		print(f'Lembrei! As sílabas: {s.join(temp_silaba)} estão no nome do hospital. Obrigada, Totoro!')
	elif (len(temp_silaba) == 0):
		print(f'Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')


print(f'Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')








