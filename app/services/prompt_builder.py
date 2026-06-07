def build_research_prompt(topic: str,level: str) -> str:

    return f"""
You are an expert research assistant.

Topic: {topic}
Level: {level}

Generate:

1. Summary
2. Key Concepts
3. Important Questions
4. Learning Roadmap

IMPORTANT:
- key_concepts must be a list of strings
- important_questions must be a list of strings
- learning_roadmap must be a list of strings
"""