import pyttsx3
text=input("what do I say?")
sound=pyttsx3.init()
sound.setProperty('rate',110)
#convert text to voice
sound.say(text) 
#play the voice 
sound.runAndWait()  




