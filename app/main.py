from fastapi import FastAPI

from app.routes.health import router as health_router
from app.utils.config import settings
from app.utils.logger import logger


app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(health_router)

logger.info("Application started")