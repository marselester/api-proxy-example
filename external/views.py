from flask import make_response

from . import app


@app.route('/')
def index():
    resp = make_response()
    resp.headers['X-Accel-Redirect'] = '/api/'
    resp.headers['FIZZ'] = 'fizz'
    resp.headers['BAZZ'] = 'bazz'
    return resp
