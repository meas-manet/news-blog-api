from fastapi import APIRouter,status,Depends
from app.responses.category import CategoryResponse
from app.config.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.category import CreateCategoryRequest,UpdateCategoryRequest
from app.services import category
from uuid import UUID

category_router = APIRouter(prefix="/Category/api", tags=["Category"],responses={404: {"description": "Not Found!"}},)

@category_router.get("/")
async def get_all_categories(session: AsyncSession = Depends(get_session)):
    return await category.get_all_categories(session)

@category_router.get("/{id}",response_model=CategoryResponse)
async def get_category_by_id(id:UUID,session: AsyncSession = Depends(get_session)):
    return await category.get_category_by_id(id,session)

@category_router.post("/",status_code=status.HTTP_201_CREATED, response_model=CategoryResponse)
async def create_category(data: CreateCategoryRequest, session: AsyncSession = Depends(get_session)):
    return await category.create_category(data,session)

@category_router.put("/{id}",status_code=status.HTTP_200_OK,response_model=CategoryResponse)
async def update_category(id:UUID,data: UpdateCategoryRequest, session: AsyncSession = Depends(get_session)):
    return await category.update_category(id,data,session)

@category_router.delete("/{id}")
async def delete_category(id:UUID,session: AsyncSession = Depends(get_session)):
    return await category.delete_category(id,session)