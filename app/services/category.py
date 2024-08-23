from app.config.settings import get_settings
from app.schemas.category import CreateCategoryRequest,UpdateCategoryRequest
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.category import Category
from sqlalchemy.future import select
from fastapi import HTTPException,status
from uuid import UUID

settings = get_settings()

async def create_category(data: CreateCategoryRequest, session: AsyncSession):
    stmt = select(Category).filter(Category.code == data.code)
    result = await session.execute(stmt)
    category_exist = result.scalars().first()

    if category_exist:
        raise HTTPException(status_code=400, detail="Category already exists.")
    
    new_category = Category(
        code = data.code,
        name = data.name,
        description = data.description
    )
    
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    
    return new_category

async def get_all_categories(session: AsyncSession):
    stmt = select(Category)
    result = await session.execute(stmt)
    categories = result.scalars().all()
    
    return categories

async def get_category_by_id(id: UUID, session: AsyncSession) -> Category:
    stmt = select(Category).where(Category.category_id == id)
    result = await session.execute(stmt)
    category = result.scalars().first()

    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    
    return category

async def update_category(id: UUID, data: UpdateCategoryRequest, session: AsyncSession):
    stmt = select(Category).where(Category.category_id == id)
    result = await session.execute(stmt)
    category = result.scalars().first()

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    category.code = data.code
    category.name = data.name
    category.description = data.description

    await session.commit()
    await session.refresh(category)  

    return category

async def delete_category(id:UUID,session: AsyncSession):
    stmt = select(Category).where(Category.category_id == id)
    result = await session.execute(stmt)
    category = result.scalars().first()

    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    
    await session.delete(category)
    await session.commit()
    return {"detail": "Category deleted successfully"}