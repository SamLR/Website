from main import app

from flask import \
    render_template, redirect, request, flash, \
    url_for, abort, send_from_directory, session

from decorator import decorator
import os

def feature_flag(flag):
    def call(f, *args, **kw):
        if app.config.get(flag, False) == True:
            return f(*args, **kw)
        return abort(404)
    return decorator(call)

@app.route("/")
def main():
    return render_template('main.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/sponsors")
def sponsors():
    return render_template('sponsors.html')


@app.route("/about/company")
def company():
    return render_template('company.html')

import users, admin, tickets
