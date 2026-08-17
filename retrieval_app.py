import streamlit as st
from retrieval_model import retrieval


# Page configuration
st.set_page_config(
    page_title="Agricultural Document Retrieval",
    page_icon="🌱",
    layout="wide"
)


# App title
st.title("🌱 Agricultural Document Retrieval")

st.write(
    "Ask a question about agriculture and retrieve the most relevant "
    "agricultural extension documents."
)


# Search box
query = st.text_input(
    "Enter your question:",
    placeholder="e.g. How do I cope with drought and erratic rainfall on my farm?"
)


# Retrieve documents
if query:
    results = retrieval(query, topk=5)

    st.subheader("Top 5 Relevant Documents")

    for _, row in results.iterrows():

        st.markdown(f"### {row['title']}")

        st.write(row["text"])

        st.caption(f"Source: {row['source']}")

        st.divider()


# Disclaimer
st.caption(
    "Disclaimer: This tool provides agricultural information for informational purposes only and should not replace professional agricultural advice."
)