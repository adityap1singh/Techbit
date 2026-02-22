from langchain_core.prompts import ChatPromptTemplate

code_review_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior Python code reviewer."),
    ("human", """
Context:
{context}

Analyze the Python code for:
- Security
- Performance
- Code Style (PEP8)
- Logic Errors

Return STRICT JSON with:
summary, issues_identified, recommendations, improved_code_examples

Code:
{code}
""")
])