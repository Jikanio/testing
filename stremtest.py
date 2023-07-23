#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def process_word_document(file):
    # Add your custom processing logic here
    # For demonstration purposes, we'll just print the content of the uploaded file.
    content = file.read()
    st.write("Uploaded Word Document Content:")
    st.write(content)

def main():
    st.title("Word Document Uploader")

    uploaded_file = st.file_uploader("Choose a Word document", type=["docx"])

    if uploaded_file is not None:
        st.write("File Uploaded!")
        process_word_document(uploaded_file)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




