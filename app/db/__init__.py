from prisma import Prisma
from prisma import models

db = Prisma(auto_register=True)

User = models.User
Post = models.Post