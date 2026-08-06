import os
import re

from dotenv import load_dotenv
from google import genai

from ai.prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def clean_code_block(code):
    """
    Removes Markdown code fences from Gemini output.
    """

    if not code:
        return ""

    code = code.strip()
    code = code.replace("```verilog", "")
    code = code.replace("```", "")

    return code.strip()


def ask_gemini(error_info, knowledge):

    try:
        with open(error_info["file"], "r") as file:
            source_code = file.read()

    except Exception:
        source_code = "Source code could not be read."

    prompt = f"""
{SYSTEM_PROMPT}

Verilog Source Code:

{source_code}

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

IMPORTANT:
Return ONLY the required format.
Do NOT skip any section.
Always include corrected Verilog code.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        ai_text = response.text

    except Exception:
        raise

    def section(name):

        pattern = rf"===\s*{name}\s*===\s*(.*?)(?=\n===|\Z)"

        match = re.search(pattern, ai_text, re.DOTALL)

        if match:
            return match.group(1).strip()

        return ""

    return {

        "summary": section("SUMMARY"),

        "cause": section("CAUSE"),

        "fix": section("FIX"),

        "code": clean_code_block(
            section("CODE")
        )

    }