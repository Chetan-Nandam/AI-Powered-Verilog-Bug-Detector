import subprocess
import sys
import time

from ai.explain import explain_error
from compiler.parser import parse_error


def compile_verilog(verilog_file):

    result = subprocess.run(
        ["iverilog", verilog_file],
        capture_output=True,
        text=True
    )

    # Read original source code
    try:
        with open(verilog_file, "r") as file:
            source_code = file.read()

    except Exception:
        source_code = "Unable to read source code."

    # Split source code into individual lines
    source_lines = source_code.splitlines()

    response = {
        "file": verilog_file,
        "source_code": source_code,
        "source_lines": source_lines
    }

    # --------------------------------------------------
    # Compilation Successful
    # --------------------------------------------------

    if result.returncode == 0:

        response["status"] = "SUCCESS"
        response["compiler_output"] = "Compilation completed successfully."

        response["error_type"] = None
        response["line"] = None

        response["errors"] = []
        response["error_lines"] = []

        response["ai_response"] = None

    # --------------------------------------------------
    # Compilation Failed
    # --------------------------------------------------

    else:

        compiler_error = result.stderr

        # Parse compiler errors
        error_info = parse_error(compiler_error)

        # -----------------------------
        # Measure AI response time
        # -----------------------------

        start = time.time()

        ai_response = explain_error(error_info)

        end = time.time()

        print("\n========== PERFORMANCE ==========")
        print(f"AI Response Time : {end - start:.2f} seconds")
        print("=================================\n")

        response["status"] = "FAILED"

        response["compiler_output"] = compiler_error

        response["error_type"] = error_info["type"]
        response["line"] = error_info["line"]

        response["errors"] = error_info["errors"]

        response["error_lines"] = [
            error["line"]
            for error in error_info["errors"]
        ]

        response["ai_response"] = ai_response

    return response


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python compiler/compile.py <verilog_file>")
        sys.exit(1)

    print(compile_verilog(sys.argv[1]))