from werkzeug.middleware.dispatcher import DispatcherMiddleware
#from werkzeug.serving import run_simple

from angrunhao import flask_app
from angrunhao.bootstrapping_treasury_zero_curve import btzc_app

application = DispatcherMiddleware(flask_app, {
    "/btzc": btzc_app.server
})

#if __name__ == "__main__":
#    run_simple('localhost', 8050, application,
#               use_reloader=True, use_debugger=True, use_evalex=True)
