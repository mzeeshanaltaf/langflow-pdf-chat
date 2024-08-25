import streamlit as st
import os


def select_ai_company():
    st.subheader("Select Company 🏢")
    ai_company = st.selectbox('Select the AI Company', ('OpenAI', 'Google', 'Groq'),
                              label_visibility="collapsed")
    return ai_company


def openai_api_key_configuration(key):
    st.subheader("API Key🔑")
    api_key = st.text_input("Enter your OpenAI API Key:", type="password", key=key,
                            help='Get API Key from: https://platform.openai.com/api-keys')
    if api_key == '':
        st.warning('Enter OpenAI API Key ️')
        app_activation = False
    elif api_key.startswith('sk-') and ((len(api_key) == 51) or (len(api_key) == 56)):
        st.success('Lets Proceed!', icon='️👉')
        app_activation = True
    else:
        st.warning('Please enter the correct API Key 🗝️!', icon='⚠️')
        app_activation = False
    return api_key, app_activation


# Function for Google API configuration
def google_api_key_configuration():
    st.subheader("API Key🔑")
    api_key = st.text_input("Enter your Google API Key:", type="password",
                            help='Get API Key from: https://platform.openai.com/api-keys')
    if api_key == '':
        st.warning('Enter Google API Key ️')
        app_activation = False
    elif api_key.startswith('AI') and (len(api_key) == 39):
        st.success('Lets Proceed!', icon='️👉')
        app_activation = True
    else:
        st.warning('Please enter the correct API Key 🗝️!', icon='⚠️')
        app_activation = False
    return api_key, app_activation


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


# Function for HF API configuration
def hf_api_key_configuration():
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

@st.dialog("LLM Configuration")
def configure_llm_model():
    # Configuration for AI Company selection
    ai_company = select_ai_company()
    model = ''
    if ai_company == 'OpenAI':
        openai_api_key, app_activation = openai_api_key_configuration(key='llm')
        model = openai_model_selection()
        os.environ['OPENAI_API_KEY'] = openai_api_key  # Set the environment variable for api key
    elif ai_company == 'Google':
        google_api_key, app_activation = google_api_key_configuration()
        model = google_model_selection()
        os.environ['OPENAI_API_KEY'] = google_api_key  # Set the environment variable for api key

    elif ai_company == 'Groq':
        groq_api_key, app_activation = groq_api_key_configuration()
        model = groq_model_selection()
        os.environ['OPENAI_API_KEY'] = groq_api_key  # Set the environment variable for api key

    apply_button_llm = st.button("Apply", type="primary", key="button_llm", disabled=not app_activation)
    return ai_company, model, app_activation


if st.button('Select LLM'):
    ai_company, llm_model, app_activation = configure_llm_model()

if st.button('Select Embedding Model'):
    pass
