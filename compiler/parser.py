import re


def parse_error(compiler_error):
    """
    Parses all Icarus Verilog compiler errors.

    Returns:
        {
            "file": "...",
            "line": 7,
            "type": "...",
            "message": "...",
            "errors": [
                {
                    "file": "...",
                    "line": 7,
                    "type": "...",
                    "message": "..."
                },
                ...
            ]
        }
    """

    errors = []

    lines = compiler_error.splitlines()

    pattern = r"^(.*?):(\d+):\s*(.*)$"

    for line in lines:

        match = re.match(pattern, line)

        if match:

            file_name = match.group(1).strip()
            line_number = int(match.group(2))
            message = match.group(3).strip()

            errors.append({
                "file": file_name,
                "line": line_number,
                "type": message,
                "message": message
            })

    if len(errors) == 0:

        return {
            "file": None,
            "line": None,
            "type": "Unknown Error",
            "message": compiler_error.strip(),
            "errors": []
        }

    return {
        "file": errors[0]["file"],
        "line": errors[0]["line"],
        "type": errors[0]["type"],
        "message": compiler_error.strip(),
        "errors": errors
    }