from fastapi import APIRouter,status,Depends
from app.responses.category import CategoryResponse
from app.config.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.category import CreateCategoryRequest
from app.services import category

category_router = APIRouter(prefix="/Category/api", tags=["Category"],responses={404: {"description": "Not Found!"}},)

@category_router.get("/")
def get_all_categories():
    return "Not Implemented"

@category_router.post("/",status_code=status.HTTP_201_CREATED, response_model=CategoryResponse)
async def create_category(data: CreateCategoryRequest, session: AsyncSession = Depends(get_session)):
    return await category.create_category(data,session)

@category_router.put("/{id}")
def update_category(id:int):
    return "Not Implemented"

@category_router.delete("/{id}")
def delete_category(id:int):
    return "Not Implemented"