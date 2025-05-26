# 🧠 AI-Based PDF Chatbot with Summarization and Contextual Q&A

An intelligent end-to-end document chatbot application that allows users to upload PDFs and interact with them using natural language. This system generates **bullet, short, and detailed summaries**, and enables **contextual question-answering** using **Retrieval-Augmented Generation (RAG)** with local embeddings.

[![GitHub Stars](https://img.shields.io/github/stars/saurabhpatle001/rag-pdf-app?style=social)](https://github.com/saurabhpatle001/rag-pdf-app/stargazers)
[![License](https://img.shields.io/github/license/saurabhpatle001/rag-pdf-app)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

## 📌 Project Overview

This project enables PDF document interaction by combining **text extraction, chunking, embeddings, vector search**, and **LLM-based summarization & Q&A**. It uses a **RAG pipeline** powered by open-source tools to ensure privacy, speed, and cost-efficiency.

> ✅ **Live Demo Screenshots**: *(Add links or embed screenshots here)*  
> ✅ **Source Code**: [GitHub Repo](https://github.com/saurabhpatle001/rag-pdf-app/tree/main)

---

## ⚙️ Tech Stack

- **Python 3.10**
- **LangChain** – Text chunking, chaining
- **HuggingFace Transformers** – For summarization & answering (BART, T5, etc.)
- **FAISS** – Local vector similarity search
- **PyMuPDF / PDFMiner** – Text extraction from PDFs
- **FastAPI or Flask** – Backend API (FastAPI recommended)
- **React.js (Optional)** – User interface

---

## 🔧 Key Features

| Feature                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| 📄 **PDF Upload**          | Upload any textbook, manual, research paper, etc.                           |
| 🧠 **Text Extraction**     | Uses PyMuPDF for extracting clean and structured text from PDF files.       |
| ✂️ **Text Chunking**       | Splits large documents into 300–500 word overlapping chunks via LangChain.  |
| 🧬 **Embeddings**          | Converts text chunks to vector embeddings using HuggingFace sentence models.|
| 🔍 **FAISS Indexing**      | Stores vectors locally for fast and accurate similarity-based retrieval.     |
| 🤖 **Summarization**       | Generates bullet-point, short, and detailed summaries using LLMs.           |
| ❓ **Q&A Chatbot**         | Answers user questions based on document context using RAG pipeline.        |

---

## 🛠️ Architecture Workflow

```mermaid
flowchart TD
    A[User uploads PDF] --> B[Text Extraction (PyMuPDF)]
    B --> C[Chunking (LangChain)]
    C --> D[Embedding with HuggingFace]
    D --> E[FAISS Vector Store]
    F[User asks question] --> G[Query FAISS for similar chunks]
    G --> H[Answer Generation with LLM (DistilBERT/BART)]
    H --> I[Return Answer to User]
