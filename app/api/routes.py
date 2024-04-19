from fastapi import APIRouter, Depends
from app.core.security import get_email_from_token
from app.schemas import PostCreate, UserOut, PostOut
from app.services import UserService, PostService

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register(code: str):
    return await UserService.register_with_google(code)

@router.post("/posts", response_model=PostOut)
async def create_post(post: PostCreate, email: str = Depends(get_email_from_token)):
    return await PostService.create_post(post, email)

@router.get("/users", response_model=list[UserOut])
async def get_users():
    return await UserService.get_users()

@router.get("/posts", response_model=list[PostOut])
async def get_posts():
    return await PostService.get_posts()