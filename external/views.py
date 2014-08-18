from flask import make_response

from . import app


@app.route('/')
def index():
    resp = make_response()
    resp.headers['X-Accel-Redirect'] = '/api/'
    return resp
