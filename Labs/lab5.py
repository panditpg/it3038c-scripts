###In this guessing number game, the computer will generate a random number between 1 to 10, and the user will have to guess it in 5 attempts. 
###So, based on the user’s guess, the computer will give several hints if the number is high or low and as the user guess matches the number, 
###the computer will then print the answer along with the number of attempts. 

###Code goes as follows:
###A python module named random is used to generate a random number.
import random

###Again, the random module is used to generate a number between 1 to 10 and store it in a variable named number.
 
number = random.randint(1, 10)
###The user is prompted to enter the name and store it to a variable named player_name. 

player_name = input("Hello, What's your name?")

###Created a variable named nad assigned 0 to it. But later on this value will be increased on each iteration of the while loop.

number_of_guesses = 0

###Print a string that includes the player name.
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

###In the first line, the controlling expression of while loop is defined. This game will allow user five attempts to guess the number so less than five is due to number of guesses variable is already assigned to zero. Within the loop, the input is taken from the user and stored it in the guess variable but the user input is string object and performed mathematical operation to convert in integer through python’s inbuilt int()method.

while number_of_guesses < 5:
    guess = int(input())

###Incrementing a value of numberofguesses variable by 1.
    number_of_guesses += 1
    
### Comparing if the guess is less than the generated number if this statement evaluates to true, we print the corresponding Guess.
    if guess < number:
        print('Your guess is too low')
    
### Checking if the guess is greater than the generated number.
    if guess > number:
        print('Your guess is too high')
    
### Break keyword terminates the loop entirely so when the guess is equal to the generated number, loop gets terminated.
    if guess == number:
        break

### Added another pair of condition statement.
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
<<<<<<< HEAD

    ###sources: A. https://djangocentral.com/creating-a-guessing-game-in-python/
    ###B. https://stackoverflow.com/questions/53038112/number-guessing-game-python/53038208

=======
  
  ###sources: A.  https://stackoverflow.com/questions/53038112/number-guessing-game-python/53038208
  ###B. https://djangocentral.com/creating-a-guessing-game-in-python/
>>>>>>> 25a8877f4ba7a0bca9009d48197c7e315329d6e1
