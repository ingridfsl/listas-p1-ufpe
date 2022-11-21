# def igualdade(n,a,b):
	# for i in a.keys():
		# if a[i]in b:
			# igual=True
		# else:
			# igual=False

# def verifica_igualdade (a , b):
	# igual = True
	# for i in range(n):
		# if True:
			# dist = a[i]
			# b.remove(dist)
		# else:
			# igual = False
			# pass
	# return igual


n = int(input())

dist_gohan = input().split(' ')
dist_piccolo = input().split(' ')

dicionario ={'gohan':dist_gohan, 'piccolo':dist_piccolo}

igual= bool
x = list(dicionario.values())

for i in range(n):
	for i in x:
			if set(x[0]) == set(x[1]):
				igual = True
			else:
				igual=False


if igual:
	print('Dale Gohan!')
else:
	print("Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.")


# igual =bool
# for i in range(n):
	# if dist_gohan[i] in dist_piccolo:
		# igual=True
	# else:
		# igual=False
