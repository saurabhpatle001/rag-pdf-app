# qa_chain.py

from dotenv import load_dotenv
load_dotenv()

from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import os

def get_qa_chain(vectorstore):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa_chain
