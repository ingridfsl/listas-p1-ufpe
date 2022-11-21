#Problem Statement

#Sheldon Lee Cooper se prova constantemente, na série, um dos homens mais inteligentes do mundo desde criança, mas para conseguir o seu objetivo final, ganhar o Nobel de Física, ele precisa da sua ajuda.

#Para isso, Sheldon pediu para você listar as conquistas acadêmicas que ele terá na sua vida até chegar no prêmio Nobel. 

#Você terá que se certificar não só quais são os feitos que Sheldon realizou, mas se eles estão vindo na ordem cronologicamente correta também, sendo eles, já em ordem:

#'Começou a Trabalhar na Caltech', 'Trabalho sobre a String Theory', 'Ganhar o Chancellor de ciência', 'Pensar na Teoria de Cooper-Hofstader', 'Criou a Super Assimetria' e 'Ganhar o Nobel'.

#Sheldon é conhecido pelas suas pegadinhas também, então, se assim que ele completar um desses feitos, a palavra 'Bazinga' for recebida, o feito deve ser desconsiderado, e precisará ser feito novamente para ser validado. Atenção, se você receber um Bazinga sem ser logo após ele ter ‘avançado’ mais um feito na sua carreira, ele não deve retroceder de novo.

#Sheldon também pode ser um pouco duro com seus amigos, então, se ele xingar Howard, Leonard ou Raj, você deve repreender ele!

#Obs.: Se você receber algum desses feitos na ordem errada, ele não deve ser considerado como feito, e só como uma mensagem recebida.

#Input

#Você receberá vários inputs em forma de mensagem, e só não irá mais recebê-los quando Sheldon ganhar o Nobel ou quando receber a mensagem: ‘É o fim da Estrada pra Sheldon Cooper’.

#Mensagem 1
#Mensagem 2
#Mensagem 3
#.
#.
#.
#Mensagem N
#Output

#Se você receber os xingamentos: 'Tinha que ser o engenheiro sem Phd do Wolowitz' ou 'Leonard seu anão covarde' ou 'Tu é muito burro Raj’, você deve printar:

#Não xingue seus amigos Sheldon!

#No fim de tudo, se Sheldon desistir antes mesmo de Começou a Trabalhar na Caltech, deve ser printado:

#Que potencial desperdiçado...

#Se ele ainda estiver apenas Trabalhando na String Theory ou na Caltech, printe:

#Tão perto, mas tão longe

#Se ele ainda estiver até só ter ganho o Chancellor ou pensado na Teoria de Cooper-Hofstader, printe:

#Não desista Sheldon, você ainda têm muito para alcançar!

#Se ele tiver pensado na Super Assimetria, mas ainda não ganho o Nobel, printe:

#Nãoooooo, esse momento ia ser seu Sheldon

#Se ele tiver ganho o Nobel, printe:

#Você conseguiu Sheldon, o Nobel é seu!!!

#Examples

#Case: 1

#Input

#Começou a Trabalhar na Caltech
#Trabalho sobre a String Theory
#Tinha que ser o engenheiro sem Phd do Wolowitz
#Ganhar o Chancellor de ciência
#Bazinga
#Ganhar o Chancellor de ciência
#Pensar na Teoria de Cooper-Hofstader
#Zoar a Penny
#Bazinga
#Criou a Super Assimetria
#Ganhar o Nobel

#Output

#Não xingue seus amigos Sheldon!
#Você conseguiu Sheldon, o Nobel é seu!!!

#Case: 2

#Input

#Começou a Trabalhar na Caltech
#Bazinga
#Leonard seu anão covarde
#Começou a Trabalhar na Caltech
#Trabalho sobre a String Theory
#Amy é linda demais
#Pensar na Teoria de Cooper-Hofstader
#Bazinga
#Tu é muito burro Raj
#Bazinga
#É o fim da Estrada pra Sheldon Cooper

#Output

#Não xingue seus amigos Sheldon!
#Não xingue seus amigos Sheldon!
#Tão perto, mas tão longe


mensagem = input()
count = 0

while (count ==0 and mensagem != "É o fim da Estrada pra Sheldon Cooper"):
	if (mensagem == "Tinha que ser o engenheiro sem Phd do Wolowitz" or mensagem == "Leonard seu anão covarde" or mensagem == "Tu é muito burro Raj"):
		print ("Não xingue seus amigos Sheldon!")
	elif (mensagem == "Começou a Trabalhar na Caltech"):
		count =1
	mensagem = input()
	if (mensagem == "Bazinga"):
		count =0

while (count ==1 and mensagem != "É o fim da Estrada pra Sheldon Cooper"):
	if (mensagem == "Tinha que ser o engenheiro sem Phd do Wolowitz" or mensagem == "Leonard seu anão covarde" or mensagem == "Tu é muito burro Raj"):
		print ("Não xingue seus amigos Sheldon!")
	elif (mensagem == "Trabalho sobre a String Theory"):
		count =2
	mensagem = input()
	if (mensagem == "Bazinga"):
		count =1 

while (count ==2 and mensagem != "É o fim da Estrada pra Sheldon Cooper"):
	if (mensagem == "Tinha que ser o engenheiro sem Phd do Wolowitz" or mensagem == "Leonard seu anão covarde" or mensagem == "Tu é muito burro Raj"):
		print ("Não xingue seus amigos Sheldon!")
	elif (mensagem == "Ganhar o Chancellor de ciência"):
		count =3
	mensagem = input()
	if (mensagem == "Bazinga"):
		count =2

while (count ==3 and mensagem != "É o fim da Estrada pra Sheldon Cooper"):
	if (mensagem == "Tinha que ser o engenheiro sem Phd do Wolowitz" or mensagem == "Leonard seu anão covarde" or mensagem == "Tu é muito burro Raj"):
		print ("Não xingue seus amigos Sheldon!")
	elif (mensagem == "Pensar na Teoria de Cooper-Hofstader"):
		count =4
	mensagem = input()
	if (mensagem == "Bazinga"):
		count =3

while (count ==4 and mensagem != "É o fim da Estrada pra Sheldon Cooper"):
	if (mensagem == "Tinha que ser o engenheiro sem Phd do Wolowitz" or mensagem == "Leonard seu anão covarde" or mensagem == "Tu é muito burro Raj"):
		print ("Não xingue seus amigos Sheldon!")
	elif (mensagem == "Criou a Super Assimetria"):
		count =5
	mensagem = input()
	if (mensagem == "Bazinga"):
		count =4
	
while (count ==5 and mensagem != "É o fim da Estrada pra Sheldon Cooper"):
	if (mensagem == "Tinha que ser o engenheiro sem Phd do Wolowitz" or mensagem == "Leonard seu anão covarde" or mensagem == "Tu é muito burro Raj"):
		print ("Não xingue seus amigos Sheldon!")
	if (mensagem == "Ganhar o Nobel"):
		count =6
	else:
		mensagem = input()
	if (mensagem == "Bazinga"):
	  count =5	
	
if (count == 0):
	print("Que potencial desperdiçado...")

elif (count ==1 or count==2):
	print("Tão perto, mas tão longe")
elif (count==3 or count == 4):
	print("Não desista Sheldon, você ainda têm muito para alcançar!")
elif (count==5):
	print("Nãoooooo, esse momento ia ser seu Sheldon")
elif (count==6):
	print("Você conseguiu Sheldon, o Nobel é seu!!!")
