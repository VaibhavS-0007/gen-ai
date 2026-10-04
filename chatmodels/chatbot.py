from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# from langchain.chat_models import init_chat_model
# model=init_chat_model("orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF" ,model_provider="huggingface")

llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-120b")
print("chose the ai way you want ans's")

print("press one for angry mode")
print("press 2 for sad mode")
print("press 3 for funny mode")
choice=int(input("entr your choice"))

if choice==1:
    mode="you have to ans in angry way coz are angery mode"
elif choice==2:
    mode="you are a sad chat bot give ans in sad way"
elif choice==3:
    mode="you are funny chat bot make conversation in funny way"

msghistory = [
    SystemMessage(content=mode)
 

]
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
