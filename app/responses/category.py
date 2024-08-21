from app.responses.base import BaseResponse
from uuid import UUID

class CategoryResponse(BaseResponse):
    category_id: UUID
    code: str
    name: str
    description: str