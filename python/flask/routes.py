from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
   return 'Hello, World!'

   @app.route('/welcome')
def welcome():
   return render_template("welcome.html")


