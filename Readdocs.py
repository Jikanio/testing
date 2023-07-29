import streamlit as st
import pandas as pd
import requests
import docx2txt
import openai

# Set your OpenAI API key here
openai.api_key = 'mxvJfnZqi2jGGtOtab66T3BlbkFJ4HTPilTcYW8ZtKEnLIyW'

def read_docx(file):
    text = docx2txt.process(file)
    return text

def read_excel(file):
    df = pd.read_excel(file)
    return df.to_string(index=False)

def read_web_link(url):
    response = requests.get(url)
    return response.text

def main():
    st.title("Upload and Read Documents")
    st.write("Please upload a Word, PDF, or Excel file, or provide a web link.")

    file = st.file_uploader("Upload a file", type=["docx", "pdf", "xlsx"])

    if file:
        file_type = file.type
        if file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            text = read_docx(file)
        elif file_type == 'application/pdf':
            # Add code to read PDF here if needed
            text = "PDF file format is not supported yet."
        elif file_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            text = read_excel(file)
        else:
            st.error("Unsupported file format.")
            return

        st.subheader("Uploaded Document Text:")
        st.write(text)

        user_input = st.text_input("Ask a question or provide a prompt:")
        if user_input:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=text + "\nUser: " + user_input + "\nAI:",
                temperature=0.7,
                max_tokens=150,
                stop=["\n"],
            )
            ai_response = response.choices[0].text.strip()
            st.subheader("AI Response:")
            st.write(ai_response)


if __name__ == "__main__":
    main()
