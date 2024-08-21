from sqlalchemy import Column, Integer, String, Text
from app.config.database import Base

class Category(Base):
    __tablename__ = "categories"
    
    category_id = Column(Integer, primary_key=True, index=True)
    code = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
