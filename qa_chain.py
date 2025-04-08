from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_core.callbacks import StdOutCallbackHandler
from langchain_openai import ChatOpenAI
from config import MODEL_NAME

def create_qa_chain(vectorstore):
    llm = ChatOpenAI(model_name=MODEL_NAME, temperature=0.7)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 25})
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory, callbacks=[StdOutCallbackHandler()])

    return conversation_chain