"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""
import pathlib

import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


key = input("key: ")
history=" "

import google.generativeai as genai

genai.configure( api_key = key)

    # Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = { 
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

model = genai.GenerativeModel(
model_name="gemini-1.5-pro-latest",
safety_settings=safety_settings,
  
generation_config=generation_config,)
chat_session = model.start_chat()
while True:
  user_input = input ("message:")
  message = history + "" + user_input
  response = chat_session.send_message(user_input)
  message = history + "\n" + user_input
  history = message + "\n" + str(response.text)
  print(response.text) 
#print(chat_session.history

