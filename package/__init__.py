from flask import Flask, render_template
from package.config import Config
from package.utils.db_utils import get

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    df = get()
    return render_template("home.html", df=str(df))