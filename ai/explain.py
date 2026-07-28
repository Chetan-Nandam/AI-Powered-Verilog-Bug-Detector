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

    except Exception:
        pass

    # ---------- Fallback ----------
    response = []

    response.append(knowledge["title"])
    response.append("")
    response.append(knowledge["explanation"])
    response.append("")
    response.append(
        f"The compiler reported this near line {error_info['line']}."
    )
    response.append(
        "In Verilog, the actual mistake is sometimes on the previous line."
    )
    response.append("")
    response.append("Original compiler message:")
    response.append(error_info["message"])
    response.append("")
    response.append("Possible causes:")

    for cause in knowledge["causes"]:
        response.append(f"- {cause}")

    response.append("")
    response.append("Suggested Fix:")
    response.append(knowledge["suggestion"])

    return "\n".join(response)