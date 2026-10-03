from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# from langchain.chat_models import init_chat_model
# model=init_chat_model("orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF" ,model_provider="huggingface")

llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-120b")
msghistory = []
model = ChatHuggingFace(llm=llm)
print("type 0 to exit ______________")
while True:

    prompt = input("You : ")
    msghistory.append(prompt)
    if prompt == "0":
        break
    responce = model.invoke(msghistory)
    msghistory.append(responce.content)
    print("bot : ", responce.content)

print(msghistory)
