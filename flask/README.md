##### Project 3: "Guess The Number" #####

#### This project is developed in flask. With this, the
#### project aims to create sessions using the Guess the Number application.
#### This application literally contains the code in guess.py under the flask main heading and the templates.
#### This project has four files. Among them, guess.html, lose.html, and win.html are created under the templates.
#### Now, why templates? Because they help isolating between logic and presentation.
#### That's why they are inside the application package of flask. 


############# The application is in file guess.py  #################

import os
import random
from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'

@app.route('/')
def index():
    ##### The "answer" value cannot be stored in the user session as done below
    ##### Eventhough the session is sent to the client in a cookie, that is not encrypted!
    session['answer'] = random.randint(1, 10)
    session['try_number'] = 1
    return redirect(url_for('guess'))

@app.route('/guess')
def guess():
    guess = int(request.args['guess']) if 'guess' in request.args else None
    if request.args.get('guess'):
        if guess == session['answer']:
            return render_template('win.html')
        else:
            session['try_number'] += 1
            if session['try_number'] > 3:
                return render_template('lose.html', guess=guess)
    return render_template('guess.html', try_number=session['try_number'],
                           guess=guess)

if __name__ == '__main__':
    app.run()
    
############# There are also three template files that you will need to store in a templates subdirectory. #################
############# Template number one is called guess.html #################

<html>
    <head>
        <title>Guess the number!</title>
    </head>
    <body>
        <h1>Guess the number!</h1>
        {% if try_number == 1 %}
        <p>I thought of a number from 1 to 10. Can you guess it?</p>
        {% else %}
        <p>Sorry, {{ guess }} is incorrect. Try again!</p>
        {% endif %}
        <form action="">
            Try #{{ try_number }}: <input type="text" name="guess">
            <input type="submit">
        </form>
    </body>
</html>

############# Template number two is win.html #################

<html>
    <head>
        <title>Guess the number: You win!</title>
    </head>
    <body>
        <h1>Guess the number!</h1>
        <p>Congratulations, {{ session['answer'] }} is the correct number.</p>
        <p><a href="{{ url_for('index') }}">Play again</a></p>
    </body>
</html>

############# And the last template is lose.html #################

<html>
    <head>
        <title>Guess the number: You lose!</title>
    </head>
    <body>
        <h1>Guess the number!</h1>
        <p>Sorry, {{ guess }} is incorrect. My guess was {{ session['answer'] }}.</p>
        <p><a href="{{ url_for('index') }}">Play again</a></p>
    </body>
</html>

#######################
#####  References #####
##### https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
##### https://stackoverflow.com/questions/46714773/number-guessing-game-in-flask
##### https://stackoverflow.com/questions/12967649/correct-way-of-coding-a-guess-the-number-game-in-python
##### https://github.com/helloflask/guess
##### https://www.youtube.com/watch?reload=9&v=NkguagDgrak
#######################
