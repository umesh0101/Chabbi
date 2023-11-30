# Chabbi

ChaabiGPT is a conversational AI chatbot designed to provide intuitive and interactive responses to user queries. It leverages the power of LLaMA (Large Language Model in Action) and vector similarity search for effective and context-aware conversation.

Installation
Before running ChaabiGPT, ensure that you have the required dependencies installed. This includes Streamlit for the web interface, HuggingFace for embeddings, and FAISS for vector storage and retrieval.
Clone the repository to your local machine.
Install the required Python packages:

pip install streamlit huggingface_hub faiss-langchain fastapi uvicorn

To start the ChaabiGPT server, navigate to the directory containing the app and run:

streamlit run app.py

The web interface will be available at http://localhost:8501. Enter your query in the input box and receive responses from ChaabiGPT.
