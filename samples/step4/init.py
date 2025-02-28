import sqlite3

sql_statements = [
	"""CREATE TABLE IF NOT EXISTS todos (
		id INTEGER PRIMARY KEY,
		title text NOT NULL,
		content text NOT NULL
	);""",

	"""INSERT INTO todos (title, content) 
			VALUES ("First Task", "Hello World")
			"""
]

try:
	with sqlite3.connect('todo.db') as conn:
		cursor = conn.cursor()
		
	for statement in sql_statements:
		cursor.execute(statement)
		
	conn.commit()
	
	print("Table Create")
except sqlite3.OperationalError as e:
	print("Failed to create tables:", e)