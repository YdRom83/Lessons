from flask import Flask
from model import UserModel

app = Flask(__name__)


@app.route('/')
def home():
    user_info = UserModel().get_user_info()
    return f"<h1> Hello {user_info['username']}! Your email is {user_info['email']}.</h1>"
