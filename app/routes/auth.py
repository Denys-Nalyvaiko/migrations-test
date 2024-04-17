from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from starlette import status
from app.models.models import User
from app.dependencies import db_dependency

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


class RegisterUserRequest(BaseModel):
    email: str
    password: str


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(register_user_request: RegisterUserRequest, db: db_dependency):
    user = User(
        email=register_user_request.email,
        hashed_password=register_user_request.password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"email": user.email, "password": user.hashed_password}
