import os
from functions import sidebar_stuff2, query_engine, save_file, remove_file

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

sidebar_stuff2()

pdf_option = st.radio("Select PDF source:", ("Upload Local PDF", "Provide Online PDF Link"))

if pdf_option == "Upload Local PDF":
    pdf_file = st.file_uploader(
        "Upload a PDF file to unleash the power of AI and have a conversation with your PDFs ⬇️ ",
        type=["pdf"],
    )
elif pdf_option == "Provide Online PDF Link":
    pdf_link = st.text_input("Enter the URL of the PDF file:")
    pdf_file = None  # Placeholder for online link handling, modify as needed

model_name = st.selectbox("Select the model you want to use", ("gpt-3.5-turbo", "gpt-4"))
temperature = st.slider("Set temperature", 0.1, 1.0, 0.5, 0.1)

if pdf_file is not None:
    if pdf_file:
        query_engine(pdf_file, model_name, temperature)
    else:
        # Handle online link processing here (e.g., download the file)
        # Modify the following line based on your requirements
        st.error("Online PDF handling is not implemented yet.")
else:
    st.error("Please upload a local PDF file or provide an online PDF link")
