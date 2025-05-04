import streamlit as st
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Startup Idea Generator", page_icon="💡")

st.title("Start-Up Idea Generator")
st.markdown("Use AI to build a complete startup plan from your problem or theme idea!")

problem = st.text_area(
    "Describe the problem, theme, or idea: Optional: Add tags or themes (comma separated)",
    placeholder="e.g. Food waste in urban homes Sustainability, Smart Home, AI"
)

def generate_reply(user_message, llm):
    prompt = PromptTemplate(
        input_variables=["problem"],
        template="""
You are a world-class startup mentor.

Given the following problem:

Problem: {problem}

Generate a complete startup plan in which the user can easily understand their main focus.
Respond in clean Markdown.
"""
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(problem=user_message)

if st.button("Generate Startup Plan"):
    if not problem:
        st.warning("Please enter a problem or idea to continue.")
    else:
        with st.spinner("Generating your startup idea..."):
            try:
                api_key = st.secrets["api_keys"]["GEMINI_API_KEY"]
                genai.configure(api_key=api_key)
                llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
                ai_reply = generate_reply(problem, llm)
                st.markdown("---")
                st.markdown("### Generated Startup Plan")
                st.markdown(ai_reply)
            except Exception as e:
                st.error(f"Error generating startup plan: {e}")

st.divider()
st.markdown("<p style='text-align: center;'>Made with by <strong>Mehdi Raza</strong> for National Incubation Center</p>", unsafe_allow_html=True)
