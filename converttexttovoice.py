import pyttsx3
text=input("what do I say?:")
sound=pyttsx3.init()
sound.setProperty('rate',110)
sound.say(text)
sound.runAndWait()



