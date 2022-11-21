# Problem Statement

# Foi decidido que no CIN seria feito uma competição de quadrilhas juninas e cada turma deveria participar. 

# Você foi o responsável por calcular a pontuação de cada equipe. Uma lista de passos permitidos foi divulgada para cada equipe. 

# Algumas regras foram definidas para calcular a pontuação final da quadrilha, mas preste bem atenção, somente você tem acesso a essas regras.

# Lista de passos permitidos:

# Cumprimento.
# Balancê.
# Passeio.
# Túnel.
# Serrote.
# Casamento.
# Despedida.
# Regras:

# Cada quadrilha tem uma sequência de 5 passos.
# Se algum passo diferente dos divulgados da lista for usado, a quadrilha terá a pontuação zerada.
# Toda quadrilha que começar com o passo “Cumprimento” terá pontuação inicial de 100 pontos. Caso o “Cumprimento” apareça em alguma outra posição, damos 10 pontos.
# A cada “Balancê” a pontuação é acrescida de 50 pontos.
# Cada “Passeio” vale 70 pontos.
# Cada vez que fizer o “Túnel” perde 10% da pontuação.
# “Serrote” vale 100 pontos.
# Caso o casamento seja realizado ao menos uma vez, a pontuação final é dobrada.
# A “Despedida” só será pontuada se vier como último passo da quadrilha, caso apareça em alguma outra posição a pontuação não será modificada. A "Despedida" vale 35 pontos.
# OBS: A pontuação deverá ser do tipo float.

# Input

# A entrada consiste nas seguintes 6 linhas:

# "nome_da_quadrilha"

# "passo_1"

# "passo_2"

# "passo_3"

# "passo_4"

# "passo_5"

# Atenção: As entradas sempre serão amigáveis e nunca uma quadrilha será composta de apenas um único movimento.

# Output

# Se a pontuação for zero, deverá retornar a seguinte frase:

# "Poxa, [nome_da_quadrilha]. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada."

# Caso a pontuação seja maior que zero:

# "Parabéns, [nome_da_quadrilha]! Bela apresentação. A pontuação foi de [pontuacao]!"

# Atenção: A pontuação deverá ser impressa com a precisão de 1 casa decimal.

# Examples

# Case: 1

# Input

# CINtenario de tradição
# Cumprimento
# Serrote
# Casamento
# Serrote
# Despedida

# Output

# Parabéns, CINtenario de tradição! Bela apresentação. A pontuação foi de 670.0!

# Case: 2

# Input

# CINtenario de tradição
# Cumprimento
# Avante
# Casamento
# Serrote
# Despedida

# Output

# Poxa, CINtenario de tradição. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.

nome = input()
passo1 = input()
passo2 = input()
passo3 = input()
passo4 = input()
passo5 = input()
pontuacao = 0

passoProibido = False
teveCasamento = False

if (passo1 == "Cumprimento"):
	pontuacao += 100
elif (passo1 == "Balancê"):
	pontuacao += 50
elif (passo1 == "Passeio"):
	pontuacao += 70
elif (passo1 == "Túnel"):
	pontuacao *= 0.9
elif (passo1 == "Serrote"):
	pontuacao += 100
elif (passo1 == "Casamento"):
	teveCasamento = True
elif (passo1 == "Despedida"):
	pontuacao += 0
else:
	passoProibido = True

if (passo2 == "Cumprimento"):
	pontuacao += 10
elif (passo2 == "Balancê"):
	pontuacao += 50
elif (passo2 == "Passeio"):
	pontuacao += 70
elif (passo2 == "Túnel"):
	pontuacao *= 0.9
elif (passo2 == "Serrote"):
	pontuacao += 100
elif (passo2 == "Casamento"):
	teveCasamento = True
elif (passo2 == "Despedida"):
	pontuacao += 0
else:
	passoProibido = True

if (passo3 == "Cumprimento"):
	pontuacao += 10
elif (passo3 == "Balancê"):
	pontuacao += 50
elif (passo3 == "Passeio"):
	pontuacao += 70
elif (passo3 == "Túnel"):
	pontuacao *= 0.9
elif (passo3 == "Serrote"):
	pontuacao += 100
elif (passo3 == "Casamento"):
	teveCasamento = True
elif (passo3 == "Despedida"):
	pontuacao += 0
else:
	passoProibido = True

if (passo4 == "Cumprimento"):
	pontuacao += 10
elif (passo4 == "Balancê"):
	pontuacao += 50
elif (passo4 == "Passeio"):
	pontuacao += 70
elif (passo4 == "Túnel"):
	pontuacao *= 0.9
elif (passo4 == "Serrote"):
	pontuacao += 100
elif (passo4 == "Casamento"):
	teveCasamento = True
elif (passo4 == "Despedida"):
	pontuacao += 0
else:
	passoProibido = True

if (passo5 == "Cumprimento"):
	pontuacao += 10
elif (passo5 == "Balancê"):
	pontuacao += 50
elif (passo5 == "Passeio"):
	pontuacao += 70
elif (passo5 == "Túnel"):
	pontuacao *= 0.9
elif (passo5 == "Serrote"):
	pontuacao += 100
elif (passo5 == "Casamento"):
	teveCasamento = True
elif (passo5 == "Despedida"):
	pontuacao += 35
else:
	passoProibido = True

if (teveCasamento):
	pontuacao *= 2

if (passoProibido):
	pontuacao = 0

if (pontuacao > 0):
	print(f'Parabéns, {nome}! Bela apresentação. A pontuação foi de {pontuacao:.1f}!')
if (pontuacao == 0):
	print(f'Poxa, {nome}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')
