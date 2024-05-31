import google.generativeai as genai

genai.configure(api_key='AIzaSyAqsSXE1FJo0XvqDE8pMrVyi6r1K__ruY4')
model = genai.GenerativeModel('gemini-pro')
context= " "
current_file = ''
while True:
    response = model.generate_content(current_file + "\n" + context + input(": "))
    print(response.text)
    context = context + "\n" + response.text + "\n"
    file_number +=1