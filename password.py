import string
import random
characters=list(string.ascii_letters +string.digits +string.punctuation)
length=int(input("Enter password length:"))
password="".join(random.sample(characters,length))
print(password)