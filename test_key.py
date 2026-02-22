from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate(
    input_variables=["code"],
    template="Review this Python code:\n{code}"
)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run(code="print('Hello world')"))