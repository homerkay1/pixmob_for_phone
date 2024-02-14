# Import the Streamlit library
import streamlit as st

# Set the background color
background_color = 'red'

# Use Streamlit to create a webpage
st.markdown(
    f"""
    <style>
        body {{
            background-color: {background_color};
            margin: 0;
            height: 100vh;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Display any additional content if needed
st.write("This is a Streamlit app with a red background.")
