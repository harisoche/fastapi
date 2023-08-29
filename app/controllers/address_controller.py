from fastapi import APIRouter, status
from app.logics import AddressLogic
from app.schema import AddressBaseSchema, AddressResponseSchema, AddressUpdateSchema


router = APIRouter(
    prefix="/address",
    tags=["address"]
    )

@router.post("/", response_model=AddressResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_address(address: AddressBaseSchema):
    return await AddressLogic.create(address)

@router.get("/{id}", response_model=AddressResponseSchema, status_code=status.HTTP_200_OK)
async def get_address_by_id(id: int):
    return await AddressLogic.get_by_id(id)

@router.put("/", response_model=AddressResponseSchema, status_code=status.HTTP_200_OK)
async def update_address(address: AddressUpdateSchema):
    return await AddressLogic.update(address)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(id: int):
    return await AddressLogic.delete(id)