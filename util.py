from langflow.load import run_flow_from_json
import streamlit as st
import tempfile
import os

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
os.environ['ASTRA_DB_APPLICATION_TOKEN'] = st.secrets['ASTRA_DB_APPLICATION_TOKEN']
os.environ['ASTRA_DB_API_ENDPOINT'] = st.secrets['ASTRA_DB_API_ENDPOINT']


def get_file_path(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name
        filename, _ = os.path.splitext(uploaded_file.name)
        return temp_pdf_path, filename


def create_vector_db(uploaded_file):
    file_path, file_name = get_file_path(uploaded_file)
    collection_name = file_name  # Make the vector db collection name same as filename
    TWEAKS = {
        "AstraDB-2WGg8": {"api_endpoint": 'ASTRA_DB_API_ENDPOINT',
                          "token": "ASTRA_DB_APPLICATION_TOKEN",
                          "collection_name": collection_name},  # Make the Collection name same as file name
        "OpenAIEmbeddings-SsyZ0": {"openai_api_key": 'OPENAI_API_KEY'},
        "File-68wml": {"path": file_path},
        "SplitText-vHnqd": {}
    }

    with st.spinner('Creating Vector DB ...'):
        result = run_flow_from_json(flow="vs_astradb.json",
                                    input_value="message",
                                    fallback_to_env_vars=True,  # False by default
                                    tweaks=TWEAKS)
        st.success('Vector DB has been created successfully!')

    return collection_name


def get_llm_response(collection_name, question):
    TWEAKS = {
        "ChatInput-vOCBK": {},
        "ParseData-kNNGD": {},
        "Prompt-gMVIv": {},
        "ChatOutput-v6RpM": {},
        "OpenAIEmbeddings-oajZX": {"openai_api_key": 'OPENAI_API_KEY'},
        "OpenAIModel-MEJ5P": {"openai_api_key": 'OPENAI_API_KEY'},
        "AstraDB-uM9oj": {"api_endpoint": 'ASTRA_DB_API_ENDPOINT',
                          "token": "ASTRA_DB_APPLICATION_TOKEN",
                          "collection_name": collection_name}
    }
    output = run_flow_from_json(flow="chat_with_pdf.json",
                                input_value=question,
                                fallback_to_env_vars=True,  # False by default
                                tweaks=TWEAKS)
    return output[0].outputs[0].messages[0].message
