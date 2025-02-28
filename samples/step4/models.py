from sqlalchemy import Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Todo(Base):
	__tablename__ = 'todos'
	
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(Text, nullable=False)
	content = Column(Text, nullable=False)