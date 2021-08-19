from flask import Flask, render_template

app = Flask(__name__)
# app.config.from_object(Config)

@app.route("/")
def home():
    return render_template("home.html")

# # setup Blueprints
# from package.user.routes import user
# from package.main.routes import main
# app.register_blueprint(user)
# app.register_blueprint(main)