from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class UserOut(BaseModel):
    id: str
    name: str
    email: str
    model_config = {
        'from_attributes': True
    }

class PostOut(BaseModel):
    id: str
    title: str
    content: str
    author_email: str
    model_config = {
        'from_attributes': True
    }