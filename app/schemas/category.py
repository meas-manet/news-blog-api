from pydantic import BaseModel

class CreateCategoryRequest(BaseModel):
    code: str
    name: str
    description: str