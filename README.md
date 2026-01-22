# AI-Legal-Assistant-Indian-Penal-Code-IPC-
An AI-powered Legal Assistant built using LangChain and a Retrieval-Augmented Generation (RAG) pipeline to answer queries related to the Indian Penal Code (IPC) with accurate, legally grounded explanations.
# Features
Ask natural language questions about IPC sections

Retrieves relevant law sections using semantic search

Generates simple, human-readable explanations using Gemini LLM

Reduces hallucinations by grounding responses in official legal documents

Displays source sections for transparency

# Architecture
**RAG Pipeline Flow:**
- IPC PDF / Legal Text  
- Text Chunking  
- Embeddings  
- FAISS Vector Database  
- Retriever (Top-k sections)  
- Gemini LLM  
- Final Answer + Sources  

