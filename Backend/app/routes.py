from fastapi import APIRouter, HTTPException, Depends
from app.models import UserCreate, UserLogin, User
from app.database import get_user_collection
from app.utils import hash_password, verify_password
from app.auth import create_access_token
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection

router = APIRouter()

# Register route
@router.post("/register")
async def register(user: UserCreate):
    users: AsyncIOMotorCollection = await get_user_collection()
    existing_user = await users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_data = {
        "email": user.email,
        "username": user.username,
        "password": hash_password(user.password)
    }
    new_user = await users.insert_one(user_data)
    created_user = await users.find_one({"_id": new_user.inserted_id})
    
    return {"id": str(created_user["_id"]), "email": created_user["email"], "username": created_user["username"]}

# Login route
@router.post("/login")
async def login(user: UserLogin):
    users: AsyncIOMotorCollection = await get_user_collection()
    existing_user = await users.find_one({"email": user.email})
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": str(existing_user["_id"])})
    
    return {"access_token": token, "token_type": "bearer"}