import time

##### In class lab practice that shows sleep time with bunch of personal craps
print("What's your name?")
myName = input()
print("Hello " + myName + ". That is a good name. How old are you?")
myAge = int(input())
print("%s? That's funny, I'm only a few seconds old." % myAge) 
print("I wish I was %s years old" % (myAge * 2)) 
time.sleep(3)
print("I'm tired. I'm done. Goodnight! Catch you later.") 