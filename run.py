import os
from flask import Flask
from env import OPENAI_KEY
import openai
import json

openai.api_key = OPENAI_KEY

prompt = "Write a tagline for an ice cream shop."

response = openai.Completion.create(engine="text-curie-001", prompt=prompt, max_tokens=6)

print(response)

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello, World"





# if __name__ == "__main__":
#     app.run(
#         host=os.environ.get("IP", "0.0.0.0"),
#         port=int(os.environ.get("PORT", "5000")),
#         debug=True)
