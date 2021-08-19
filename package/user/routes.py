from flask import Blueprint, render_template

from package.user.forms import LoginForm

user = Blueprint("user", __name__)

@user.route("/task")
def task():
    return "task"

@user.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template("home.html")
    return render_template("main/login.html", title="Login", form=form)
