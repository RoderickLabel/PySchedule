class cli_agenda:

	def __init__(self):
		self.larguraPrompt = 70
	
	def header_app(self, agenda_title):
		agenda_title = str(agenda_title)
		print(agenda_title.center(self.larguraPrompt, '-'))
		print()

	def mostrar_ajuda(self):
		help_message = "1 - Listar, 2 - Incluir, 3 - Alterar, 4 - Excluir, 5 - Pesquisar,  6 - Ajuda"
		print(help_message)
		print()

	def renderiza_linha(self):
		print('-'.center(self.larguraPrompt, '-'))

	def renderiza_tabela_contatos(self, contatos):
		self.renderiza_linha()
		print('|' + ' CONTATOS ATUAIS '.center(self.larguraPrompt - 2, ' ') + '|')
		self.renderiza_linha()
		for contato in contatos:
			self.renderiza_linha()
			print(    "| Nome:".ljust(15, ' ') + contato[0].ljust(54, ' ') + '|')
			print(   "| Email:".ljust(15, ' ') + contato[1].ljust(54, ' ') + '|')
			print("| Telefone:".ljust(15, ' ') + contato[2].ljust(54, ' ') + '|')
			self.renderiza_linha()

	def build_contato_input(self):
		nome = input("Digite o Nome:".ljust(19, ' '))
		email = input("Digite o Email:".ljust(19, ' '))	
		telefone = input("Digite o Telefone:".ljust(19, ' '))
		return (nome, email, telefone)

	def show_intro(self):
		print ('intro')