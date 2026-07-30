from ai.knowledge import get_error_knowledge
from ai.llm import ask_gemini


def explain_error(error_info):
    """
    Generate an explanation for a parsed compiler error.
    Uses Gemini AI when possible and falls back to the
    built-in rule-based explanation if AI is unavailable.
    """

    knowledge = get_error_knowledge(error_info["type"])

    if knowledge is None:
        return "No explanation available for this error."

    # Try Gemini first
    try:
        return ask_gemini(error_info, knowledge)

    except Exception as e:
        return f"""
Gemini Error

{e}

-------------------------

Fallback Explanation

{knowledge["title"]}

{knowledge["explanation"]}

The compiler reported this near line {error_info["line"]}.

Original compiler message:

{error_info["message"]}

Suggested Fix:

{knowledge["suggestion"]}
"""