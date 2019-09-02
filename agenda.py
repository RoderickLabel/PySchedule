# -*- coding: UTF-8 -*-
import src.cli_agenda as cli
import src.agenda_model as model

class agenda:
	
	def __init__(self):
		self.main()

	def main(self):

		self.cli = cli.cli_agenda()
		self.agenda = model.agenda_model("data/agenda.db")
		self.cli.header_app(" PyAgenda CLI ")
		self.cli.mostrar_ajuda()
		comando = input("Insira o comando para continuar: ")
		if comando == "1":	
			self.comandoListar()
		elif comando == "2":
			self.comandoIncluir()
		elif comando == "3":	
			self.comandoAlterar()
		elif comando == "4":	
			self.comandoExcluir()
		elif comando == "5":
			self.comandoPesquisar();
		elif comando == "6":
			self.comandoAjudar()

	def comandoListar(self):
		self.cli.renderiza_tabela_contatos(self.agenda.listar())

	def comandoIncluir(self):
		print("Comando Incluir acionado!")
		contato = self.cli.build_contato_input()
		self.agenda.incluir(contato)
		self.cli.renderiza_tabela_contatos(self.agenda.listar())

	def comandoAlterar(self):
		email = input("Digite o email do contato que deseja alterar! ")
		idx = self.agenda.buscar(email)
		contato = self.cli.build_contato_input()
		self.agenda.alterar(idx[0], contato)
		self.cli.renderiza_tabela_contatos(self.agenda.listar())

	def comandoExcluir(self):
		email = input("Digite o email do contato que deseja excluir! ")
		idx = self.agenda.buscar(email)
		self.agenda.excluir(idx[0])
		self.cli.renderiza_tabela_contatos(self.agenda.listar())

	def comandoPesquisar(self):
		email = input("Digite o email do contato que deseja pesquisar! ")	
		try: 
			idx = self.agenda.buscar(email)			
			print("Id do contato: " + str(idx))
		except :		 	
			print("O e-mail \"" + email + "\" nao foi encontrado. Verifique se ele realmente consta na listagem...")

	def comandoAjudar(self):
		self.cli.mostrar_ajuda()

app = agenda()