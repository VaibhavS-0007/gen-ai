from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# from langchain.chat_models import init_chat_model
# model=init_chat_model("orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF" ,model_provider="huggingface")

llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-120b")
msghistory = []
model = ChatHuggingFace(llm=llm)

responce = model.invoke("hi")



print(responce.content)




