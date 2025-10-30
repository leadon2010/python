from models.post import Post, db
from typing import List, Optional

class PostService:
    @staticmethod
    def get_all_posts() -> List[Post]:
        return Post.query.order_by(Post.created_at.desc()).all()
    
    @staticmethod
    def get_post_by_id(post_id: int) -> Optional[Post]:
        return db.get_or_404(Post, post_id)
    
    @staticmethod
    def create_post(title: str, content: str) -> Post:
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return new_post
    
    @staticmethod
    def update_post(post_id: int, title: str, content: str) -> Post:
        post = db.get_or_404(Post, post_id)
        post.title = title
        post.content = content
        db.session.commit()
        return post
    
    @staticmethod
    def delete_post(post_id: int) -> None:
        post = db.get_or_404(Post, post_id)
        db.session.delete(post)
        db.session.commit()