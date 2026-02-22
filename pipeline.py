from prompts import code_review_prompt
from model import llm
from validator import validate_input

code_review_pipeline = code_review_prompt | llm

def review_code(code, context):
    validate_input(code, context)

    response = code_review_pipeline.invoke({
        "code": code,
        "context": context
    })

    return response.content