
from bottle import default_app, route, post, get, template

@route('/keyfind')
def keyshome():
    return template("keyshome.html")

@post('/keysresult')
def keysfound():
    return template("keysresult.html")

application = default_app()

