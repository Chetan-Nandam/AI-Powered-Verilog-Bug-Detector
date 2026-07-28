import subprocess
import sys

from ai.explain import explain_error
from compiler.parser import parse_error


if len(sys.argv) != 2:
    print("Usage: py compiler/compile.py <verilog_file>")
    sys.exit(1)

verilog_file = sys.argv[1]

print(f"Checking file: {verilog_file}")

result = subprocess.run(
    ["iverilog", verilog_file],
    capture_output=True,
    text=True
)

# Common Header
print("=" * 40)
print("AI VERILOG BUG DETECTOR")
print("=" * 40)
print(f"File   : {verilog_file}")

if result.returncode == 0:

    print("Status : SUCCESS")

    print("\nAI Explanation")
    print("------------------------------")
    print(explain_error(None))

else:

    print("Status : FAILED")
    print()

    compiler_error = result.stderr

    print("Compiler Output:")
    print(compiler_error)

    # Parse the compiler error
    error_info = parse_error(compiler_error)

    print("\nParsed Error Information")
    print("-" * 30)
    print(f"File : {error_info['file']}")
    print(f"Line : {error_info['line']}")
    print(f"Type : {error_info['type']}")

    ai_response = explain_error(error_info)

    print()
    print("AI Explanation")
    print("-" * 30)
    print(ai_response)