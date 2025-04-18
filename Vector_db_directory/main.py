import os
import json

import streamlit as st 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
GROQ_API_KEY = config_data["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

def setup_vectorstore():
    persist_directory = f"{working_dir}/vector_db_directory"
    embeddings = HuggingFaceEmbeddings()
    vectorstore = Chroma(persist_directory=persist_directory,
                         embedding_function=embeddings)
    return vectorstore

def chat_chain(vectorstore):
    llm = ChatGroq(model="llama-3.3-70b-versatile",
                   temperature=0)
    retriever = vectorstore.as_retriever()
    memory = ConversationBufferMemory(
        llm=llm,
        output_key="answer",
        memory_key="chat_history",
        return_messages=True
    )
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        memory=memory,
        verbose=True,
        return_source_documents=True
    )
    return chain

st.set_page_config(
    page_title= "ChatBot",
    page_icon= "📒",
    layout= "centered"
)

st.title("📒Multi Documents ChatBot📒")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
#vectorstore = setup_vectorstore()
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = setup_vectorstore()

#chain = chat_chain()    
if "conversationsal_chain" not in st.session_state:
    st.session_state.conversationsal_chain = chat_chain(st.session_state.vectorstore)

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
user_input = st.chat_input("ASK AI...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content" : user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
        
    
    with st.chat_message("assistant"):
        response = st.session_state.conversationsal_chain({"question": user_input})
        assistant_response = response["answer"]
        st.markdown(assistant_response)
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})








# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# .venv\Scripts\Activate.ps1

# cd vector_db_directory

# streamlit run main.py

# WHAT IS PATHOPHYSIOLOGY?

