import google.generativeai as genai

GOOGLE_API_KEY= "AIzaSyDAfjeSV9J9O6mqo3owI_R05VxocBlnivA"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
prompt = "Conte a história do Windows em 2 paragráfos"
response = model.generate_content(prompt)
print(response.text)



print('Oi, Gemini!')