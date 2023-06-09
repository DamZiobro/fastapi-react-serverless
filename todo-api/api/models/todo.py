"""Implementation of Entities and Models based on the Clean Architecture principles"""

from typing import Union

from pydantic import (
    BaseModel,
    Field,
)


# Define a Todo model
class TodoModel(BaseModel):
    id: int
    task: str = Field(title="Title of the task", max_length=300)
    description: Union[str, None] = Field(
        default=None, title="Description of the task", max_length=500
    )
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
    task: str = Field(title="Title of the task", max_length=300)
    description: Union[str, None] = Field(
        default=None, title="Description of the task", max_length=500
    )

    class Config:
        schema_extra = {
            # example for autogenerated OpenAPI docs
            "example": {
                "task": "Wash car",
                "description": "Go to car wash and wash the car",
            }
        }
