from app.models import User
from app.schema import UserBaseSchema, UserUpdateSchema
from app.logics.auth_logic import AuthLogic
from app.utils import mapping_null_values


class UserLogic:
    @staticmethod
    async def create(obj: UserBaseSchema):
        obj.password = AuthLogic.generate_password(obj.password)
        user = await User.create(obj)

        return user

    @staticmethod
    async def get_by_id(id: int):
        return await User.get_by_id(id)

    @staticmethod
    async def update(obj: UserUpdateSchema):
        if obj.password is not None:
            obj.password = AuthLogic.generate_password(obj.password)

        user = await User.get_by_id(obj.id)
        user = mapping_null_values(dict(obj), user.__dict__)
        await User.update(user)

        return user

    @staticmethod
    async def delete(id: int):
        await User.get_by_id(id)
        await User.delete(id)

        return {"message": "User deleted successfully"}
