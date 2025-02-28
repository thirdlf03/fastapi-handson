from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
	title: str
	content: str

class TodoUpdate(BaseModel):
	title: Optional[str] = None
	content: Optional[str] = None