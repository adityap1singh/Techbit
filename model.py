from dotenv import load_dotenv
load_dotenv()  # 👈 THIS LINE IS REQUIRED

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)