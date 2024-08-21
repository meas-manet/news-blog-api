from sqlalchemy import Column, Integer, String, Text
from app.config.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Category(Base):
    __tablename__ = "categories"
    
    category_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    code = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
