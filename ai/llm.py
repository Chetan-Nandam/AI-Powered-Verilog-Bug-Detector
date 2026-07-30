import os

from dotenv import load_dotenv
from google import genai

from ai.prompts import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_section(text, start_marker, end_marker=None):
    try:
        start = text.index(start_marker) + len(start_marker)

        if end_marker:
            end = text.index(end_marker, start)
            return text[start:end].strip()

        return text[start:].strip()

    except ValueError:
        return ""


def clean_code_block(code):
    """
    Removes Markdown code fences from Gemini output.
    """

    code = code.strip()

    if code.startswith("```verilog"):
        code = code[len("```verilog"):]

    elif code.startswith("```"):
        code = code[len("```"):]

    if code.endswith("```"):
        code = code[:-3]

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
"""

    response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents=prompt
    )

    ai_text = response.text

    return {
        "summary": extract_section(
            ai_text,
            "===SUMMARY===",
            "===CAUSE==="
        ),
        "cause": extract_section(
            ai_text,
            "===CAUSE===",
            "===FIX==="
        ),
        "fix": extract_section(
            ai_text,
            "===FIX===",
            "===CODE==="
        ),
        "code": clean_code_block(
            extract_section(
                ai_text,
                "===CODE==="
            )
        )
    }