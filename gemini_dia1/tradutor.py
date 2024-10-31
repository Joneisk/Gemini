import streamlit as st

st.title("Gemini FIPP Translator")
input_text = st.text_area("Digite aqui o texto que deseja traduzir", height=50)
st.button("Traduzir")
