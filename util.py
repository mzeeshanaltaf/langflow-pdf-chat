from langflow.load import run_flow_from_json
import streamlit as st
import tempfile
import os


def configure_llm_model():
    # Configuration for AI Company selection
    ai_company = select_ai_company()
    model = ''
    app_activation = False
    if ai_company == 'OpenAI':
        openai_api_key, app_activation = openai_api_key_configuration()
        model = openai_model_selection()
        st.session_state.openai_api_key = openai_api_key

    elif ai_company == 'Google':
        google_api_key, app_activation = google_api_key_configuration()
        model = google_model_selection()
        st.session_state.google_api_key = google_api_key

    elif ai_company == 'Groq':
        groq_api_key, app_activation = groq_api_key_configuration()
        model = groq_model_selection()
        st.session_state.groq_api_key = groq_api_key

    return ai_company, model, app_activation


def configure_embedding_model():
    embedding_model = embedding_configuration()
    app_activation = False
    if embedding_model == 'OpenAI':
        openai_embedding_api_key, app_activation = openai_embedding_api_key_configuration()
        st.session_state.openai_embedding_api_key = openai_embedding_api_key
    elif embedding_model == 'HuggingFace':
        hf_embedding_api_key, app_activation = hf_embedding_api_key_configuration()
        st.session_state.hf_embedding_api_key = hf_embedding_api_key

    return embedding_model, app_activation


# Function to configure options to select AI company
def select_ai_company():
    st.subheader("Select Company 🏢")
    ai_company = st.selectbox('Select the AI Company', ('', 'OpenAI', 'Google', 'Groq'),
                              label_visibility="collapsed")
    return ai_company


# Function for OpenAI API configuration
def openai_api_key_configuration():
    st.subheader("API Key🔑")
    openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password",
                            help='Get API Key from: https://platform.openai.com/api-keys')
    if openai_api_key == '':
        st.warning('Enter OpenAI API Key ️')
        app_activation = False
    elif openai_api_key.startswith('sk-') and (len(openai_api_key) == 56):
        st.success('Lets Proceed!', icon='️👉')
        app_activation = True
    else:
        st.warning('Please enter the correct API Key 🗝️!', icon='⚠️')
        app_activation = False
    return openai_api_key, app_activation


# Function for Google API configuration
def google_api_key_configuration():
    st.subheader("API Key🔑")
    google_api_key = st.text_input("Enter your Google API Key:", type="password",
                            help='Get API Key from: https://platform.openai.com/api-keys')
    if google_api_key == '':
        st.warning('Enter Google API Key ️')
        app_activation = False
    elif google_api_key.startswith('AI') and (len(google_api_key) == 39):
        st.success('Lets Proceed!', icon='️👉')
        app_activation = True
    else:
        st.warning('Please enter the correct API Key 🗝️!', icon='⚠️')
        app_activation = False
    return google_api_key, app_activation


# Function for Groq API configuration
def groq_api_key_configuration():
    st.subheader("API Key🔑")
    groq_api_key = st.text_input("Enter your Groq API Key:", type="password",
                                 help='Get Groq API Key from: https://console.groq.com/keys')
    if groq_api_key == '':
        st.warning('Enter Groq API Key')
        app_activation = False
    elif groq_api_key.startswith('gsk_') and (len(groq_api_key) == 56):
        st.success('Lets Proceed!', icon='️👉')
        app_activation = True
    else:
        st.warning('Please enter the correct API Key 🗝️!', icon='⚠️')
        app_activation = False
    return groq_api_key, app_activation


# Function for HF API key configuration
def hf_embedding_api_key_configuration():
    st.subheader("API Key🔑")
    hf_api_key = st.text_input("Enter your HF API Key:", type="password",
                               help='Get Groq API Key from: https://console.groq.com/keys')
    if hf_api_key == '':
        st.warning('Enter HF API Key')
        app_activation = False
    elif hf_api_key.startswith('hf_') and (len(hf_api_key) == 37):
        st.success('Lets Proceed!', icon='️👉')
        app_activation = True
    else:
        st.warning('Please enter the correct API Key 🗝️!', icon='⚠️')
        app_activation = False
    return hf_api_key, app_activation


# Function for OpenAI Embedding API key configuration
def openai_embedding_api_key_configuration():
    st.subheader("API Key🔑")
    openai_api_key = st.text_input("Enter your OpenAI Embedding API Key:", type="password",
                            help='Get API Key from: https://platform.openai.com/api-keys')
    if openai_api_key == '':
        st.warning('Enter OpenAI API Key ️')
        app_activation = False
    elif openai_api_key.startswith('sk-') and ((len(openai_api_key) == 51) or (len(openai_api_key) == 56)):
        st.success('Lets Proceed!', icon='️👉')
        app_activation = True
    else:
        st.warning('Please enter the correct API Key 🗝️!', icon='⚠️')
        app_activation = False
    return openai_api_key, app_activation


# Function to configure options to select available Google models
def openai_model_selection():
    st.subheader("Model Selection🤖📚")
    model = st.selectbox('Select the Model', ('gpt-4o-mini', 'gpt-4o', 'gpt-4', 'gpt-3.5-turbo',
                                              'gpt-3.5-turbo-0125'), label_visibility="collapsed")
    return model


# Function to configure options to select available Google models
def google_model_selection():
    st.subheader("Model Selection🤖📚")
    model = st.selectbox('Select the Model', ('gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-1.0-pro',
                                              'gemini-1.0-pro-vision'), label_visibility="collapsed")
    return model


# Function to configure options to select available Groq models
def groq_model_selection():
    st.subheader("Model Selection🤖📚")
    model = st.selectbox('Select the Model', ('gemma2-9b-it', 'gemma-7b-it', 'llama-3.1-70b-versatile',
                                              'llama-3.1-8b-instant', 'llama3-groq-70b-8192-tool-use-preview',
                                              'llama3-groq-8b-8192-tool-use-preview',
                                              'llama3-70b-8192', 'llama3-8b-8192',
                                              'mixtral-8x7b-32768'), label_visibility="collapsed")
    return model


def embedding_configuration():
    st.subheader("Embedding Model Selection")
    embedding_model = st.selectbox('Select the Embedding Model', ('', 'OpenAI', 'HuggingFace'),
                                   label_visibility="collapsed")
    return embedding_model


def get_file_path(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        temp_pdf_path = temp_pdf.name
        filename, _ = os.path.splitext(uploaded_file.name)
        return temp_pdf_path, filename


def create_vector_db(uploaded_file, embedding_model):
    file_path, file_name = get_file_path(uploaded_file)
    collection_name = file_name + "_" + embedding_model  # Make the vector db collection name same as filename

    if embedding_model == "OpenAI":
        create_vector_db_openai(collection_name, file_path)

    elif embedding_model == "HuggingFace":
        create_vector_db_hf(collection_name, file_path)

    return collection_name


def create_vector_db_openai(collection_name, file_path):
    TWEAKS = {
        "AstraDB-gEyqU": {"api_endpoint": 'ASTRA_DB_API_ENDPOINT',
                          "token": "ASTRA_DB_APPLICATION_TOKEN",
                          "collection_name": collection_name},
        "File-nVOlf": {"path": file_path},
        "SplitText-uaSmV": {},
        "OpenAIEmbeddings-tDtW8": {"openai_api_key": "OPENAI_EMBEDDING_API_KEY"}
    }

    with st.spinner('Creating Vector DB ...'):
        result = run_flow_from_json(flow="vs_astradb_openai.json",
                                    input_value="message",
                                    fallback_to_env_vars=True,  # False by default
                                    tweaks=TWEAKS)
        st.success('Vector DB has been created successfully!')


def create_vector_db_hf(collection_name, file_path):
    TWEAKS = {
        "AstraDB-2WGg8": {"api_endpoint": 'ASTRA_DB_API_ENDPOINT',
                          "token": "ASTRA_DB_APPLICATION_TOKEN",
                          "collection_name": collection_name},
        "File-68wml": {"path": file_path},
        "SplitText-vHnqd": {},
        "HuggingFaceInferenceAPIEmbeddings-wC6aZ": {"api_key": "HUGGING_FACE_API_KEY",
                                                    "api_url": "HF_API_URL",
                                                    "model_name": "BAAI/bge-large-en-v1.5"}
    }

    with st.spinner('Creating Vector DB ...'):
        result = run_flow_from_json(flow="vs_astradb_hf.json",
                                    input_value="message",
                                    fallback_to_env_vars=True,  # False by default
                                    tweaks=TWEAKS)
        st.success('Vector DB has been created successfully!')


def get_llm_response(collection_name, question, ai_company, model, embedding_model):
    if ai_company == 'OpenAI' and embedding_model == "OpenAI":
        return llm_openai_embedding_openai(collection_name, question, model)
    elif ai_company == 'Google' and embedding_model == "OpenAI":
        return llm_gemini_embedding_openai(collection_name, question, model)
    elif ai_company == 'Groq' and embedding_model == "OpenAI":
        return llm_groq_embeddings_openai(collection_name, question, model)
    elif ai_company == 'OpenAI' and embedding_model == "HuggingFace":
        return llm_openai_embedding_hf(collection_name, question, model)
    elif ai_company == 'Google' and embedding_model == "HuggingFace":
        return llm_gemini_embedding_hf(collection_name, question, model)
    elif ai_company == 'Groq' and embedding_model == "HuggingFace":
        return llm_groq_embeddings_hf(collection_name, question, model)


def llm_openai_embedding_openai(collection_name, question, model):
    TWEAKS = {
        "ChatInput-vMnxM": {},
        "ParseData-8oSv3": {},
        "Prompt-fr6Sg": {},
        "ChatOutput-mIOFr": {},
        "OpenAIModel-sfHtD": {"openai_api_key": 'OPENAI_API_KEY',
                              "model_name": model},
        "AstraDB-prrD7": {"api_endpoint": 'ASTRA_DB_API_ENDPOINT',
                          "token": "ASTRA_DB_APPLICATION_TOKEN",
                          "collection_name": collection_name},
        "OpenAIEmbeddings-qdIm0": {"openai_api_key": 'OPENAI_EMBEDDING_API_KEY'}
    }

    output = run_flow_from_json(flow="chat_with_pdf_openai_embeddings_openai.json",
                                input_value=question,
                                fallback_to_env_vars=True,  # False by default
                                tweaks=TWEAKS)
    return output[0].outputs[0].messages[0].message


def llm_openai_embedding_hf(collection_name, question, model):
    TWEAKS = {
        "ChatInput-vOCBK": {},
        "ParseData-kNNGD": {},
        "Prompt-gMVIv": {},
        "ChatOutput-v6RpM": {},
        "OpenAIModel-MEJ5P": {"openai_api_key": 'OPENAI_API_KEY',
                              "model_name": model},
        "AstraDB-uM9oj": {"api_endpoint": 'ASTRA_DB_API_ENDPOINT',
                          "token": "ASTRA_DB_APPLICATION_TOKEN",
                          "collection_name": collection_name},
        "HuggingFaceInferenceAPIEmbeddings-kZsLZ": {"api_key": "HUGGING_FACE_API_KEY",
                                                    "api_url": "HF_API_URL",
                                                    "model_name": "BAAI/bge-large-en-v1.5"}
    }
    output = run_flow_from_json(flow="chat_with_pdf_openai_embeddings_hf.json",
                                input_value=question,
                                fallback_to_env_vars=True,  # False by default
                                tweaks=TWEAKS)
    return output[0].outputs[0].messages[0].message


def llm_gemini_embedding_openai(collection_name, question, model):
    TWEAKS = {
        "ChatInput-52jFb": {},
        "ParseData-fbJt6": {},
        "Prompt-aGcfJ": {},
        "ChatOutput-iLXj3": {},
        "AstraDB-2v74G": {"api_endpoint": 'ASTRA_DB_API_ENDPOINT',
                          "token": "ASTRA_DB_APPLICATION_TOKEN",
                          "collection_name": collection_name},
        "GoogleGenerativeAIModel-OVdPm": {"google_api_key": 'GOOGLE_API_KEY', "model_name": model},
        "OpenAIEmbeddings-UwJRs": {"openai_api_key": 'OPENAI_EMBEDDING_API_KEY'}
    }
    output = run_flow_from_json(flow="chat_with_pdf_gemini_embedding_openai.json",
                                input_value=question,
                                fallback_to_env_vars=True,  # False by default
                                tweaks=TWEAKS)
    return output[0].outputs[0].messages[0].message


def llm_gemini_embedding_hf(collection_name, question, model):
    TWEAKS = {
        "ChatInput-52jFb": {},
        "ParseData-fbJt6": {},
        "Prompt-aGcfJ": {},
        "ChatOutput-iLXj3": {},
        "AstraDB-2v74G": {"api_endpoint": 'ASTRA_DB_API_ENDPOINT',
                          "token": "ASTRA_DB_APPLICATION_TOKEN",
                          "collection_name": collection_name},
        "GoogleGenerativeAIModel-OVdPm": {"google_api_key": 'GOOGLE_API_KEY', "model_name": model},
        "HuggingFaceInferenceAPIEmbeddings-Vx0Ec": {"api_key": "HUGGING_FACE_API_KEY",
                                                    "api_url": "HF_API_URL",
                                                    "model_name": "BAAI/bge-large-en-v1.5"}
    }
    output = run_flow_from_json(flow="chat_with_pdf_gemini_embedding_hf.json",
                                input_value=question,
                                fallback_to_env_vars=True,  # False by default
                                tweaks=TWEAKS)
    return output[0].outputs[0].messages[0].message


def llm_groq_embeddings_openai(collection_name, question, model):
    TWEAKS = {
        "ChatInput-JtbrK": {},
        "ParseData-z7279": {},
        "Prompt-Z6pAj": {},
        "ChatOutput-DJasm": {},
        "AstraDB-NSfP9": {"api_endpoint": 'ASTRA_DB_API_ENDPOINT',
                          "token": "ASTRA_DB_APPLICATION_TOKEN",
                          "collection_name": collection_name},
        "OpenAIEmbeddings-X9Uyn": {"openai_api_key": 'OPENAI_EMBEDDING_API_KEY'},
        "GroqModel-PqJIq": {"groq_api_key": "GROQ_API_KEY", "model_name": model}
    }
    output = run_flow_from_json(flow="chat_with_pdf_groq_embedding_openai.json",
                                input_value=question,
                                fallback_to_env_vars=True,  # False by default
                                tweaks=TWEAKS)
    return output[0].outputs[0].messages[0].message


def llm_groq_embeddings_hf(collection_name, question, model):
    TWEAKS = {
        "ChatInput-JtbrK": {},
        "ParseData-z7279": {},
        "Prompt-Z6pAj": {},
        "ChatOutput-DJasm": {},
        "AstraDB-NSfP9": {"api_endpoint": 'ASTRA_DB_API_ENDPOINT',
                          "token": "ASTRA_DB_APPLICATION_TOKEN",
                          "collection_name": collection_name},
        "HuggingFaceInferenceAPIEmbeddings-Jm491": {"api_key": "HUGGING_FACE_API_KEY",
                                                    "api_url": "HF_API_URL",
                                                    "model_name": "BAAI/bge-large-en-v1.5"},
        "GroqModel-PqJIq": {"groq_api_key": "GROQ_API_KEY", "model_name": model}
    }
    output = run_flow_from_json(flow="chat_with_pdf_groq_embedding_hf.json",
                                input_value=question,
                                fallback_to_env_vars=True,  # False by default
                                tweaks=TWEAKS)
    return output[0].outputs[0].messages[0].message
