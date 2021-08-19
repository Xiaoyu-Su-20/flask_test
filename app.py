from flask import Flask, render_template
from utils.db_utils import get
from waitress import serve

app = Flask(__name__)


@app.route("/")
def home():
    df = get()
    return render_template("home.html", df=str(df))


# production
if __name__ == "__main__":
    serve(app, port=80)

# # development
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="5001", debug=True)
