import streamlit as st
import pandas as pd
import requests
import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

def read_excel(file):
    df = pd.read_excel(file)
    return df.to_string(index=False)

def read_web_link(url):
    response = requests.get(url)
    return response.text

def main():
    st.title("Upload and Read Documents")
    st.write("Please upload an Excel file or provide a web link.")

    file = st.file_uploader("Upload an Excel file", type=["xlsx"])

    if file:
        text = read_excel(file)
        st.subheader("Uploaded Document Text:")
        st.write(text)

    web_link = st.text_input("Provide a web link:")
    if web_link:
        text = read_web_link(web_link)
        st.subheader("Web Link Text:")
        st.write(text)

    if file or web_link:
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
