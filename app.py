# Import libraries
import streamlit as st

# --- PAGE SETUP ---
main_page = st.Page(
    "views/chat_pdf.py",
    title="Chat with PDF",
    icon=":material/upload_file:",
    default=True,
)

admin_page = st.Page(
    "views/admin.py",
    title="Configuration",
    icon=":material/admin_panel_settings:",
)

about_page = st.Page(
    "views/about.py",
    title="About",
    icon=":material/info:",
)

pg = st.navigation({
    "Admin": [admin_page],
    "Home": [main_page],
    "About": [about_page],
                    })

pg.run()
