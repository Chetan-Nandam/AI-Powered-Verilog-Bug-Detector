import os
import re

from dotenv import load_dotenv
from google import genai

from ai.prompts import SYSTEM_PROMPT

print("LLM FILE:", __file__)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def clean_code_block(code):
    """
    Remove markdown code fences.
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

    print("MODEL USED: gemini-3.5-flash")

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    ai_text = response.text

    print("\n========== RAW GEMINI RESPONSE ==========\n")
    print(ai_text)
    print("\n=========================================\n")

    def section(name):

        pattern = rf"===\s*{name}\s*===\s*(.*?)(?=\n===|\Z)"

        match = re.search(pattern, ai_text, re.DOTALL)

        if match:
            return match.group(1).strip()

        return ""

    summary = section("SUMMARY")
    cause = section("CAUSE")
    fix = section("FIX")
    code = clean_code_block(section("CODE"))

    print("\n========== PARSED DATA ==========")
    print("SUMMARY:")
    print(summary)

    print("\nCAUSE:")
    print(cause)

    print("\nFIX:")
    print(fix)

    print("\nCODE LENGTH:", len(code))
    print("\nFIRST 200 CHARACTERS:")
    print(repr(code[:200]))
    print("=================================\n")

    return {
        "summary": summary,
        "cause": cause,
        "fix": fix,
        "code": code
    }