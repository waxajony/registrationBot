import sqlite3

class Database:

	def __init__(self, db_name):
		self.conn = sqlite3.connect(db_name)
		self.cursor = self.conn.cursor()

	def add_user(self, tg_id, tg_name, tg_lastname, username):
		sql = '''
			INSERT INTO RegUsers(tg_id, tg_name, tg_lastname, username)
			VALUES (?,?,?,?);
		'''
		self.cursor.execute(sql, (tg_id, tg_name, tg_lastname, username))
		self.conn.commit()

	def get_user(self, tg_id):
		users = self.cursor.execute(f"SELECT * FROM users WHERE tg_id=?;", (tg_id,))
		return users.fetchone()

	def update_user(self, tg_id, full_name, phone, email, birthday):
		self.cursor.execute(f"UPDATE users SET full_name=?, phone=?, email=?, birthday=?"
							f"  WHERE tg_id=?;", (tg_id, full_name, phone, email, birthday))
		self.conn.commit()


	def __del__(self):
		self.cursor.close()
		self.conn.close()