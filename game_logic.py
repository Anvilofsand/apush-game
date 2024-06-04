import google.generativeai as genai
import time
promptnum = 0
file_number = int(input ("""pick your adventure
1. ride of paul revere
                         choice: """)) -1
file_list = ["f1.text", 0, 0, 0]
current_file = file_list [file_number]
current_file = open(current_file, "r")
context = current_file.read () + "off of this/these document(s) you will make an adventure that is historically accurate. You will keep the user on task and make sure to stop us from going to far from the story. you will run it in a Dnd like style where you are the game master where you descirbe the events and consequences of my actions to me once I do them; you are not to give options but wait for me to tell you what I am doing. I am the main character in whatever historical event we are in. after we have gone though the whole story you will give me a score out of 10 for how well I did. 10 is the highest 1 is the lowest. \n \n \n"
key = 'AIzaSyAqsSXE1FJo0XvqDE8pMrVyi6r1K__ruY4'
model = ''
error = False
user_input =''
while True:
    genai.configure(api_key=key) 
    if error==True: 
        model = 'gemini-1.0-pro-latest'
        error_input = ''
    if error == False: 
        user_input = input ("input: ")
        model = 'gemini-1.5-flash-latest'
    print ("model:", model ,"\n _______________________")
    try:
        if model == 'gemini-1.0-pro-latest': total_input = error_input
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
