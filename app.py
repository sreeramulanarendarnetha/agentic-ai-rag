import sys
import streamlit as st

sys.path.insert(0, "src")

from graph import graph


st.set_page_config(
    page_title="Agentic AI RAG",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Agentic AI RAG Assistant")
st.write("Ask questions about the Agentic AI ebook.")

question = st.text_input(
    "Enter your question:",
    placeholder="What is agentic AI?"
)

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching the document and generating an answer..."):
            result = graph.invoke({
                "question": question,
                "context": "",
                "answer": "",
                "score": 0.0
            })

        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("Confidence Score")
        st.write(result["score"])