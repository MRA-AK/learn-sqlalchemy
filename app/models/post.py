from sqlalchemy import Column, Integer, ForeignKey, REAL, String, TIMESTAMP, CheckConstraint, func
from sqlalchemy.orm import relationship
from app.database import Base


class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.current_timestamp(), nullable=False, onupdate=func.current_timestamp())
    url = Column(String(200), nullable=False)
    caption =  Column(String(240))
    lat = Column(REAL, CheckConstraint('lat IS NULL OR (lat >= -90 AND lat <= 90)', name='lat_range_check'))
    lng = Column(REAL, CheckConstraint('lng IS NULL OR (lng >= -180 AND lng <= 180)', name='lng_range_check'))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    user = relationship("User", back_populates="posts")
