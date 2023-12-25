import os
import requests
import PyPDF2
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
    pdf_link = None  # Set online link to None
elif pdf_option == "Provide Online PDF Link":
    pdf_link = st.text_input("Enter the URL of the PDF file:")
    pdf_file = None  # Set local file to None

model_name = st.selectbox("Select the model you want to use", ("gpt-3.5-turbo", "gpt-4"))
temperature = st.slider("Set temperature", 0.1, 1.0, 0.5, 0.1)

if pdf_file is not None:
    query_engine(pdf_file, model_name, temperature)
elif pdf_link:
    try:
        # Download PDF content from the provided link
        response = requests.get(pdf_link)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        
        # Save the downloaded content to a temporary file
        temp_pdf_path = "temp.pdf"
        with open(temp_pdf_path, "wb") as pdf_file:
            pdf_file.write(response.content)
        
        # Pass the temporary PDF file to the query_engine function
        query_engine(temp_pdf_path, model_name, temperature)
        
    except requests.exceptions.RequestException as e:
        st.error(f"Error downloading PDF from the provided link: {e}")
    finally:
        # Remove the temporary PDF file
        os.remove(temp_pdf_path)
else:
    st.error("Please upload a local PDF file or provide an online PDF link")
