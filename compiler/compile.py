import subprocess
import sys

def parse_error(compiler_error):
    pass

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
if result.returncode == 0:
    print("=" * 40)
    print("AI VERILOG BUG DETECTOR")
    print("=" * 40)
    print(f"File   : {verilog_file}")
    print("Status : SUCCESS")
else:
    print("=" * 40)
    print("AI VERILOG BUG DETECTOR")
    print("=" * 40)
    print(f"File   : {verilog_file}")
    print("Status : FAILED")
    print()
    compiler_error = result.stderr
    print("Compiler Output:")
    print(compiler_error)
    error_parts = compiler_error.split(":")
    error_file = error_parts[0]
    error_line = int(error_parts[1])
    error_type = error_parts[2].split("\n")[0].strip()
    #print(f"Error File : {error_parts[0]}")
    #print(f"Error Line : {error_parts[1]}")
    #error_type = error_parts[2].split("\n")[0]
    #print(f"Error Type : {error_type}")
    error_info = {
        "file": error_file,
        "line": error_line,
        "type": error_type
    }
    print("\nParsed Error Information")
    print("-" * 30)
    print(f"File : {error_info['file']}")
    print(f"Line : {error_info['line']}")
    print(f"Type : {error_info['type']}")