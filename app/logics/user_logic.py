from app.models import User, Address
from app.schema import UserBaseSchema, UserUpdateSchema, UserWithAddressSchema, AddressBaseSchema
from app.logics import generate_password
from app.utils import mapping_null_values
from fastapi import HTTPException, status


class UserLogic:
    @staticmethod
    async def create(obj: UserBaseSchema):
        obj.password = generate_password(obj.password)
        user = await User.create(obj)

        return user

    @staticmethod
    async def get_by_id(id: int, username: str = None):
        user = await User.get_by_id(id)
        if user.username == username:
            return user
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    @staticmethod
    async def update(obj: UserUpdateSchema):
        if obj.password is not None:
            obj.password = generate_password(obj.password)

        user = await User.get_by_id(obj.id)
        user = mapping_null_values(dict(obj), user.__dict__)
        await User.update(user)

        return user

    @staticmethod
    async def delete(id: int):
        await User.get_by_id(id)
        await User.delete(id)

        return {"message": "User deleted successfully"}

    @staticmethod
    async def get_with_address(user_id: int):
        user = await User.get_by_id(user_id)
        if user:
            addresses = await Address.get_by_user_id(user.id)

            address_schemas = [
                AddressBaseSchema(
                    address=address.address,
                    province=address.province,
                    city=address.city,
                    postal_code=address.postal_code,
                    country=address.country,
                    is_primary=address.is_primary
                )
                for address in addresses
            ]

            return UserWithAddressSchema(
                id=user.id,
                full_name=user.full_name,
                username=user.username,
                email=user.email,
                role_id=user.role_id,
                addresses=address_schemas
            )
