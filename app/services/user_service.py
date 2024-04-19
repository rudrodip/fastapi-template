import requests
from app.core import settings
from app.db import User, db
from app.core.security import create_token
from app.schemas import UserOut

class UserService:
    @staticmethod
    async def register_with_google(code: str):
        token_url = "https://accounts.google.com/o/oauth2/token"
        data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }
        response = requests.post(token_url, data=data)
        access_token = response.json().get("access_token")

        user_info = requests.get(
            "https://www.googleapis.com/oauth2/v1/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
        )

        user = await User.prisma().create(
            data={
                'name': user_info.json().get('name'),
                'email': user_info.json().get('email'),
            },
        )

        token = create_token(user.email)
        return UserOut.model_validate(user), token

    @staticmethod
    async def get_users():
        await db.connect()
        user = await User.prisma().find_many()
        await db.disconnect()
        return user