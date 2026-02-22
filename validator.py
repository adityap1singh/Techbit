import ast

def validate_input(code, context):
    if not code.strip():
        raise ValueError("Empty code snippet")

    if len(code) > 5000:
        raise ValueError("Code too long")

    if not context.strip():
        raise ValueError("Context required")

    ast.parse(code)  # raises SyntaxError automatically