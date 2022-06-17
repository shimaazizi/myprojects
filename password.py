import string
import random
characters=list(string.ascii_letters +string.digits +string.punctuation)
#Enter password length
length=int(input("Enter password length:"))
#creat password
password="".join(random.sample(characters,length))
print(password)