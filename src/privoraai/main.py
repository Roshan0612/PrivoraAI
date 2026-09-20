from fastapi import FastAPI

from privoraai.api.health import router as health_router
from privoraai.api.me import router as me_router

from privoraai.api.connections import router as connections_router
def create_app() -> FastAPI:
    app = FastAPI(
        title="PrivoraAI",
        version="0.1.0",
    )
    
    app.include_router(health_router)
    app.include_router(me_router)
    app.include_router(connections_router)

    return app


app = create_app()