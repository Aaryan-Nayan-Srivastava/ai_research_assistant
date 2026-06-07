from fastapi import APIRouter, HTTPException

from app.schemas.research_request import ResearchRequest
from app.schemas.research_response import ResearchResponse

from app.services.research_service import generate_research

router = APIRouter(prefix="/research")


@router.post("/generate",response_model=ResearchResponse)
def generate_research_brief(
    request: ResearchRequest
):
    try:
        return generate_research(topic=request.topic,level=request.level)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )