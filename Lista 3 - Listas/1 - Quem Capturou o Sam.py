# Problem Statement

# Sam Winchester foi sequestrado! Dean conta com a sua ajuda para encontrar o responsável e trazer o irmão de volta à segurança.

# Para isso, você receberá uma lista de suspeitos, e realizará operações nela de acordo com o comando de Dean, até que sobre um único culpado.

# Input

# Para o input, inicialmente, será recebida uma lista de nomes separados por vírgula, em uma mesma linha.

# nome1,nome2,nome3, ... ,nome n

# Em seguida, serão recebidas diversas entradas, até que sobre um único suspeito na lista e o mistério seja solucionado.

# Para cada entrada descrita abaixo, realize a operação correspondente:

# “Não encontrei nada no primeiro suspeito"

# Você deve remover o primeiro suspeito da lista.

# “O último da lista está limpo”

# Você deve remover o último suspeito da lista

# “Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita”

# Você deve remover o nome do indivíduo que encontra-se no meio da lista.

# **OBS: Note que, caso o número de elementos restantes na lista seja par, deve-se remover o elemento de maior índice entre os dois elementos do meio.

# “Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:”

# Você receberá logo em seguida uma entrada com a posição do suspeito na lista, que começa no índice 0, e o removerá da lista.

# “Acho que temos mais uma opção a ser analisada…”

# Você receberá logo em seguida uma entrada com o nome do novo suspeito e o adicionará no final da lista.

# Qualquer outra entrada além das mencionadas anteriormente não gerará nenhuma operação na lista.

# **OBS: Está liberado o uso de métodos e funções prontas de listas

# Output

# Sempre que a entrada for diferente das especificadas no input, você avisará ao Dean:

# “Isso não estava no combinado, a lista vai permanecer do mesmo jeito”
# Quando a lista tiver apenas um suspeito, você deve finalizar as operações e avisar ao Dean que a busca chegou ao fim por meio da seguinte frase:

# “Acho que encontramos o suspeito. O seu nome é {nome_suspeito}, vamos salvar o Sam!”
# Examples

# Case: 1

# Input

# Alastair,Eve,Metatron,Lilith,Amara,Azazel
# Não encontrei nada no primeiro suspeito
# Não encontrei nada no primeiro suspeito
# O último da lista está limpo
# Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita
# Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:
# 1

# Output

# Acho que encontramos o suspeito. O seu nome é Metatron, vamos salvar o Sam!


suspeitos= input().split(',')

while(len(suspeitos)!=1):
	mensagem = input()
	if (mensagem =="Não encontrei nada no primeiro suspeito"):
		del suspeitos[0]
	elif (mensagem =="O último da lista está limpo"):
		suspeitos.pop(-1)
	elif (mensagem == "Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita"):
		len(suspeitos)
		del suspeitos[int(len(suspeitos)/2)]
	elif (mensagem == "Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:"):
		posicao = int(input())
		suspeitos.pop(posicao)
	elif (mensagem =="Acho que temos mais uma opção a ser analisada…"):
		novo_suspeito = input()
		suspeitos.append(novo_suspeito)
	else:
		print("Isso não estava no combinado, a lista vai permanecer do mesmo jeito")

print(f"Acho que encontramos o suspeito. O seu nome é {suspeitos[0]}, vamos salvar o Sam!")

