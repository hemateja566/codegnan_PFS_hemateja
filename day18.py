
import pyttsx3

engine=pyttsx3.init()

def speak_text(text):
    engine.say(text)
    

speak_text("Hello ,I am your assistant")
speak_text("Can i know your name please")
speak_text(f"good to know you teja, how can i help you")
engine.runAndWait()
'''
import pyttsx3

engine=pyttsx3.init()

def speak_text(text):
    engine.say(text)
    
user_text= input("enter your message:").lower()
if "my name is" in user_text:
    name=user_text.split("my name is")[-1].strip()
elif "name is" in user_text:
    name=user_text.split("name is")[-1].strip()

if user_text in ["hi","hello","hey"]:
    response="Hello ! how can i help you?"
elif "name" in user_text:
    response=f"hello {name},how can i help you?"
else:
    response="sorry, i didn't understand that."
print(response)
speak_text(response)
engine.runAndWait()
  '''  
