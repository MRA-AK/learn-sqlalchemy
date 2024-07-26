
from sqlalchemy.orm import Session
from app.models.post import Post


class PostRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_post_by_id(self, post_id: int):
        return self.db.query(Post).filter(Post.id == post_id).scalar()
