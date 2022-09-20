from enum import Enum

from pydantic import BaseModel, EmailStr


class Roles(Enum):
    senior = "senior"
    admin = "admin"
    junior = "junior"




class UserSchema(BaseModel):
    email: EmailStr
    username: str
    password: str
    is_active: bool = True
    role: Roles = "admin"

    class Config:
        orm_mode = True