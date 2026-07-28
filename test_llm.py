from ai.llm import ask_gemini

response = ask_gemini(
    "Explain in two sentences what a Verilog syntax error is."
)

print(response)