"""Implementation of Entities and Models based on the Clean Architecture principles"""

from typing import Optional

from pydantic import BaseModel


# Define a Todo model
class TodoModel(BaseModel):
    id: int
    task: str
    description: Optional[str] = None
    completed: bool = False


# Define a Todo DTO
class TodoDTO(BaseModel):
    task: str
    description: Optional[str] = None
