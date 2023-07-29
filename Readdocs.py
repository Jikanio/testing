import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Function to generate a response using GPT-3.5 model
def generate_response(prompt_text, model, tokenizer):
    inputs = tokenizer(prompt_text, return_tensors="pt")
    outputs = model(**inputs)
    response = tokenizer.decode(outputs.logits[0], skip_special_tokens=True)
    return response

# Main Streamlit app code
def main():
    st.title("GPT-3.5 Chatbox")

    # Uploading documents
    uploaded_files = st.file_uploader("Upload Documents", accept_multiple_files=True)

    # Input web link
    web_link = st.text_input("Web Link")

    # Input user prompt
    user_prompt = st.text_area("Enter your prompt here:")

    # Load GPT-3.5 model and tokenizer
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # Process uploaded documents
    if uploaded_files:
        for file in uploaded_files:
            file_content = file.read()
            st.write(f"**Uploaded Document:** {file.name}")
            st.write(file_content)

            # Generate response based on the uploaded document
            response = generate_response(file_content.decode("utf-8"), model, tokenizer)
            st.write(f"**GPT-3.5 Response:** {response}")

    # Process web link
    if web_link:
        st.write(f"**Web Link:** {web_link}")

        # Generate response based on the web link
        # You might need to use a library like 'requests' to fetch the data from the web link
        response = generate_response(web_link, model, tokenizer)
        st.write(f"**GPT-3.5 Response:** {response}")

    # Process user prompt
    if user_prompt:
        st.write(f"**Your Prompt:** {user_prompt}")

        # Generate response based on the user prompt
        response = generate_response(user_prompt, model, tokenizer)
        st.write(f"**GPT-3.5 Response:** {response}")


if __name__ == "__main__":
    main()
