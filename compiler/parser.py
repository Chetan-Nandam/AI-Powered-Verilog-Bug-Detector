def parse_error(compiler_error):

    error_parts = compiler_error.split(":")

    error_file = error_parts[0]
    error_line = int(error_parts[1])
    error_type = ":".join(error_parts[2:]).split("\n")[0].strip()

    error_message = compiler_error.strip()

    error_info = {
        "file": error_file,
        "line": error_line,
        "type": error_type,
        "message": error_message
    }

    return error_info