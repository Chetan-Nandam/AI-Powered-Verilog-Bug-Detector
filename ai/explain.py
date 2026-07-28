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
        print("\nAI Explanation")
        print("------------------------------")
        print("No explanation available for this error.")
        return

    print("\nAI Explanation")
    print("------------------------------")

    # Try Gemini first
    try:
        ai_response = ask_gemini(error_info, knowledge)
        print(ai_response)
        return

    except Exception as e:
        print(f"(Gemini unavailable, using local knowledge base)\n")
        print(f"Reason: {e}\n")

    # ---------- Fallback ----------
    print(knowledge["title"])
    print()

    print(knowledge["explanation"])
    print()

    print(f"The compiler reported this near line {error_info['line']}.")
    print("In Verilog, the actual mistake is sometimes on the previous line.")
    print()

    print("Original compiler message:")
    print(error_info["message"])
    print()

    print("Possible causes:")
    for cause in knowledge["causes"]:
        print(f"- {cause}")

    print()

    print("Suggested Fix:")
    print(knowledge["suggestion"])