# Multi-Document RAG Chatbot

## Overview
This project implements a Multi-Document Retrieval-Augmented Generation (RAG) chatbot that enables efficient information extraction and querying across multiple documents. Built using **LangChain**, **Groq**, **ChromaDB**, and **LLAMA 3.3**, the solution is deployed with **Streamlit** for a seamless user interface.

## Features
- **Multi-Document Support**: Retrieve and generate responses from multiple documents.
- **Efficient Information Extraction**: Leverages advanced retrieval techniques for quick document searching.
- **Generative Responses**: Uses LLAMA 3.3 to generate human-like, context-aware responses.
- **Streamlit Deployment**: User-friendly interface for interacting with the chatbot.

## Technologies Used
- **LangChain**: For building the retrieval pipeline.
- **Groq**: Hardware-accelerated processing for efficient computation.
- **ChromaDB**: Database for storing and retrieving documents.
- **LLAMA 3.3**: Language model for generating accurate responses.
- **Streamlit**: Used for deployment and creating the UI.

## Installation

### Requirements:
- Python 3.13
- Streamlit
- LangChain
- Groq
- ChromaDB

### Setup:
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/multi-document-rag-chatbot.git
   cd multi-document-rag-chatbot
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

## Usage
- The app will load in your default web browser.
- Upload multiple documents for the chatbot to process.
- Type in a query, and the chatbot will retrieve relevant documents and generate contextually accurate responses.
