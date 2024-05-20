import google.generativeai as genai

genai.configure(api_key='AIzaSyAqsSXE1FJo0XvqDE8pMrVyi6r1K__ruY4')
model = genai.GenerativeModel('gemini-pro')
context= " "
while True:
    response = model.generate_content(context + input(": "))
    print(response.text)
    context = context + response.text + " "