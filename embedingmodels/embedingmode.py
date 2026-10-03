from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings=OpenAIEmbeddings(

    model='text-embedding-3-small',
    dimensions=64
)
text=[
"hello myour name is yt",
"you gys all are awsome",
"helloe there"

]

vector=embeddings.embed_query("we are going to learn gen ai")
vector=embeddings.embed_documents(text)

print(vector)
