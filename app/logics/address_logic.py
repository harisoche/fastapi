from app.models import Address
from app.schema import AddressBaseSchema, AddressUpdateSchema
from app.utils import mapping_null_values


class AddressLogic:
    @staticmethod
    async def create(obj: AddressBaseSchema):
        address = await Address.create(obj)

        return address

    @staticmethod
    async def get_by_id(id: int):
        return await Address.get_by_id(id)

    @staticmethod
    async def update(obj: AddressUpdateSchema):
        address = await Address.get_by_id(obj.id)
        address = mapping_null_values(dict(obj), address.__dict__)
        await Address.update(address)

        return address

    @staticmethod
    async def delete(id: int):
        await Address.get_by_id(id)
        await Address.delete(id)

        return {"message": "Address deleted successfully"}
