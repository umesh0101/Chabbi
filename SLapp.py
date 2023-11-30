import os
import streamlit as st 
from streamlit_chat import message
import tempfile
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import ConversationalRetrievalChain
import uvicorn
from fastapi import FastAPI

app = FastAPI()
os.environ["TOKENIZERS_PARALLELISM"] = "false"
DB_FAISS_PATH = 'vectorstore/db_faiss'

def loadLLM():
    # Load the locally downloaded model here
    config = {'max_new_tokens': 1000, 'context_length':1000, 'repetition_penalty': 1.1}
    llm = CTransformers(
        model = "/Users/umeshkumar/Downloads/Final/model.bin",
        model_type="llama",
        config=config,
        temperature = 0.5
    )
    return llm

st.title("ChaabiGPT")

fileloader = CSVLoader(file_path='/Users/umeshkumar/Downloads/Final/bigBasketProducts.csv', encoding="utf-8", csv_args={
            'delimiter': ','})
data = fileloader.load()
#st.json(data)
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                    model_kwargs={'device': 'cpu'})

fais = FAISS.from_documents(data, embeddings)
fais .save_local(DB_FAISS_PATH)
llm = loadLLM()
conChain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=fais .as_retriever())

def conversational_chat(query):
    result = conChain({"question": query, "chat_history": st.session_state['history']})
    st.session_state['history'].append((query, result["answer"]))
    return result["answer"]

if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Ask ChaabiGPT🤗"]
if 'past' not in st.session_state:
    st.session_state['past'] = ["Hey!"]

response_container = st.container()
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_input("Query:", placeholder="Message ChaabiGPT (:", key='input')
        submit_button = st.form_submit_button(label='Send')
    if submit_button and user_input:
        output = conversational_chat(user_input)
        print(output)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
            message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")
