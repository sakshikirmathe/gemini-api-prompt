class PromptEngine:
    def build(self, user_input: str) -> str:
        return f"""
You are a professional data and AI assistant.

Analyze the following input and respond clearly and concisely.

User Input:
{user_input}

Output:
"""
