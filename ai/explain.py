from ai.knowledge import get_error_knowledge
from ai.llm import ask_gemini


def explain_error(error_info):
    """
    Generate an explanation for a parsed compiler error.
    Uses Gemini AI when available.
    Falls back to built-in knowledge if Gemini is unavailable.
    """

    knowledge = get_error_knowledge(error_info["type"])

    if knowledge is None:

        return {
            "summary": "No explanation available.",
            "cause": "Unknown compiler error.",
            "fix": "Please inspect the compiler output.",
            "code": ""
        }

    # -------------------------
    # Try Gemini
    # -------------------------

    try:

        return ask_gemini(error_info, knowledge)

    # -------------------------
    # Fallback
    # -------------------------

    except Exception as e:

        print("\n========== GEMINI EXCEPTION ==========")
        print(e)

        return {

            "summary":
                knowledge["title"],

            "cause":
                knowledge["explanation"],

            "fix":
                knowledge["suggestion"],

            "code": ""

        }