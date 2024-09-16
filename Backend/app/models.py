#Pydantic and typing modules to define a model class for data validation and serialization in Python

from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: Optional[str]
    email: EmailStr
    username: str
