from flask import Blueprint, render_template

from package.utils.db_utils import get

main = Blueprint("main", __name__)


@main.route("/")
def home():
    df = get()
    return render_template("home.html", df=str(df))