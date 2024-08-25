import streamlit as st

st.subheader('About')
with st.expander('Application'):
    st.markdown(''' Chat with your PDF documents.''')
with st.expander('Technologies Used'):
    st.markdown(''' 
    * Langflow -- Low code app builder for AI based RAG applications 
    * Supported LLMs -- All the LLMs of below companies 
        * OpenAI
        * Google
        * Groq
    * Supported Embeddings: 
        * OpenAI
        * Hugging Face
    * Supported Vector DB:
        * Astra DB
    * Streamlit -- For application Front End
    ''')
with st.expander('Contact'):
    st.markdown(''' Any Queries: Contact [Zeeshan Altaf](mailto:zeeshan.altaf@92labs.ai)''')
with st.expander('Source Code'):
    st.markdown(''' Source code: [GitHub](https://github.com/mzeeshanaltaf/langflow-pdf-chat)''')
