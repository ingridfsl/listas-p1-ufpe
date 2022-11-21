# Problem Statement

# Em um dia bastante incomum na vida de Sheldon Cooper, ele resolve mostrar que é um homem com senso de humor bastante refinado e quer impressionar sua namorada, Amy Farrah, levando-a para um encontro.

# O date do casal aconteceu nada mais nada menos que num dos melhores clubes de comédia da Califórnia, o Scot Nery's Boobietrap - Los Angeles. 

# De acordo com as piadas contadas, Sheldon terá uma reação que indicará se ele gostou ou não do que foi dito.

# Agora cabe a você, uma pessoa desenvolvedora tão brilhante e grande fã do físico, montar um programa que dirá a reação final do ilustre PhD ao show, de acordo com as informações a seguir.

# Input 

# As entradas do programa não têm uma quantidade definida e se encerram sempre com a frase “Fim do Show!”, como é ilustrado abaixo:

# piada_1

# reação_1

# piada_2

# reação_2

# ...

# piada_N

# reação_N

# Fim do Show!

# Caso ele tenha gostado, sua reação será unicamente um sonoro “BAZINGA!”. Em caso contrário, ele terá qualquer outra reação.

# Output

# Para a saída do programa, temos três opções.

# Se o número de piadas boas foi bastante superior:
# “BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!”

# Se houve equilíbrio entre piadas boas e ruins:
# “Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!”

# Já se o número de piadas ruins foi bastante superior:
# “Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!”

# Considere que para que um tipo de reação às piadas seja “bastante superior” ao outro, elas devem ser mais de 60% do total de reações. Caso contrário, há equilíbrio entre boas e ruins.

# Examples

# Case: 1

# Input

# Por que uma galinha cruzou a Fita de Möbius? R: Para chegar do mesmo lado!
# BAZINGA!
# Um nêutron entra numa agência da Celpe e pede para fazerem a ligação da sua casa. O atendente responde, para você não tem energia elétrica!
# BAZINGA!
# O que o meu tio falou quando viu a mesa das sobremesas no último natal? R: É pavê ou pacumê?!
# Meh, essa é mais velha que a fome!
# O que é pior que ser atingido por um raio? R: ser atingido pelo diâmetro, que tem o dobro do tamanho!!!
# BAZINGA!
# O que aconteceu com o pintinho do cabeção? R: Foi ciscar e deu uma cambalhota!
# Nossa, essa não foi nem de longe digna de BAZINGA!
# O que três pontos não colineares disseram um ao outro? R: Temos um plano.
# BAZINGA!
# Fim do Show!

# Output

# BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!

# Case: 2

# Input

# O que 6 carbonos e 6 hidrogênios estão fazendo de mãos dadas na igreja? R: Benzeno.
# BAZINGA!
# O que um pato disse para o outro? R: Estamos empatados!
# Amy, o que está acontecendo????
# O que tem mais de 3 patas e menos de 4? R: O “Pi”olho.
# BAZINGA!
# O tio do pavê não existe. Pavê não tem tio, tem acento circunflexo.
# Tem como ficar pior do que isso?
# Fim do Show!

# Output

# Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!




piada_boa = 0
piada_ruim = 0
ativador = True

while (ativador):
	piada = input()
	if (piada != "Fim do Show!"):
		reacao = input()
		if (reacao == "BAZINGA!"):
			piada_boa +=1
		else:
			piada_ruim +=1
	else:
		ativador = False
else:
	if (piada_boa/piada_ruim > 1.6):
		print("BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!")
	elif (piada_ruim/piada_boa > 1.6):
		print("Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!")
	else:
		print("Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!")
