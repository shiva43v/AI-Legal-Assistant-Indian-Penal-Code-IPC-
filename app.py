import streamlit as st
from rag_chain import load_rag_chain

st.set_page_config(page_title="AI Legal Assistant (IPC)")
st.title("AI Legal Assistant – Indian Penal Code")

qa_chain = load_rag_chain()

query = st.text_input(
    "Ask a legal question (e.g., What is punishment for IPC 420?)"
)

if query:
    with st.spinner("Analyzing IPC sections..."):
        result = qa_chain(query)

    st.subheader("Legal Explanation")
    st.write(result["result"])

    with st.expander("Source Sections"):
        for doc in result["source_documents"]:
            st.write(doc.page_content[:500] + "...")
