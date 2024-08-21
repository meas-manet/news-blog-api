from pydantic import BaseModel
from uuid import UUID


class CreateCategoryRequest(BaseModel):
    code: str
    name: str
    description: str

class UpdateCategoryRequest(BaseModel):
    code: str
    name: str
    description: str