# pylint: disable-all

import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv
#  loading all the environment variables
load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# function to load Gemini Pro model and get responses
# model = genai.GenerativeModel("gemini-pro")
model = genai.GenerativeModel("gemini-2.0-flash")


def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# Initialize our streamlit app
st.set_page_config(page_title="Q&A demo")
st.header("GEMINI LLM APPLICATION")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# When submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)
