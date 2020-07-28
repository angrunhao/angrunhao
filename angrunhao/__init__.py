from flask import Flask

flask_app = Flask(__name__, instance_relative_config = False)
flask_app.config.from_object("config.Config")

with flask_app.app_context():
    #import routes
    from . import routes
