from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.research import router as research_router

from app.utils.config import settings
from app.utils.logger import logger


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(research_router)

logger.info("Application started")