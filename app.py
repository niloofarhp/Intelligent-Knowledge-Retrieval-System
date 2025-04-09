import os
from config import DOCS_PATH
from document_loader import load_documents, split_documents, load_image_documents
from vector_store import create_vectorstore, load_vectorstore
from qa_chain import create_qa_chain
from interface import launch_streamlit_interface


db = load_vectorstore()
docs = load_documents(DOCS_PATH)
image_docs = load_image_documents(DOCS_PATH)
all_docs = docs + image_docs

split_docs = split_documents(docs)
db = create_vectorstore(split_docs)
qa_chain = create_qa_chain(db)
    
launch_streamlit_interface(qa_chain)
