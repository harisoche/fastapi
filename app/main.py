from fastapi import FastAPI
from .database import db

def init_app():
    db.init()
    app = FastAPI(
        title="Simple FastAPI",
        description="Simple FastAPI with SQLAlchemy",
        version="1",
    )

    @app.on_event("startup")
    async def startup():
        await db.create_all()
    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    from .router import api
    app.include_router(api, prefix="/api/v1")

    return app

app = init_app()
