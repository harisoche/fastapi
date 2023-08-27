from fastapi import APIRouter, status
from app.logics import UserLogic
from app.schema import UserBaseSchema, UserResponseSchema, UserUpdateSchema


router = APIRouter(
    prefix="/users",
    tags=["users"]
    )

@router.post("/", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBaseSchema):
    return await UserLogic.create(user)

@router.get("/{id}", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def get_user_by_id(id: int):
    return await UserLogic.get_by_id(id)

@router.put("/", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def update_user(user: UserUpdateSchema):
    return await UserLogic.update(user)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int):
    return await UserLogic.delete(id)