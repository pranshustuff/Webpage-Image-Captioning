import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str, max_tokens=150) -> str:
    """
    Summarize a section of text using OpenAI GPT.
    """
    try:
        prompt = f"Summarize the following section concisely:\n\n{text}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.3
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"[Error summarizing section: {e}]"
