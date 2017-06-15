
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, \
    redirect, abort, session, g, flash, Markup
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

@app.route("/v1/toonstuff", methods=["POST", "PUT"])
def toon_handle():
    """receive anything coming from the ai api as webhook"""
    request_args = {
             "args":request.args,
             #"json": request.body
           }
    request_json = request.get_json(silent=True)
    try:
        interesting_stuff = request_json["result"]
    except KeyError as e:
        interesting_stuff = {" No ": "Interesting stuff"}
    return render_template('json.html', data=interesting_stuff)
    #return render_template('json.html', data=data)

@app.route("/foobar",methods=["GET","POST"])
def wtpost(uuid= "aoeuaoeu", *args, **kwargs):
    """dummy test"""
    #content = request.get_json(silent=True)
    #print content
    return uuid
