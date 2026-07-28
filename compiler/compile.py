import subprocess
import sys

from ai.explain import explain_error
from compiler.parser import parse_error


def compile_verilog(verilog_file):

    result = subprocess.run(
        ["iverilog", verilog_file],
        capture_output=True,
        text=True
    )

    output = []

    output.append("=" * 40)
    output.append("AI VERILOG BUG DETECTOR")
    output.append("=" * 40)
    output.append(f"File   : {verilog_file}")

    if result.returncode == 0:

        output.append("Status : SUCCESS")
        output.append("")
        output.append("Compilation completed successfully.")

    else:

        output.append("Status : FAILED")
        output.append("")

        compiler_error = result.stderr

        output.append("Compiler Output:")
        output.append(compiler_error)

        error_info = parse_error(compiler_error)

        output.append("")
        output.append("Parsed Error Information")
        output.append("-" * 30)
        output.append(f"File : {error_info['file']}")
        output.append(f"Line : {error_info['line']}")
        output.append(f"Type : {error_info['type']}")
        output.append("")

        ai_response = explain_error(error_info)

        output.append("AI Explanation")
        output.append("-" * 30)
        output.append(str(ai_response))

    return "\n".join(output)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: py compiler/compile.py <verilog_file>")
        sys.exit(1)

    print(compile_verilog(sys.argv[1]))