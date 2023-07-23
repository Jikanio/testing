{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "42261467-d83a-4f9e-9d51-91a1e56ef6b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "def process_word_document(file):\n",
    "    # Add your custom processing logic here\n",
    "    # For demonstration purposes, we'll just print the content of the uploaded file.\n",
    "    content = file.read()\n",
    "    st.write(\"Uploaded Word Document Content:\")\n",
    "    st.write(content)\n",
    "\n",
    "def main():\n",
    "    st.title(\"Word Document Uploader\")\n",
    "\n",
    "    uploaded_file = st.file_uploader(\"Choose a Word document\", type=[\"docx\"])\n",
    "\n",
    "    if uploaded_file is not None:\n",
    "        st.write(\"File Uploaded!\")\n",
    "        process_word_document(uploaded_file)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ca846b1-5855-4e63-b240-19ff1baa8ed2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a120e37-0ca9-4265-964a-8f6214f88e76",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
