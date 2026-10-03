from dotenv import load_dotenv

load_dotenv()
'''
from langchain.chat_models import init_chat_model
# from langchain_groq import ChatGroq
model=init_chat_model("openai/gpt-oss-20b",model_provider="groq",temperature = 0) #,max_tokens=500 -by this u can set token usage
responce=model.invoke("what is earth in short")

print(responce.content)
print(responce.usage_metadata)
'''

from langchain.chat_models import init_chat_model

model=init_chat_model("orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF",model_provider="huggingface")
responce=model.invoke("hi")

print(responce.content)

'''
from dotenv import load_dotenv

load_dotenv()
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4.1")



response = model. invoke("what is cricket?")
print(response.content)
'''
'''
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.2"
)
print(model)

# response = model.invoke("What is cricket?")

# print(response.content)


import .env 
 from chat model import init caht model
 init caht model(modelname)
 model.invoke("qus)
 store on responce then responce .content

'''
