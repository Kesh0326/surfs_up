from flask import Flask
# create flask app
app = Flask(__name__)

# define starting point (root)
@app.route('/')
def hello_world():
    return 'Hello World'

    