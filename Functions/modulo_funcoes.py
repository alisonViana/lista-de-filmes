import os
import platform

#Menu de opções	
def menu():
	try:
		opcao = int(input(''' Menu:
	<1> Para adicionar filme
	<2> Para exibir os filmes ordenados por nome
	<3> Para exibir os filmes ordenados por ano
	<4> Para pesquisar um filme
	<5> Para excluir um filme
 -> '''))
	except ValueError:
		print(' Utilize apenas dígitos!')
	else: 
		clear()
		return opcao

#Inserir novos filmes
def registrar(arquivo):
	lista = []
	resp = 'S'
	while resp == 'S':
		try:
			filme = [input('\n Digite o nome do filme: ').title().replace(',',' '), int(input(' Digite o ano do filme: '))]
		except ValueError:	#caso seja digitado caracter diferente de dígito, executa esse trecho
			print(' Verifique o ano inserido e tente novamente!')
		else:	#se não, executa esse trecho
			lista.append(filme)	#lista de listas		
			resp = input(' Digite <S> para inserir um novo filme: ').upper()				
	return persistir(lista, arquivo)
	
def persistir(lista, arquivo):
	with open(arquivo, 'a') as lista_csv:
		for filme in lista:
			lista_csv.write(filme[0] + ',' + str(filme[1]) + '\n')
	return ' Persistido com sucesso! \n'
	
#Exibir a lista de filmes
def exibir(arquivo, ordem_ano):
	lista_ordenada = ordenar(arquivo, ordem_ano)
	formata_exibicao(lista_ordenada)

#Exibe a lista formatada
def formata_exibicao(lista_ordenada):
	print('')
	for filme in lista_ordenada:
		print(f' {filme[0]:.<50} ({filme[1][:len(filme[1])-1]})')	#elimina o '\n' do final
	print(f'\n Total:{len(lista_ordenada)} filmes\n')

def formata_exibicao_indice(lista_ordenada):
	print('')
	for filme in lista_ordenada:
		#formato = [(índice,[nome, ano])]
		print(f' {filme[0]} - {filme[1][0]:.<50} ({filme[1][1][:-1]})')	#elimina o '\n' do final
	print(f'\n Total:{len(lista_ordenada)} filmes\n')


#Converte o CSV em lista e ordena
def ordenar(arquivo, ordem_ano):
	lista_filmes = []
	with open(arquivo, 'r', encoding='utf-8') as lista_csv:
		lista = lista_csv.readlines()
	for linha in lista:
		filme = linha.split(',')	#cria uma tupla
		lista_filmes.append(filme)	
#ordena por ano	
	if ordem_ano == True:	
		lista_filmes = sorted(lista_filmes, key = lambda x: x[1])
#ordena por nome	
	else:
		lista_filmes = sorted(lista_filmes)
	return lista_filmes	#lista de tuplas

#Buscar um filme
def buscar(arquivo):
	lista_ordenada = ordenar(arquivo, False)
	resultado = []
	try:
		tipo_busca = int(input('''\nDigite:
	<1> Para pesquisar por nome
	<2> Para pesquisar por ano 
 -> '''))
	except ValueError:
		print(' Opção inválida!\n')
	else:
#pesquisa por nome
		if tipo_busca == 1:
			pesquisa = input('\n Digite o nome a ser pesquisado: ')
			for filme in lista_ordenada:
				if pesquisa.lower() in filme[0].lower():
					resultado.append(filme)
			formata_exibicao(resultado)		
#pesquisa por ano
		elif tipo_busca == 2:
			pesquisa = input(' Digite o ano a ser pesquisado: ')
			for filme in lista_ordenada:
				if str(filme[1][:len(filme[1])-1]) in pesquisa:
					resultado.append(filme)
			formata_exibicao(resultado)	
		else:
			print(' Opção inválida!\n')		

#Excluir filme
def excluir(arquivo):
	lista_ordenada = ordenar(arquivo, False)
	lista_numerada = list(enumerate(lista_ordenada))
#formato => lista_numerada = [(índice,[nome, ano])]
	formata_exibicao_indice(lista_numerada)
	try:
		indice = int(input(' Qual o índice do filme que você deseja excluir? '))
	except ValueError:
		return ' Verifique o índice inserido e tente novamente.\n'
	if indice > len(lista_numerada):
		return ' O índice não existe, tente novamente.\n '
	resposta = input(f' Deseja excluir o filme {lista_numerada[indice][1][0]} ({lista_numerada[indice][1][1][:4]})? (S/N) ').upper()
	if resposta == 'S':
		del lista_numerada[indice]
		with open(arquivo, 'w') as lista_csv:
			for filme in lista_numerada:
				lista_csv.write(filme[1][0] + ',' + str(filme[1][1]))
		status = ' Filme excluído!\n'
	else:
		status = ' Operação cancelada...\n'					
	return status 

#Limpar o console
def clear():
	sistema = platform.system().lower()
	if sistema == 'linux':
		os.system('clear')
	elif sistema == 'windows':
		os.system('cls')