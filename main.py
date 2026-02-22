from pipeline import review_code

code = """
password = "admin123"
if input() == password:
    print("Access granted")
"""

context = "Authentication logic"

print(review_code(code, context))