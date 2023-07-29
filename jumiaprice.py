import streamlit as st
import requests
import hashlib
import hmac
import urllib.parse
from datetime import datetime

def get_product_data():
    # API URL
    api_url = "https://sellercenter-api.jumia.co.ke/"

    # API parameters
    params = {
        "Action": "GetProducts",
        "Filter": "all",
        "Format": "JSON",
        "Timestamp": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "UserID": "njuenew@gmail.com",
        "Version": "1.0",
    }

    # API key
    api_key = "a07e4537d1cc04eb24dfda9303d572a584be6379"

    # Concatenate and URL encode parameters
    concatenated = "&".join([f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items()])
    signature = hmac.new(api_key.encode(), concatenated.encode(), hashlib.sha256).hexdigest()

    # Add signature to parameters
    params["Signature"] = signature

    try:
        # Making the API request
        response = requests.get(api_url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Check if the response contains the expected keys
            if "ErrorResponse" in data and "Head" in data["ErrorResponse"] and "ErrorType" in data["ErrorResponse"]["Head"]:
                error_type = data["ErrorResponse"]["Head"]["ErrorType"]
                error_code = data["ErrorResponse"]["Head"]["ErrorCode"]
                error_message = data["ErrorResponse"]["Head"]["ErrorMessage"]
                st.write(f"Error: {error_type} (Code: {error_code}) - {error_message}")
            elif "SuccessResponse" in data and "Body" in data["SuccessResponse"] and "Products" in data["SuccessResponse"]["Body"]:
                products = data["SuccessResponse"]["Body"]["Products"]["Product"]

                # Create a list to store the product details
                product_list = []

                # Collecting product details
                for product in products:
                    product_info = {
                        "Product Name": product["Name"],
                        "Price": product["Price"],
                        "Sale Price": product["SalePrice"],
                        "URL": product["Url"],
                        "Main Image": product["MainImage"]
                    }
                    product_list.append(product_info)

                return product_list

            else:
                st.write("Error: Unexpected response format.")

        else:
            st.write("Error: Unable to fetch data from the API.")

    except requests.exceptions.RequestException as e:
        st.write("Error: ", e)

def main():
    st.title("Jumia Product Data")
    st.write("This web app displays product data from the Jumia API.")

    product_data = get_product_data()

    if product_data:
        st.table(product_data)

if __name__ == "__main__":
    main()
