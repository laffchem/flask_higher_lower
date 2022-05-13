from flask import Flask
import random

app = Flask(__name__)

num = random.randint(0, 9)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_blue(function):
    def wrapper_function(*args):
        function(args)
        if function(args) < num:
            return "<h1 style='color:blue'>" + function() + "</h1>"
    return wrapper_function

def make_red(function):
    def wrapper_function(*args):
        function(args)
        if function(args) > num:
            return "<h1 style='color:red'>" + function() + "</h1>"
    return wrapper_function

def make_green(function):
    def wrapper_function(*args):
        function(args)
        if function(args) == num:
            return "<h1 style='color:green'>" + function() + "</h1>"
    return wrapper_function

def header(function):
    def wrapper_function():
        return "<h1>" + function() + "</h1>"
    return wrapper_function

@app.route('/')
@header
def index():
    return 'Guess a number between 0 and 10. \
        <br> \
        <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:guess>')
def user_num(guess):
    if guess < num:
        return '<h1 style=color:blue>Too Low! Try again.</h1> \
            <br> \
                <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > num:
        return '<h1 style=color:red>Too High! Try again.</h1> \
            <br> \
                <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style=color:green>You found me!</h1> \
            <br> \
                <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)

# ## Python Decoartor Function

# def decorator_function(function):
#     def wrapper_function():
#         #Do something before
#         function()
#         #Do something after
#     return wrapper_function
