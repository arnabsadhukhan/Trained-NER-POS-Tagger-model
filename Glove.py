import sqlite3 as sql
import numpy as np
class Golve_embedding:
	def __init__(self,database_name,vec_dimention=25):
		self.vec_dimention = vec_dimention
		self.con = sql.connect(database_name)
		self.curs = self.con.cursor() 
	def tokenizer(self,text):
		s = ''
		for i in range(len(text)-1):
			if text[i]!=' ' and (text[i].isalpha() or text[i].isdigit())  and (text[i+1].isalpha() or text[i+1].isdigit()):
				s+=text[i]
			else:
				if text[i]!=' ':
					s+=text[i]+' '
		return s.split()
	def fetch(self,word):
		self.curs.execute(f'''SELECT * FROM glove25d where word="{word.lower()}"''')
		row = self.curs.fetchall()
		try:
			return  np.array(row[0][1:self.vec_dimention+1])
		except:return np.zeros((25))
	def fetch_all(self,word_list):
		result = []
		for word in word_list:
			self.curs.execute(f'''SELECT * FROM glove25d where word="{word.lower()}"''')
			row = self.curs.fetchall()
			try:
				result.append(np.array(row[0][1:self.vec_dimention+1]))
			except:
				result.append(np.zeros((25)))
		return np.array(result)
	def close(self):
		self.con.close()