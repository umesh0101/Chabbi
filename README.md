# Chabbi

ChaabiGPT is a conversational AI chatbot designed to provide intuitive and interactive responses to user queries. It leverages the power of LLaMA (Large Language Model in Action) and vector similarity search for effective and context-aware conversation.

First Download model from the given link 

https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin

Installation
Before running ChaabiGPT, ensure that you have the required dependencies installed. This includes Streamlit for the web interface, HuggingFace for embeddings, and FAISS for vector storage and retrieval.
Clone the repository to your local machine.
Install the required Python packages:

pip install -r requirements.txt

pip install streamlit huggingface_hub faiss-langchain fastapi uvicorn

To start the ChaabiGPT server, navigate to the directory containing the app and run:

pip install streamlit

streamlit run SLapp.py

The web interface will be available at http://localhost:8501. Enter your query in the input box and receive responses from ChaabiGPT.


OUTPUT of ChabbiGPT
<img width="1431" alt="Screenshot 2023-11-30 at 11 19 27 PM" src="https://github.com/umesh0101/Chabbi/assets/95159950/01e16606-13bc-435b-8759-e861f9d6b671">
<img width="1440" alt="Screenshot 2023-11-30 at 11 37 53 PM" src="https://github.com/umesh0101/Chabbi/assets/95159950/aec147e9-43df-4fde-adc1-8250257ec376">

Loading app may take time as I run it using cpu and for faster loading use gpu 
