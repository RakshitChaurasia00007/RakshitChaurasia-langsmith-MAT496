# utils.py
# Basic implementation for get_vector_db_retriever
# You can modify this later depending on your LangSmith or OpenAI RAG setup.

from typing import List, Dict

class DummyRetriever:
    """
    A mock retriever class that simulates vector database retrieval.
    In a real RAG setup, this would connect to a vector DB like Pinecone, FAISS, or Chroma.
    """
    def __init__(self, documents: List[str]):
        self.documents = documents

    def retrieve(self, query: str) -> List[Dict[str, str]]:
        # For now, return all docs containing any query word
        results = [doc for doc in self.documents if any(word.lower() in doc.lower() for word in query.split())]
        return [{"content": r} for r in results]


def get_vector_db_retriever() -> DummyRetriever:
    """
    Returns a DummyRetriever instance.
    In real projects, replace this with code that initializes and returns your actual retriever.
    """
    sample_docs = [
        "LangSmith helps trace and debug LLM applications.",
        "OpenAI models like GPT-4o-mini can perform reasoning and text generation.",
        "Vector databases are used in RAG (Retrieval-Augmented Generation) pipelines.",
        "The @traceable decorator is used for LangSmith tracing.",
    ]
    return DummyRetriever(sample_docs)
