import streamlit as st
import pypdf

file = st.file_uploader("Upload a PDF file", type=["pdf"])
if file is not None:
    reader = pypdf.PdfReader(file)
    page = reader.pages[0]
    text = page.extract_text()
    st.write(text)