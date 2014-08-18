from . import app


@app.route('/api/')
def api():
    return 'Hi, I am internal API!'
