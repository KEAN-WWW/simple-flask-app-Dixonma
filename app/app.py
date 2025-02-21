from flask import Flask, render_template
from flask import Blueprint


app = Flask(__name__)

# Default route
@app.route('/')
def home():
    return "Hello CPS3500!"

# New page route
@app.route('/new_page')
def new_page():
    return "This is a New Page!"

# Route with a username variable
@app.route('/user/<username>')
def user(username):
    return render_template("user.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
