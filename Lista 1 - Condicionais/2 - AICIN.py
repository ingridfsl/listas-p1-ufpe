# Problem Statement

# Como todos sabem, o São João é uma das melhores épocas do ano e, com ele, vem também as comidas típicas, que são de longe umas das melhores partes dessa época! 

# A empresa AICIN, que vende todo tipo de comida, nessa época do ano resolve apenas vender comidas típicas do São João, mas como o fluxo de pedido está muito alto e algumas pessoas estão fazendo pedidos de outro tipo de comida como: Pizza, hambúrgueres e etc, a AICIN resolve chamar, VOCÊ, aluno(a) do CIN para ajudar a criar um código que irá conseguir diferenciar os tipos de comida que estão sendo pedidas. 

# Para isso, você vai precisar criar um programa onde receberá de entrada um tipo de comida e você terá que informar se é junina ou não.

# Os tipos de comidas juninas que estão sendo oferecidas pelo AICIN são: Canjica, Pamonha e Bolo de milho. Qualquer outra comida digitada o AICIN não vai conseguir identificar.

# Input

# O input é uma linha única contendo o nome da comida a ser identificada, que pode ser uma das abaixo:

# “Pamonha”

# “Canjica”

# “Bolo de milho”

# Output

# Se a comida escolhida for canjica, deverá retornar:

# “Boa! Canjica faz parte.”

# Se a comida escolhida for pamonha, deverá retornar:

# “Boa! Pamonha faz parte.”

# Se a comida escolhida for bolo de milho, deverá retornar:

# “Boa! Bolo de milho faz parte.”

# Caso, outro tipo de comida for digitada ou qualquer outra coisa que não seja os 3 tipos, irá retornar:

# “Opa! Parece que voce procura um tipo de comida que nao combina com essa epoca, tente novamente.”

# Examples

# Case: 1

# Input

# Canjica

# Output

# Boa! Canjica faz parte.

# Case: 2

# Input

# Pizza

# Output

# Opa! Parece que voce procura um tipo de comida que nao combina com essa epoca, tente novamente.


x = input()

if (x == "Pamonha" or x== "Canjica" or x== "Bolo de milho"):
	print("Boa! " + x + " faz parte.")

else:
	print("Opa! Parece que voce procura um tipo de comida que nao combina com essa epoca, tente novamente.")
