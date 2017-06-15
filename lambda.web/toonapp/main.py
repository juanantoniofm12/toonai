
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, \
    redirect, abort, session, g, flash, Markup, jsonify
import json
from toonapp import app


@app.route('/')
def index():
    return "You are at the homepage!"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# CSRF protection needs a little bit of reading and adjustment. lets go for now.
#@csrf.error_handler
#def csrf_error(reason):
#    return render_template('csrf_error.html', reason=reason)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']


@app.route('/login', methods=['GET', 'POST'])
def login_handler():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_user_in(request.form['username'])
        else:
            error = "Invalid username/password!"
    return render_template('login.html', error=error)


@app.route("/v1/mirror", methods=["POST", "PUT"])
def mirror_handle():
    """receive anything coming from the ai api as webhook"""
    request_json = request.get_json()
    try:
        interesting_stuff = request_json
    except KeyError as e:
        interesting_stuff = {" No ": "Interesting stuff"}
    except TypeError as e:
        interesting_stuff = {" No ": "stuff at all"}
    return jsonify(interesting_stuff)


@app.route("/v1/toonstuff", methods=["POST"])
def toon_handler():
    """
            Trying to do some serious stuff.
            The result bit:
            {
          "action": "greetings",
          "actionIncomplete": false,
          "contexts": [],
          "fulfillment": {
            "messages": [
              {
                "speech": "Hi Ana! Nice to meet you!",
                "type": 0
              }
            ],
            "speech": "Hi Ana! Nice to meet you!"
          },
          "metadata": {
            "intentId": "9f41ef7c-82fa-42a7-9a30-49a93e2c14d0",
            "intentName": "greetings",
            "webhookForSlotFillingUsed": "false",
            "webhookUsed": "true"
          },
          "parameters": {
            "city": "Rome",
            "name": "Ana"
          },
          "resolvedQuery": "my name is Ana and I live in Rome",
          "score": 1.0,
          "source": "agent",
          "speech": ""
        }
    """
    request_json = request.get_json()
    """
    take some interesting stuff like the intent name.
    Then put it in a log for now and sew how it does in AWS
    """
    try:
        c_parameters = request_json["result"]["parameters"]
        c_action = request_json["result"]["action"]
        c_headers = dict(request.headers)
        interesting_stuff = {
            "parameters": c_parameters,
            "action":c_action,
            "headers": c_headers}

    except ValueError as e:
        pass

    print interesting_stuff

    return jsonify(interesting_stuff)


@app.route("/foobar",methods=["GET","POST"])
def wtpost(uuid= "aoeuaoeu", *args, **kwargs):
    """dummy test"""
    #content = request.get_json(silent=True)
    #print content
    return uuid
