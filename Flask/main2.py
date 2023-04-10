import aiml
from flask import Flask
import os

kernel = aiml.Kernel()
for filename in os.listdir("brain_chatbot (aiml_files)"):
    if filename.endswith(".aiml"):
        kernel.learn("brain_chatbot (aiml_files)/" + filename)

app = Flask(__name__)


@app.route('/')
def index():
    s = "Привет"
    return kernel.respond(s)


if __name__ == '__main__':
    app.run()
