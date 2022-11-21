# Problem Statement

# Você foi chamado pelo professor Carvalho para o ajudar com sua pesquisa para registrar e documentar todos os Pokémon. Ele teve uma ideia genial de um dispositivo que armazena as informações do Pokémon, e as cita, quando solicitada, chamada de Pokédex.

# O professor Carvalho o recrutou para desenvolver o programa da Pokédex, para isso, você deve criar um algoritmo, que recebe um número indefinido de entradas com os comandos ‘ADD’ ou ‘DESC’.

# Input

# Ao receber o comando ‘ADD’ também virá o nome do Pokémon que deve ser adicionado, e depois, mais um input com a descrição do Pokémon.

# Ex.:

# ADD Charmander

# Tem preferência por coisas quentes. Quando chove, diz-se que o vapor jorra da ponta de sua cauda.

# Ao receber o comando ‘DESC’, também virá em seguida o nome do Pokémon que que ele quer a descrição:

# Ex.:

# DESC Charmander

# Dica: Use try/except com EOFError para pegar as entradas.

# Output

# Ao receber o comando ‘ADD’, caso o Pokémon, já tenha sido adicionado, a Pokédex deverá printar, ‘Pokémon já adicionado na Pokédex’.
# Caso o Pokémon não tenha sido adicionado ainda, a Pokédex tem que adicionar, e printar, ‘Pokémon adicionado com sucesso’
# Ao receber o comando ‘DESC’, caso o pokémon não tenha sido adicionado ainda, a Pokédex deve printar, ‘Ainda não há registro desse Pokémon’.
# Caso o Pokémon já tenha sido adicionado, ela deve printar a descrição do Pokémon escolhido.
# Examples

# Case: 1

# Input

# ADD Charmander
# A chama em sua cauda indica a força vital de Charmander, se estiver saudável, a chama queima brilhantemente.
# ADD Bulbassauro
# A semente em suas costas é cheia de nutrientes. A semente fica cada vez maior à medida que seu corpo cresce.
# ADD Squirtle
# Quando retrai seu longo pescoço em sua concha, esguicha água com força vigorosa.
# DESC Charmander
# DESC Bulbassauro
# DESC Squirtle

# Output

# Pokémon adicionado com sucesso
# Pokémon adicionado com sucesso
# Pokémon adicionado com sucesso
# A chama em sua cauda indica a força vital de Charmander, se estiver saudável, a chama queima brilhantemente.
# A semente em suas costas é cheia de nutrientes. A semente fica cada vez maior à medida que seu corpo cresce.
# Quando retrai seu longo pescoço em sua concha, esguicha água com força vigorosa.


pokedex = {}

while True:
	try:
		comando, nome = input().split(' ')
		if "ADD" == comando:
			if nome not in pokedex:
				pokedex.get(nome)
				descricao = input()
				pokedex[nome] = descricao
				print("Pokémon adicionado com sucesso")
			else:
				print("Pokémon já adicionado na Pokédex")
		elif "DESC" == comando:
			if nome not in pokedex:
				print("Ainda não há registro desse Pokémon")
			else:
				print(pokedex[nome])
	except EOFError:
		break

