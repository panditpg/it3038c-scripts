##### Project 3: "Guess The Number" #####

#### This project is developed in flask. With this, the
#### project aims to create sessions using the Guess the Number application.
#### This application literally contains the code in guess.py under the flask main heading and the templates.
#### This project has four files. Among them, guess.html, lose.html, and win.html are created under the templates.
#### Now, why templates? Because they help isolating between logic and presentation.
#### That's why they are inside the application package of flask.So, the first thing is first. To run the code first Window,then VSCode, then go to guess.py. In the terminal (window console), follow: 
py -3 -m venv C:\venv\flask
C:\venv\flask\Scripts\Activate.ps1
pip install flask
cd .\flask
Then finally type: python guess.py
#### Then The Guess The Number application presented below is accessed throguh the browser with localhost:5000/guess. 
#### If you type a number, it's gonna display sorry 1 (the number) is incorrect. Please try it again! Until you enter the correct number, or after third attempt it's gonna say the answer, or if your number is correct, it's gonna say Congratulations! 8 (depends) is the correct answer. It's like a fun game, right!
#### More importantly, it's gonna give the idea of how to decode flask user session. For this, on the browser after you submit the the number, in a blank area, right click and follow the inspect element. Then click on the icon as you prefer or need to get the response or output from such as Inspector, Console, Debugger, Network, {} style editor, performance, memory, storage accessibility, and application functionalities. I decided to continue working on flask because it combines python and html and displays through the localhost in the browser. It also touches and introduces previous labs and projects I've learned and worked so far. For example, server, webscrapping, web-browsing, listening or calling through a server with ports associated to localhost on the browser by connecting codes between templates and index and htmls. Last but not the least, this project would give someone an idea of understanding not to have misconception of as flask user session is entirely secured. Don't be in trap literally! Because one can decode a flask user session without requiring the application's secret key used for encoding it (like the one given in the guess.py). Meaning, don't ever store secrets in a flask session cookie.


############# The application is in file guess.py  #################

import os
import random
from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'

@app.route('/')
def index():
    ##### The "answer" value cannot be stored in the user session like it is shown as follows.
    ##### Eventhough the session is sent to the client in a cookie, it is not encrypted!
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
        <title>Guess The Number!</title>
    </head>
    <body>
        <h1>Guess The Number!</h1>
        {% if try_number == 1 %}
        <p>I've thought of a number between 1 and 10. Could you please guess it?</p>
        {% else %}
        <p>Sorry, {{ guess }} is incorrect. Please try it again!</p>
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
        <title>Guess The Number: You win!</title>
    </head>
    <body>
        <h1>Guess The Number!</h1>
        <p>Congratulations! {{ session['answer'] }} is the correct number.</p>
        <p><a href="{{ url_for('index') }}">Would You Like To Play It Again?</a></p>
    </body>
</html>


############# And the last template is lose.html #################

<html>
    <head>
        <title>Guess The Number: You lose!</title>
    </head>
    <body>
        <h1>Guess The Number!</h1>
        <p>Sorry, {{ guess }} is incorrect. Actually, my guess was {{ session['answer'] }}.</p>
        <p><a href="{{ url_for('index') }}">Please play it again</a></p>
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
