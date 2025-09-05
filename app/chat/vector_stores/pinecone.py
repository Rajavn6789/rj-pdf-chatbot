from pinecone import Pinecone
import os
from langchain.vectorstores import Pinecone as LangchainPinecone
from app.chat.embeddings.openai import embeddings  # your OpenAI embeddings

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = os.getenv("PINECONE_INDEX_NAME")


if index_name not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=1536,             
        metric="cosine",
        spec={"serverless": {"cloud": "aws", "region": "us-east-1"}}
    )

vector_store = LangchainPinecone.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

def build_retriever(chat_args):
    search_kwargs = {"filter": {"pdf_id": chat_args.pdf_id}}
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )
