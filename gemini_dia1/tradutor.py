import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY= "AIzaSyDAfjeSV9J9O6mqo3owI_R05VxocBlnivA"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Gemini FIPP Translator")
input_text = st.text_area("Digite aqui o texto que deseja traduzir", height=50)

if st.button("Traduzir"):
    if input_text:  
        prompt = "Traduza para o inglês: " + input_text
        response = model.generate_content(prompt)
        st.write(response.text)
    else:
        st.write("Por favor, digite um texto para traduzir")