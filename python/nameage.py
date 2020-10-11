import time

start_time = time.time()
##### In class lab practice that shows sleep time with bunch of personal craps
print("What's your name?")
print("Please type 'your name'")
myName = input() 
while myName != 'your name':
    print("This is not \"your name\". Please type \"your name\"?") 
    myName = input() 

print("You typed " + myName + ". Haha.") 
print("Hello " + myName + ". That is a good name. How old are you?")
myAge = int(input())

if myAge < 14:
    print("You're not even a teenager yet!")
elif myAge == 14:
    print("You're a teenager now... yay...")
elif myAge > 14 and myAge < 25:
    print("You're young and dumb silly-billy!")
elif myAge >= 25 and myAge < 60:
    print("You're super adulting...") 
else:
    print("... and you're not paralyzed yet?")
###set the programAge prior to giving to the user
programAge = int(time.time() - start_time)

print("%s? That's funny, I'm only %s seconds old." % (myAge, programAge)) 
print("I wish I was %s years old" % (myAge * 2)) 
time.sleep(3)
print("I'm tired. I'm done. Goodnight! Catch you later.") 