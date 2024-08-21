from app.responses.base import BaseResponse

class CategoryResponse(BaseResponse):
    category_id: int
    code: str
    name: str
    description: str