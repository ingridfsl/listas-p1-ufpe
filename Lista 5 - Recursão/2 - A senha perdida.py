# Problem Statement

# Cooper e seus amigos tripulantes estavam próximos ao massivo buraco negro Gargantua e perceberam que a senha de acesso a serviços emergenciais da nave, que estava armazenada no sistema para casos extremos, tinha sido alterada. A grande distorção do espaço-tempo prejudica o funcionamento dos equipamentos e alterou os caracteres da senha original. Sua missão como programador(a) da tripulação é desenvolver um código que altere caracteres e cheque se, ao final das alterações, a nova palavra gerada pela distorção é idêntica à senha alterada. Assim, a senha original estará sob alcance de todos novamente.

# É de conhecimento da tripulação que, em casos de interferência pela distorção, a fórmula que equivale ao efeito nos caracteres é uma combinação da sequência de Fibonacci e fatorial. Esse efeito se dá em caractere por caractere, ou seja, os passos são aplicados para cada caractere, e funciona da seguinte maneira:

# Aplica-se mod 11 na posição de cada letra no alfabeto. (Considere como 0 a posição da primeira letra do alfabeto, 1 da segunda, etc)
# Calcula-se a sequência de Fibonacci até o número resultante na primeira operação. Ou seja, se a operação 1 resultou 3, deve-se calcular a sequência até o terceiro termo: [0, 1, 1]. E também calcula-se o fatorial de 0 até n-1. Ou seja, o resultado da operação 1 sendo 4, deve-se calcular o fatorial de 0, de 1, de 2 e de 3: [1, 1, 2, 6].
# Por fim, são analisados três cenários: o resultado da operação 1 ser 0 (ser ímpar ou par, desconsiderando o 0). Caso seja 0, "1" será adicionado como parte da nova palavra. Caso seja ímpar, o(s) novo(s) caractere(s) será(ão) resultantes de uma multiplicação entre os termos da sequência de Fibonacci e do fatorial, sendo par é semelhante ao cenário de ímpares, mas substituindo a multiplicação por uma soma.
# Exemplo: cenário em que seja ímpar e 3 teremos Fibonacci [0,1,1] e fatorial [0,1,2]. Então faz-se a multiplicação de 0x0, 1x1 e 1x2, onde cada resultado das três operações é mapeado para o alfabeto. Ou seja, 0x0=0 então se torna a letra "a", 1x1=1 se torna a letra b e 1x2=2 se torna a letra c. Logo, "abc" será adicionada como parte da nova palavra.

# OBS: é obrigatório o uso de recursão para calcular Fibonacci e fatorial

# OBS: na senha, sempre existirão apenas letras minúsculas

# Input

# A primeira linha será a senha alterada.

# senha

# Em seguida, um inteiro n que representa quantidade de palavras que serão transformadas e comparadas.

# n

# Por fim, as n palavras.

# palavra 1

# palavra 2

# ...

# palavra n

# Output

# Caso alguma das palavras transformadas seja igual a senha alterada:

# Achamos! Achamos a senha.

# Caso contrário:

# É... Temos que procurar mais.

# Examples

# Case: 1

# Input

# bcdibv1bcdibvbcdibv1bcbcdibvajabcmucoae1
# 4
# espacotempo
# buraconegro
# relatividade
# miller

# Output

# É... Temos que procurar mais.

# Case: 2

# Input

# bcdibcdibvajbcabcmucobcdibvajbcdibcdibvajbc
# 3
# relatividade
# einstein
# gargantua

# Output

# Achamos! Achamos a senha.


#definindo funções
#essa função codifica as letras e aplica o mod 11 para elas
def codificar (palavra):
	palavra_codificada = []
	for letra in palavra:
		palavra_codificada.append( (ord(letra) - 97) % 11 )
	return palavra_codificada

#funcao fatorial
def fat(termo):
	if termo == 0 :
		return 1 
	else:
		return termo * fat(termo-1)

#aplica fatorial em cada termo
def aplica_fat (num):
	lista_fat = []
		
	for i in range(0,num):
		lista_fat.append( fat(i) )
		
	return lista_fat

#funcao fibonacci
def fib(termo):
	if(termo == 0 or termo == 1):
		return termo
	else:
		return fib(termo-1) + fib(termo-2)

#aplica fibonacci pra cada termo
def aplica_fib (num):
	lista_fib = []
	for i in range(0,num):
		lista_fib.append( fib(i) )
	return lista_fib

#funcao que transforma os numeros em letras no final
def decodificar(palavra_codificada):
	senha = ''
	for cod in palavra_codificada:
		if cod == '1':
			senha += '1'
		else:
			if cod < 26:
				pass
			else:
				cod = cod % 26
			letra = chr(cod + 97)
			senha += letra
	return senha

#inicio do programa

senha = input()
n = int(input())

senha_certa = False

palavras = []
for i in range(n):
	palavra = codificar(input())
	palavras.append(palavra)

for palavra in palavras:
	senha_codificada = []
	for cod in palavra:
		fato = aplica_fat(cod)
		fibo = aplica_fib(cod)
		if cod == 0:
			senha_codificada.append('1')
		elif cod % 2 == 1:
			for n in range(len(fato)):
				senha_codificada.append((fato[n] * fibo[n]))
		else:
			for n in range(len(fato)):
				senha_codificada.append((fato[n] + fibo[n]))
		senha_teste = decodificar(senha_codificada)
	if senha_teste == senha:
		senha_certa = True

if senha_certa == True:
	print('Achamos! Achamos a senha.')
else:
	print('É... Temos que procurar mais.')








