import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(openai_api_base="http://localhost:11434/v1", openai_api_key="ignored", model=os.environ['MODEL'])

print(llm.invoke("Who are you?"))
