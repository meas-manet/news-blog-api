from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from app.config.database import Base
import uuid
from datetime import datetime

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    activity_log_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    entity_name = Column(String, nullable=True)
    activity_type_no = Column(Integer, nullable=False)
    entity_identifier = Column(UUID(as_uuid=True), nullable=True)
    property_name = Column(String, nullable=True)
    old_value = Column(Text, nullable=True)
    new_value = Column(Text, nullable=True)
    user_id = Column(UUID(as_uuid=True), nullable=True)
    user_name = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.now, nullable=False)

