from flask import Flask, render_template, request
import openai #dunno doesnt work rn i think
import os
from dotenv import load_dotenv

#https://platform.openai.com/account/api-keys

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

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
    #get the message input from the user
    user_input = request.form["message"]


    # this stuff change to be specific to what i want out of my chatbot 
    # no real chatting just single prompt and response

    #use openai api to generate response
    prompt = f"User : {user_input}\nChatbot: "
    chat_history = []
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        stop=["\nUser: ", "\nChatbot: "]
    )

    # extract response text from the openai API result
    bot_response = response.choices[0].text.strip()

    # add user input and bot response to chat history
    chat_history.append(f"User: {user_input}\nChatbot: {bot_response}")

    # render chatbot template w response text
    return render_template(
        "chatbot.html",
        user_input=user_input,
        bot_response=bot_response
    )

# start the flask app
if __name__=="__main__":
    app.run(debug=True)

