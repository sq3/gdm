# -*- coding: utf-8 -*-

import flask
from flask import Flask
import gdm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def service():
    if flask.request.method == 'POST':
        migrate_from = unicode(flask.request.form['migrate-from'])
        client_id = unicode(flask.request.form['client-id'])
        client_secret = unicode(flask.request.form['client-secret'])
        migrate_to = unicode(flask.request.form['migrate-to'])

        user_data = {
                'migrate_form': migrate_from,
                'client_id': client_id,
                'client_secret': client_secret,
                'migrate_to': migrate_to
            }

        print user_data

    return flask.render_template('index.html')

def run():
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
