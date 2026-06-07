from pydantic import BaseModel, Field


class ResearchResponse(BaseModel):
    summary: str = Field(
        description="A concise summary of the topic."
    )

    key_concepts: list[str] = Field(
        description="List of important concepts."
    )

    important_questions: list[str] = Field(
        description="List of questions a learner should explore."
    )

    learning_roadmap: list[str] = Field(
        description="Ordered learning steps."
    )