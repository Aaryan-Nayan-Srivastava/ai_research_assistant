from app.schemas.research_response import ResearchResponse

from app.services.prompt_builder import build_research_prompt

from app.services.groq_service import llm


def generate_research(topic: str,level: str) -> ResearchResponse:

    prompt = build_research_prompt(topic=topic,level=level)

    structured_llm = llm.with_structured_output( ResearchResponse)

    response = structured_llm.invoke(prompt)

    return response