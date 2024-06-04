import google.generativeai as genai
import time
context= " " 
current_file = ' '
file_number=1
promptnum = 0
key = 'AIzaSyAqsSXE1FJo0XvqDE8pMrVyi6r1K__ruY4'
f1 = open('f1.text', 'r')
model = ''
error = False
user_input =''
while True:
    genai.configure(api_key=key) 
    if error==True: model = 'gemini-1.0-pro-latest'
    if error == False: 
        user_input = input ("input: ")
        model = 'gemini-1.5-flash-latest'
    print ("model:", model ,"\n _______________________")
    try:
        if model == 'gemini-1.0-pro-latest': total_input = user_input
        if model == 'gemini-1.5-flash-latest': total_input = context + "\n" + user_input
        model = genai.GenerativeModel(model)
        response = model.generate_content(total_input)
        print(response.text)
        if model == 'gemini-1.5-flash-latest': context = context + "\n" + response.text + "\n"
        if model == 'gemini-1.0-pro-latest': context = context
        #file_number +=1
        error = False
    except: 
        error=True
        print ("_________________________ \n AN ERROR HAS OCCURED WARNING WARNING AN ERROR HAS OCCURED \n ____________________________________")
    
print (promptnum)
