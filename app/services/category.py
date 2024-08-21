from app.config.settings import get_settings
from app.schemas.category import CreateCategoryRequest
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.category import Category
from sqlalchemy.future import select
from fastapi import HTTPException

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