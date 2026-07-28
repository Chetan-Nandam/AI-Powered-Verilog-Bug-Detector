import os

from dotenv import load_dotenv
from google import genai

from ai.prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(error_info, knowledge):

    prompt = f"""
{SYSTEM_PROMPT}

Compiler Error:
{error_info["message"]}

Line Number:
{error_info["line"]}

Known Explanation:
{knowledge["explanation"]}

Known Possible Causes:
{", ".join(knowledge["causes"])}

Known Suggestion:
{knowledge["suggestion"]}

Generate a helpful explanation.
"""

    response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents=prompt
    )

    return response.text