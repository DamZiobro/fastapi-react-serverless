"""Implementation of Entities and Models based on the Clean Architecture principles"""

from typing import Optional

from pydantic import BaseModel


# Define a Todo model
class TodoModel(BaseModel):
    id: int
    task: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        schema_extra = {
            # example for autogenerated OpenAPI docs
            "example": {
                "id": 1,
                "task": "Wash car",
                "description": "Go to car wash and wash the car",
                "completed": False,
            }
        }


# Define a Todo DTO
class TodoDTO(BaseModel):
    task: str
    description: Optional[str] = None

    class Config:
        schema_extra = {
            # example for autogenerated OpenAPI docs
            "example": {
                "task": "Wash car",
                "description": "Go to car wash and wash the car",
            }
        }