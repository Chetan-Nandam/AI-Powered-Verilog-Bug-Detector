import subprocess
import sys

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
    print("Compilation Successful!")
else:
    print("Compilation Failed!")
    print(result.stderr)