import os
import PyPDF2
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document

load_dotenv()


def initialize_llm():
    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )


def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)

    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text

    return full_text


def get_summary(text, mode="short"):
    llm = initialize_llm()

    if mode == "bullet":
        prompt = PromptTemplate.from_template(
            "Summarize the text in bullet points:\n\n{text}"
        )

    elif mode == "detailed":
        prompt = PromptTemplate.from_template(
            "Provide a detailed summary:\n\n{text}"
        )

    else:
        prompt = PromptTemplate.from_template(
            "Give a concise summary:\n\n{text}"
        )

    docs = [Document(page_content=text[:3000])]

    chain = load_summarize_chain(
        llm,
        chain_type="stuff",
        prompt=prompt
    )

    summary = chain.run(docs)

    return summary