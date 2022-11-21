# Problem Statement

# Originalmente criadas para celebras os três santos de junho – Antônio, João e Pedro -, as festas juninas começaram a tomar conta da agenda cultura do Brasil. De norte a sul, as cidades convidam a população e os turistas para festejos típicos. As principais cidades são: Caruaru(PE), Campina Grande(PB), João Pessoa(PB), São Luís (MA), Mossoró e Natal (RN), Fortaleza (CE), entre outas. Para escolher a melhor festa, existe um site que fornece notas, que é uma média das avaliações recebidas por cada cidade. Sua tarefa é ajudar o usuário a encontrar a cidade mais adequada para ele ir, que seria a de maior nota. Apenas um detalhe, caso a nota mais alta não seja maior ou igual a 4, deve-se imprimir "Nota mínima não atingida".

# Em caso de empate nas notas deve selecionar a cidade mais próxima. Não haverá empate na proximidade nesses casos.

# Input

# As entradas representam as informações de 3 cidades, para cada cidade, teremos uma string composta pelo nome da cidade, seguido da respectiva nota (0 <= nota <= 5.0, com 1 casa decimal) e a distância da cidade em relação ao usuário em km,

# Cidade 1

# Nota 1

# Distância 1

# Cidade 2

# Nota 2

# Distância 2

# Cidade 3

# Nota 3

# Distância 3

# Output

# A saída consiste de uma linha única

# Caso nenhuma cidade tenha nota maior ou igual a 4:

# Nota mínima não atingida

# Caso contrário, você deve imprimir a cidade com a maior pontuação

# Nome_Cidade

# Examples

# Case: 1

# Input

# Campina Grande
# 3.5
# 1150
# Caruaru
# 4.0
# 1140
# Recife
# 3.5
# 1570

# Output

# Caruaru

# Case: 2

# Input

# Fortaleza
# 3.5
# 1150
# Natal
# 3.0
# 1060
# Mossoro
# 3.5
# 1570

# Output

# Nota mínima não atingida

# Case: 3

# Input

# Salvador
# 4.0
# 1150
# Paulo Afonso
# 4.0
# 1060
# Aracaju
# 4.0
# 1570

# Output

# Paulo Afonso


c1 = input()
n1 = float(input())
d1 = int(input())

c2 = input()
n2 = float(input())
d2 = int(input())

c3 = input()
n3 = float(input())
d3 = int(input())

if (n1>n2 and n1>n3):
	print(c1)
elif (n2>n1 and n2>n3):
	print(c2)
elif (n3>n1 and n3>n2):
	print(c3)
elif (n1<4.0 and n2<4.0 and n3<4.0):
	print("Nota mínima não atingida")
elif (n1==n2==n3):
	if (d1<d2 and d1<d3):
		print(c1)
	elif (d2<d1 and d2<d3):
		print(c2)
	elif (d3<d1 and d3<d2):
		print(c3)
