from flask import Flask
from package.config import Config

app = Flask(__name__)
app.config.from_object(Config)


# # setup Blueprints
from package.user.routes import user
from package.main.routes import main
app.register_blueprint(user)
app.register_blueprint(main)