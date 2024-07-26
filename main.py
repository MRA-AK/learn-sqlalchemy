from app.database import init_db, SessionLocal
from app.repositories import UserRepository, PostRepository


# Initialize the database
init_db()

def main():
    # Create a new session
    db = SessionLocal()
    
    try:
        user_repo = UserRepository(db)
        post_repo = PostRepository(db)
        
        user = user_repo.get_user_by_id(1)
        print(user.username)
        
        post = post_repo.get_post_by_id(1)
        print(post.id)

    finally:
        # Close the session
        db.close()

if __name__ == "__main__":
    main()
