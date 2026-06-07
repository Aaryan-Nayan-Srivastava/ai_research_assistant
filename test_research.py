from app.services.research_service import (
    generate_research
)

result = generate_research(
    topic="Transformers",
    level="Beginner"
)

print(result)