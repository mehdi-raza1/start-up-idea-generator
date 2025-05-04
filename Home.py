import streamlit as st


st.set_page_config(
    page_title="NIC | Startup Idea Generator",
    page_icon="💡",
    layout="centered"
)


st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Welcome to NIC's Startup Idea Generator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Empowering Entrepreneurs with AI</h3>", unsafe_allow_html=True)


st.divider()


st.markdown("### What is this?")
st.write("""
This AI-powered tool helps you brainstorm startup ideas by describing a problem or theme.
It provides a full startup plan including:
- Target market
- Business model
- Revenue streams
- Tech stack
""")


st.markdown("### How does it work?")
st.write("""
1. Click on **Startup Idea Generator** from the sidebar.
2. Enter a problem or theme.
3. Let AI generate a startup idea for you!
""")


st.divider()
st.markdown("<p style='text-align: center;'>Made with by <strong>Mehdi Raza</strong> for National Incubation Center</p>", unsafe_allow_html=True)
