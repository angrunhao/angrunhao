from flask import Flask

def create_app():
    #Flask app with embedded Dash
    app = Flask(__name__, instance_relative_config = False)
    app.config.from_object("config.Config")

    with app.app_context():
        #import routes
        from . import routes
        #import Dash app
        from .bootstrapping_treasury_zero_curve import create_bootstrapping_treasury_zero_curve
        app = create_bootstrapping_treasury_zero_curve(app)

        return app
