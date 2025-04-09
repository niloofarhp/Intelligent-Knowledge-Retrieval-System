from langchain.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from config import DB_NAME
import os
def create_vectorstore(docs, persist_directory=DB_NAME):
    embeddings = OpenAIEmbeddings()
    vector_store =  Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=persist_directory)
    vector_store.persist()
    return vector_store

def load_vectorstore(persist_directory=DB_NAME):
    embeddings = OpenAIEmbeddings()
    if os.path.exists(DB_NAME):
        Chroma(persist_directory=DB_NAME, embedding_function=embeddings).delete_collection()    
    return Chroma(persist_directory=persist_directory, embedding_function=embeddings)
