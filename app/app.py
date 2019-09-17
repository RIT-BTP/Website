from flask import Flask, request, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import base64
import datetime

app = Flask(__name__)

app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from models import tmpUsers, Events
from forms import RegistrationForm, LoginForm, EventForm
from functions import user_check


@app.route("/")
def root():
    return redirect(url_for("home"))


@app.route("/login", methods=["GET", "POST"])
def login():
    failed = request.args.get("failed")
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        if not user_check(form.username.data):
            return redirect(url_for("login", failed=True))
        # check
        flash("Logged In")
        return redirect(url_for("home"))
    return render_template("unauth/login/login.html", form=form, failed_login=failed)


@app.route("/register", methods=["GET", "POST"])
def register():
    failed = request.args.get("failed")
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        if user_check(form.username.data):
            return redirect(url_for("register", failed=True))
        tmpUsers.insert(name=form.username.data)
        flash("Thanks for registering")
        return redirect(url_for("registeredlist"))
    return render_template(
        "unauth/register/register.html", form=form, failed_registration=failed
    )


@app.route("/registeredlist", methods=["GET"])
def registeredlist():
    users = tmpUsers.get()
    users = [user.name for user in users]
    print(users)
    return render_template("unauth/register/list.html", users=users)


@app.route("/home", methods=["GET"])
def home():
    all_events = Events.get()
    curr_events = []
    for event in all_events:
        if event.date >= datetime.date.today():
            curr_events.append(event)
    curr_events = sorted(curr_events, key=lambda x: x.date)
    return render_template("auth/home/home.html", events=curr_events)


@app.route('/create event', methods=["GET", "POST"])
def createEvent():
    form = EventForm(request.form)
    
    if request.method == "POST" and form.validate():
        Events.insert(name=form.name.data, icon=base64.b64encode(request.files[form.icon.name].read()), date=form.date.data, description=form.description.data)
        return redirect(url_for("home"))
    return render_template(
        "auth/events/create.html", form=form
    )
