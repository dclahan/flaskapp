from flask import Flask, render_template, request
import openai #dunno doesnt work rn i think
import os
from dotenv import load_dotenv

#https://platform.openai.com/account/api-keys

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

# print(openai.api_key)

# Set up Flask app

# 2 endpts one for chat and then one to put query into openai

app = Flask(__name__)

# Define home page route
# user enters here

@app.route("/")
def home():
    return render_template("index.html")

# define chatbot route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    pass