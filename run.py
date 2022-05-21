import os
import json
from flask import Flask, render_template, request
import openai
from env import OPENAI_KEY

openai.api_key = OPENAI_KEY

app = Flask(__name__)

'''
open AI model for detailed product description,
iterates through returned object and returns response
'''


def product_description(query):
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=f"Generate a detailed product description for: {query}",
        temperature=0.6,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = "I don't have an answer for you this time"
    else:
        answer = "I don't have an answer for you this time"

    return answer

'''
listens for form input on index.html and returns AI response
'''


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form['productDescription']
        ai_answer = product_description(query)
        prompt = f'AI suggestion for {query}:'
        history = [prompt, ai_answer]

    return render_template('index.html', **locals())


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
