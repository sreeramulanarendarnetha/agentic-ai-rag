from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_ollama import ChatOllama

from config import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
)


# --------------------------------------------------
# 1. Define Graph State
# --------------------------------------------------

class AgentState(TypedDict):
    question: str
    context: str
    answer: str
    score: float


# --------------------------------------------------
# 2. Initialize Embeddings, Vector Store and LLM
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = PineconeVectorStore(
    index_name=PINECONE_INDEX_NAME,
    embedding=embeddings,
    pinecone_api_key=PINECONE_API_KEY,
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# --------------------------------------------------
# 3. Retrieve Node
# --------------------------------------------------

def retrieve(state: AgentState):
    question = state["question"]

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return {
        "context": context
    }


# --------------------------------------------------
# 4. Generate Node
# --------------------------------------------------

def generate(state: AgentState):
    question = state["question"]
    context = state["context"]

    prompt = f"""
You are a helpful question-answering assistant.

Answer the user's question using ONLY the context provided below.

If the answer cannot be found in the context, say:
"I don't have enough information in the provided document."

Do not invent facts.
Do not use outside knowledge.

After answering, provide a confidence score between 0 and 1.

Context:
{context}

Question:
{question}

Return your response in this format:

Answer: <your answer>

Confidence: <number between 0 and 1>
"""

    response = llm.invoke(prompt)

    answer_text = response.content

    # Extract confidence score
    score = 0.0

    for line in answer_text.splitlines():
        if line.lower().startswith("confidence:"):
            try:
                score = float(
                    line.split(":", 1)[1].strip()
                )
            except ValueError:
                score = 0.0

    return {
        "answer": answer_text,
        "score": score
    }


# --------------------------------------------------
# 5. Build LangGraph Workflow
# --------------------------------------------------

workflow = StateGraph(AgentState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

graph = workflow.compile()