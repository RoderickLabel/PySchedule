import sqlite3
import datetime

class agenda_model:

	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cursor = self.conn.cursor()

	def listar(self):
		return self.cursor.execute('SELECT nome, email, telefone FROM contatos ORDER BY nome, id')

	def buscar(self, email):
		return self.cursor.execute("SELECT id FROM contatos WHERE email = ':email' ", {"email" : email}).fetchone()

	def incluir(self, contato):
		self.cursor.execute("INSERT INTO contatos (nome, email, telefone, data_inclusao) VALUES (?, ?, ?, ?)", 
			(contato[0], contato[1], contato[2], datetime.datetime.now()))
		self.conn.commit()

	def alterar(self, idx, contato):
		self.cursor.execute("UPDATE contatos SET nome = :nome, email = :email, telefone = :telefone WHERE id = :idx", 
			(contato[0], contato[1], contato[2], idx))
		self.conn.commit()

	def excluir(self, id):
		self.cursor.execute("DELETE FROM contatos WHERE id = :id", {"id" : id})
		self.conn.commit()