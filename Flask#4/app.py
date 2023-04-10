# -*- coding: UTF-8 -*-

from flask import Flask, render_template, request, redirect, url_for

from Processor import Processor

app = Flask(__name__)


class Message:

    def __init__(self, type, msg):
        self.type = type
        self.message = msg


messages = []


@app.route("/")
def home():
    return render_template('home.html', messages=messages)


@app.route("/add_answer")
def add_answer():
    return render_template('add_answer.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    userText = request.form['text']
    messages.append(Message("user", userText))
    answer = Processor().find_answer(userText)
    if answer == None:
        answer = "К сожалению, я не смог найти ответ на ваш запрос. Добавьте свой ответ на запрос и сделаете базу лучше. Внимание!!! Не оставляйте личных данных."
        messages.append(Message("chatbot", answer))
        return redirect(url_for('add_answer'))
    else:
        messages.append(Message("chatbot", answer))
        return redirect(url_for('home'))


@app.route("/add_answer2", methods=['POST'])
def add_answer2():
    userText = request.form['text']
    if (userText != ''):
        Processor().add_user_answer(userText)
        answer = "Cпасибо, за добавленный ответ. Вы сделали базу чуть лучше"
        messages.append(Message("chatbot", answer))
        return redirect(url_for('home'))
    else:
        answer = "К сожалению, ваш ответ не добавлен."
        messages.append(Message("chatbot", answer))
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
