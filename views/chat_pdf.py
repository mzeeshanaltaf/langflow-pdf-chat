import os

from util import *
import pandas as pd

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
if "response" not in st.session_state:
    st.session_state.response = None
if "collection_name" not in st.session_state:
    st.session_state.collection_name = None
if "app_activation" not in st.session_state:
    st.session_state.app_activation = False
if "ai_company" not in st.session_state:
    st.session_state.ai_company = None
if "llm_model" not in st.session_state:
    st.session_state.llm_model = None
if "embedding_model" not in st.session_state:
    st.session_state.embedding_model = None
if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ''
if "google_api_key" not in st.session_state:
    st.session_state.google_api_key = ''
if "groq_api_key" not in st.session_state:
    st.session_state.groq_api_key = ''
if "hf_embedding_api_key" not in st.session_state:
    st.session_state.hf_embedding_api_key = ''
if "openai_embedding_api_key" not in st.session_state:
    st.session_state.openai_embedding_api_key = ''

# Set the environment variables for Token, API URK,  EP and API keys
os.environ['ASTRA_DB_APPLICATION_TOKEN'] = st.secrets['ASTRA_DB_APPLICATION_TOKEN']
os.environ['ASTRA_DB_API_ENDPOINT'] = st.secrets['ASTRA_DB_API_ENDPOINT']
os.environ['HF_API_URL'] = st.secrets['HF_API_URL']
os.environ['OPENAI_API_KEY'] = st.session_state.openai_api_key
os.environ['GROQ_API_KEY'] = st.session_state.groq_api_key
os.environ['GOOGLE_API_KEY'] = st.session_state.google_api_key
os.environ['HUGGING_FACE_API_KEY'] = st.session_state.hf_embedding_api_key
os.environ['OPENAI_EMBEDDING_API_KEY'] = st.session_state.openai_embedding_api_key

# INITIALIZE STREAMLIT APP
page_title = "Chat with PDF"
page_icon = "📄"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# TITLE PAGE
st.title("Chat with PDF💬📄")
st.write(":blue[***Powered by Langflow***]")

df = pd.DataFrame({
    'LLM Company': [st.session_state.ai_company],
    'LLM': [st.session_state.llm_model],
    'Embedding Model': [st.session_state.embedding_model]
})
st.subheader('Selected Configuration:')
if st.session_state.app_activation is False:
    st.info('Set the configuration from Configuration page before proceeding...', icon="ℹ️")
else:
    st.dataframe(df, hide_index=True, use_container_width=True)

#  UPLOAD SECTION
st.subheader('Upload PDF⬆️:')
uploaded_file = st.file_uploader("Upload your PDFs", type=['pdf'], label_visibility='collapsed',
                                 disabled=not st.session_state.app_activation)
upload = st.button("Create Vector DB", type="primary", key="process", disabled=not uploaded_file)

if upload:
    # Create Vector Database
    st.session_state.collection_name = create_vector_db(uploaded_file, st.session_state.embedding_model)

st.subheader('Chatbot🤖:')
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if question := st.chat_input(placeholder='Enter your question related to uploaded document',
                             disabled=not st.session_state.collection_name):
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)
    with st.spinner('Processing...'):
        response = get_llm_response(st.session_state.collection_name, question, st.session_state.ai_company,
                                    st.session_state.llm_model, st.session_state.embedding_model)
        st.session_state.response = response
        st.session_state.messages.append({"role": "assistant", "content": st.session_state.response})
        st.chat_message("assistant").write(st.session_state.response)
