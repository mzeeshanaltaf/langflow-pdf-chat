from util import *

# SIDEBAR CONFIGURATION
st.title("Configuration")
with st.expander('LLM Configuration'):
    ai_company, llm_model, app_activation = configure_llm_model()
    apply_button_llm = st.button("Apply", type="primary", key="button_llm", disabled=not app_activation)

    if apply_button_llm:
        st.session_state.ai_company = ai_company
        st.session_state.llm_model = llm_model
        st.session_state.app_activation = app_activation
        st.toast('Changes saved successfully!', icon='🎉')

with st.expander('Embedding Model Configuration'):
    embedding_model, app_activation = configure_embedding_model()

    apply_button_embeddings = st.button("Apply", type="primary", key="embeddings_llm",
                                        disabled=not app_activation)

    if apply_button_embeddings:
        st.session_state.embedding_model = embedding_model
        st.session_state.app_activation = app_activation
        st.toast('Changes saved successfully!', icon='🎉')

