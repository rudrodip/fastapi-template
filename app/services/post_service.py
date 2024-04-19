from app.db import Post, db
from app.schemas import PostCreate, PostOut

class PostService:
    @staticmethod
    async def create_post(post: PostCreate, author_email: str):
        await db.connect()
        post_created = await Post.prisma().create(
            data={
                'title': post.title,
                'content': post.content,
                'author': {'connect': {'email': author_email}}
            }
        )
        await db.disconnect()
        return PostOut.model_validate(post_created)

    @staticmethod
    async def get_posts():
        await db.connect()
        posts = await Post.prisma().find_many()
        await db.disconnect()
        return posts