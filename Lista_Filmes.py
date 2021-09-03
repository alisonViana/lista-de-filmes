from Modules.functions import *

# arquivo_csv = 'DB/ListaFilmes.csv'
arquivo_csv = 'Tests/teste2.csv'
opcao = menu()

while True:
	if opcao == 1:
		print('Adicionar filme\n')
		print(registrar(arquivo_csv))
	elif opcao == 2:
		print('Lista de filmes (ordenada por nome)\n')
		exibir(arquivo_csv, False)		# Ordena por nome
	elif opcao == 3:
		print('Lista de filmes (ordenada por ano)\n')
		exibir(arquivo_csv, True)		# Ordena por ano
	elif opcao == 4:
		print('Pesquisar filme\n')
		buscar(arquivo_csv)
	elif opcao == 5:
		print('Excluir filme\n')
		print(excluir(arquivo_csv))
	else:
		print('Opção inválida!\n')
	opcao = menu()
