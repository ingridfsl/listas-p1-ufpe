# Problem Statement

# Haru salvou um gatinho que ia ser atropelado ao atravessar a rua, mas não esperava que esse gato fosse o príncipe do Reino dos Gatos!
# Em gratidão, o reino prometeu dias de felicidade à menina e entregou uma carta escrita em símbolos de Miauês (idioma dos gatos). 
# Haru pediu sua ajuda para entender o que dizia a carta. Ela conseguiu identificar palavras e sabe que cada letra foi representada por um número.

# Cada número representa uma letra, de acordo com algumas regras:

# De 0 até 49, os números representam letras minúsculas, de forma que 0 = a, 1 = b, etc. Lembre-se que deve-se considerar que o alfabeto inicia novamente da letra a para números maiores que 25. Ex. 25 = z e 26 = a.

# De 50 até 99, os números representam letras maiúsculas, de forma que 50 = A, 51 = B, etc. Lembre-se que deve-se considerar que o alfabeto inicia novamente da letra A para números maiores que 75. Ex. 75 = Z e 76 = A.

# Se o número for 100, ele representa um espaço para separar duas palavras.

# Se algum número não estiver no intervalo identificado pelas regras acima, não é possível traduzi-lo.

# AS PALAVRAS NÃO TÊM ACENTO E NEM Ç

# Você pode usar os métodos do python ord() e chr() e deve consultar a Tabela Ascii para usar essas funções corretamente. Também lembre de construir uma função para traduzir os números.

# Input

# Você receberá uma lista de x números inteiros separada por espaço:

# n1 n2 n3 n4 n5 n6 .... nx

# Output

# A saída deve conter a mensagem que você e Haru conseguiram decodificar, caso não seja possível fazer a decodificação completa, a mensagem deve ser a seguinte:

# 'Infelizmente os números nao dizem nada'

# Examples

# Case: 1

# Input

# 64 100 17 4 8 13 14 100 3 14 18 100 56 0 19 14 18 100 14 5 4 17 4 2 4 100 15 4 19 8 18 2 14 18

# Output

# O reino dos Gatos oferece petiscos

# Case: 2

# Input

# 19 20 100 121 0 8 100 15 0 18 18 0 17 100 4 12 100 58 65

# Output

# Infelizmente os números nao dizem nada

numeros = list(range(101))
alfabeto = []
codigos = input().split(' ')

# lista do alfabeto de 0 a 100
# posição 0 a 26
c = 0
for i in range(ord('a'), ord('z')+1): 
	alfabeto.insert(c, chr(i))
	c += 1
# posição 26 a 49
for i in range (ord('a'), ord('x')+1):
	alfabeto.append(chr(i))
# posição 50 a 75
for i in range (ord('A'), ord('Z')+1):
	alfabeto.append(chr(i))
# posição 76 a 99
for i in range (ord('A'), ord('X')+1):
	alfabeto.append(chr(i))
#inserindo o espaço na posição 100
alfabeto.append(' ')

#função de codificação
def codificador (codigo):
	mensagem =''
	identificavel = True
	for codigo in codigos:
		if (int(codigo) in numeros):
			letra = alfabeto[int(codigo)]
			mensagem = mensagem + letra
		else:
			identificavel = False
	if identificavel == True:
		return mensagem
	else:
		return ('Infelizmente os números nao dizem nada')
#chamada da função 
mensagem = codificador(codigos)
print(mensagem)







