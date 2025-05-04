from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel

class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    hashed_password: str
    role: Role = Field(default=Role.USER)

class Project(SQLModel, table=True):
    __tablename__ = "projects"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    owner_id: int = Field(foreign_key="users.id")