# Import necessary libraries
import streamlit as st
import requests

# Define a function to validate email using the provided API
def validate_email(email):
    # Check if email is provided
    if email:
        # Enter Your API KEY HERE
        api_key = "ema_live_ITkV5Pqq40WNdMLdjqMZlNcb4AEBrNvWiSFd1MYE"
        # URL for the email validation API
        url = f"https://api.emailvalidation.io/v1/info?apikey={api_key}&email={email}"

        try:
            # Send GET request to the API
            response = requests.get(url)
            # Check if response is successful (status code 200)
            if response.status_code == 200:
                # Extract JSON data from the response
                result = response.json()
                # Display the validation result
                display_result(result)
            else:
                # Display error message if response status code is not 200
                st.error("Error occurred while fetching data from the API.")
        except Exception as e:
            # Display error message if an exception occurs during API call
            st.error(f"An error occurred: {e}")
    else:
        # Display message if email is not provided
        st.warning("Please input your email address.")

# Define a function to display the validation result
def display_result(result):
    # Check if result is a dictionary
    if isinstance(result, dict):
        # Display each key-value pair with proper formatting
        st.markdown("## Validation Result:")
        for key, value in result.items():
            # Check if value is not None and not a boolean or float
            if value is not None and not isinstance(value, (bool, float)):
                # Check if value is not empty or whitespace
                if isinstance(value, str) and value.strip():
                    st.write(f"**{key.capitalize()}:** {value.capitalize()}")
        # Additional styling for the output
        st.markdown("-----------------------------------------------------")
        st.markdown("## Best Email Marketing Platform For Businesses: [Constant Contact](https://constant-contact.ibfwsl.net/aeducateweb) (Start For Free)")
    else:
        # Display error message if result is not a dictionary
        st.error("Error: Invalid response format")

# Main function to run the Streamlit application
def main():
    # Set page title and description
    st.title("Email Address Validator")
    st.write("This app validates the provided email address using an external API.")

    # Collect email address from the user using a text input widget
    email = st.text_input("Enter the email address to validate:")

    # Check if the user has entered an email address
    if st.button("Validate"):
        # Check if the email is a valid format
        if '@' not in email or '.' not in email:
            st.warning("Invalid input email address.")
        else:
            # Call the validate_email function with the provided email address
            validate_email(email)

# Entry point of the Streamlit application
if __name__ == "__main__":
    main()
