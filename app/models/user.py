from sqlalchemy import Column, Integer, String, TIMESTAMP, CheckConstraint, func
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.current_timestamp(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.current_timestamp(), nullable=False, onupdate=func.current_timestamp())
    username = Column(String(30), nullable=False)
    bio = Column(String(400))
    avatar = Column(String(200))
    phone = Column(String(25))
    email = Column(String(40))
    password = Column(String(50))
    status = Column(String(15))

    posts = relationship("Post", back_populates="user")

    __table_args__ = (
        CheckConstraint(
            'COALESCE(phone, email) IS NOT NULL', 
            name='phone_or_email_not_null'
        ),
    )
