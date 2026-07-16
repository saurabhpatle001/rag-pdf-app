from dotenv import load_dotenv
import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


def create_vector_store_from_text(text):
    # Split text into chunks
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.create_documents([text])

    # Google Gemini Embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # Create FAISS vector store
    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore