import pyttsx3 as p
import speech_recognition as sr
import wolframalpha 



engine=p.init()
def speak(text):
   engine.say(text)
   engine.runAndWait()

r=sr.Recognizer()

speak("Hello,Sir")
print("Hello,Sir")
speak("I am Alexa How are you ")
print("I am Alexa How are you")


with  sr.Microphone() as source:
   r.energy_threshold=10000
   r.adjust_for_ambient_noise(source,1.2)
   print("Listening...")
   audio= r.listen(source)
   text=r.recognize_google(audio)
   print("You:",text)
if "What" and "about" and "you" :
   speak("I am also fine having a good day sir")
   print("I am also fine having a good day sir")
   speak("What can i do you sir")
   print("What can i do you sir")

   app_id = 'K7Y6PX-UYP2WGJ49Q'

client = wolframalpha.Client(app_id)

with  sr.Microphone() as source:
   r.energy_threshold=10000
   r.adjust_for_ambient_noise(source,1.2)
   print("Listening...")
   audio= r.listen(source)
   text=r.recognize_google(audio)
   print("You",text)

res = client.query(text)

for pod in res.pods:
    print(pod.title + ":")
    for sub in pod.subpods:
        speak(sub.plaintext)



      