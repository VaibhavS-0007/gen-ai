from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

model=HuggingFaceEndpoint(
    model="openai/gpt-oss-120b"
)
m=ChatHuggingFace(llm=model)

result=m.invoke("hi")
print(result.content)
