import streamlit as st
import google.generativeai as gen_ai
from PIL import Image

# Set up Google Gemini-Pro AI model
GOOGLE_API_KEY = "AIzaSyDAfjeSV9J9O6mqo3owI_R05VxocBlnivA"
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel("gemini-1.5-flash")

# Título do aplicativo
st.title("Comer Bem AI")

# Carregar a imagem
uploaded_file = st.file_uploader("Selecione a imagem", type=["jpg", "jpeg", "png"])

# Exibir a imagem se o usuário fizer upload
if uploaded_file is not None:
    my_image = Image.open(uploaded_file)
    st.image(my_image)
    PROMPT = """Analise a imagem fornecida e responda com as seguintes informações:
                - Verifique se a imagem representa um alimento. Se sim, continue a análise; 
                caso contrário, responda que a imagem não é de um alimento.
                - Se a imagem for de um alimento, determine se é saudável ou não, 
                baseando-se em características comuns de alimentos saudáveis, 
                como baixos níveis de gordura saturada, alto teor de fibras e 
                nutrientes essenciais. Considere alimentos naturais e integrais 
                como saudáveis e alimentos altamente processados, com adição 
                de açúcar ou gordura saturada, como menos saudáveis.
                - Dê uma breve justificativa para a sua classificação 
                de saudável ou não saudável.
                Responda com clareza e objetividade.
            """
    response = model.generate_content([PROMPT, my_image])
    st.write(response.text)
else:
    st.write("Por favor, selecione uma imagem.")


