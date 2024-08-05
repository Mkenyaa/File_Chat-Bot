import os
import tempfile
import streamlit as st
from langchain.document_loaders import JSONLoader, CSVLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Function to save the uploaded file to a temporary location
def save_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        return tmp_file.name

# Function to load and process the document
def load_document(file_path):
    if file_path.endswith(".json"):
        loader = JSONLoader(file_path=file_path)
    elif file_path.endswith(".csv"):
        loader = CSVLoader(file_path=file_path)
    elif file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path=file_path)
    else:
        st.error("Unsupported file type")
        return None

    data = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(data)
    return documents

# Function to create the vector store
def create_vector_store(documents):
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(documents, embeddings)
    return vector_store

# Function to create the QA chain
def create_qa_chain(vector_store):
    llm = ChatOpenAI(model_name="gpt-4")
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vector_store.as_retriever())
    return qa_chain

# Streamlit app
def main():
    st.title("Chat with your documents")

    # Get OpenAI API key from the user
    api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")
    os.environ["OPENAI_API_KEY"] = api_key

    uploaded_file = st.file_uploader("Upload a file", type=["json", "csv", "pdf"])

    if uploaded_file is not None:
        file_path = save_uploaded_file(uploaded_file)
        documents = load_document(file_path)
        if documents is not None:
            vector_store = create_vector_store(documents)
            qa_chain = create_qa_chain(vector_store)

            query = st.text_input("Ask a question about the document")
            if query:
                response = qa_chain({"query": query})
                st.write(response["result"])

if __name__ == "__main__":
    main()
