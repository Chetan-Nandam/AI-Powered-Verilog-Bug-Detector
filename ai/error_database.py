ERROR_DATABASE = {

    "syntax error": {
        "title": "Syntax Error",

        "explanation": (
            "The Verilog code does not follow the correct language syntax."
        ),

        "causes": [
            "Missing semicolon (;)",
            "Missing endmodule",
            "Typing mistake in a keyword",
            "Missing begin/end block"
        ],

        "suggestion": (
            "Inspect the reported line and the line immediately before it. "
            "Syntax errors are frequently caused by a missing semicolon, "
            "an unmatched begin/end block, or a missing endmodule."
        )
    },

    "Unknown module type": {
        "title": "Unknown Module",

        "explanation": (
            "The compiler cannot find the module being instantiated."
        ),

        "causes": [
            "Module name is misspelled",
            "Required Verilog file was not compiled",
            "Module definition is missing"
        ],

        "suggestion": (
            "Verify that the module exists, the spelling is correct, "
            "and that all required Verilog source files are compiled together."
        )
    }

}