# Problem Statement

# Na cultura popular brasileira, as festas juninas têm lugar especial, pois, além de valorizarem as tradições locais do país, também revelam muitos elementos históricos, religiosos e mitológicos curiosos, que passam despercebidos. 

# Ademais, não podemos esquecer dos diversos shows que ocorrem pelas grandes cidades nessa época maravilhosa.

# Como exemplo, temos o São João de Petrolina, que trás diversos cantores para animar o povo dessa cidade incrível. Com 9 dias de show, o local conta com cantores como Nattan, Priscila Senna, Cavaleiros do Forró, Zé vaqueiro e muitos outros.

# Pedro, um estudante do CIn, resolveu tirar alguns dias de férias em petrolina para aproveitar essa festa, sabendo que ele estava em época de recesso da faculdade.

# Após lembrar das aulas de programação, Pedro resolveu desenvolver um programa que facilitaria saber qual o valor máximo que ele poderá gastar em cada dia de festa, supondo que ele irá gastar com alimentação, bebida e transporte nos dias de festa. Esse valor varia dependendo se seus cantores favoritos cantarão ou não cantarão em cada dia de show.

# Sabendo que você se passa por Pedro para desenvolver esse programa, você deve considerar que:

# Os shows ocorrerão do dia 17 ao dia 26, com exceção do dia 20.
# Os cantores favoritos de Pedro cantarão nos dias pares.
# Pedro estipulou uma meta de gastar no máximo 400 reais em dias que seus cantores favoritos cantarem e 200 reais nos dias que seus cantores favoritos não cantarem.
# Input

# A linha de entrada será um número inteiro, O dia que Pedro irá consultar o valor máximo que ele pode gastar.

# X - inteiro

# Output

# A linha de saída será uma string, que dependerá da linha de entrada digitada por Pedro.

# Caso for escolhido um dia que um dos cantores favoritos de Pedro cantará, deverá retornar: “Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!”

# Caso for escolhido um dia que nenhum cantor favorito de Pedro cantará, deverá retornar: “Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!”

# Caso for escolhido um dia que seja fora do intervalo do dia 17 ao dia 26, deverá retornar: “Você escolheu um dia que não irá acontecer nenhum show, tente novamente!”

# Caso for escolhido o dia 20, também deverá retornar: “Você escolheu um dia que não irá acontecer nenhum show, tente novamente!”

# Examples

# Case: 1

# Input

# 17

# Output

# Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!

# Case: 2

# Input

# 24

# Output

# Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!

n = int(input())

if (n==18 or n==22 or n==24 or n==26):
	print("Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!")
elif (n==17 or n==19 or n==21 or n==23 or n==25):
	print("Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!")
elif (n<17 or n>26 or n==20):
	print("Você escolheu um dia que não irá acontecer nenhum show, tente novamente!")
