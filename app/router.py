from .controllers import user_controller, auth_controller, address_controller
from fastapi import APIRouter


api = APIRouter()

@api.get("/health-check")
async def health_check():
    return {"message": "Health Check"}

api.include_router(user_controller.router)
api.include_router(address_controller.router)