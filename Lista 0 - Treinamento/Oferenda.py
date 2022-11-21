# Problem Statement

# Após ficarem impressionados com a mecânica do jogo, Arthur, Luiz e Pedro resolveram continuar jogando. Como Tantan estava muito mais avançado em recursos, eles convidaram Tantan para morar em suas vilas e fizeram ofertas de diamantes para tornar o convite mais interessante. Arthur ofereceu 10 diamantes, Luiz ofereceu 30 e Pedro 100.

# Tantan estava precisando de diamantes, porém, sendo um garoto muito humilde, falou que iria aceitar a menor oferta possível que suprisse sua necessidade.

# Sua tarefa é fazer um programa que ajude Tantan a decidir com quem ir morar.

# Input

# D

# D - número natural (1 <= D)
# A linha única de entrada é composta pela quantidade de diamantes que Tantan necessita.

# Obs: Você deve considerar que a entrada é amigável, ou seja, sempre estará dentro do formato descrito.

# Output

# P

# P - string
# A linha única de saída é composta pelo nome de quem fez a oferta que foi aceita por Tantan, ou pela string "Nenhum", no caso em que nenhuma oferta supria a quantidade de diamantes necessária.

# Examples

# Case: 1

# Input

# 20

# Output

# Luiz

# Case: 2

# Input

# 120

# Output

# Nenhum

# Case: 3

# Input

# 5

# Output

# Arthur

d = int(input())

if (0 < d <= 10):
	print("Arthur")
if(10 <  d<= 30):
	print("Luiz")
if (30 < d <=100): 
	print("Pedro")
if (d == 0 or d > 100):
	print("Nenhum")
