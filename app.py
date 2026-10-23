import streamlit as st
import streamlit.components.v1 as components

# Set page to wide mode for the full dashboard experience
st.set_page_config(layout="wide", page_title="J.A.R.V.I.S. Command Center")

# Hide the default Streamlit header and footer for a clean look
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read your HTML file
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Embed the HTML into Streamlit using an iframe
    # You can adjust the height, but '100%' or a large number like 1000 works best for dashboards
    components.html(html_code, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("Error: The file 'index.html' was not found. Make sure it is in the same folder as app.py.")
