from pydantic import BaseModel

from app.db.models import Role

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: Role = Role.USER

class UserRead(UserBase):
    id: int
    role: Role