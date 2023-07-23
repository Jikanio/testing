#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install streamlit requests


# In[3]:


import streamlit as st
import requests


# In[5]:


BASE_URL = "http://sellerapi.sellercenter.jumia.com/"
API_KEY = "a07e4537d1cc04eb24dfda9303d572a584be6379"


# In[6]:


def main():
    st.title("Jumia Product Stock Level App")
    st.write("Enter the product information to fetch stock levels:")

    # User input for product information
    product_info = st.text_input("Enter Product Name, ID, or SKU:")

    if st.button("Fetch Stock Levels"):
        # Fetch and display stock levels
        stock_level = get_stock_level(product_info)

        if stock_level is not None:
            st.success(f"Stock Level for {product_info}: {stock_level}")
        else:
            st.error("Product not found or error fetching stock level.")

# Function to fetch stock level from Jumia API
def get_stock_level(product_info):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"product_info": product_info}

    try:
        response = requests.get(BASE_URL + "stock-level", headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return data["stock_level"]
        else:
            return None

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching stock level: {e}")
        return None

if __name__ == "__main__":
    main()


# In[ ]:




