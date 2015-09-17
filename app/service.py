# -*- coding: utf-8 -*-

import flask
from flask import Flask
import gdm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def service(name=None):
    user_data = {}
    if flask.request.method == 'POST':
        user_data.update(
                migrate_from=unicode(
                    flask.request.form['migrate-from']
                    )
                )
        
        user_data.update(
                client_id=unicode(
                     flask.request.form['client-id'])
                )
        
        user_data.update(
                client_secret=unicode(
                    flask.request.form['client-secrte']
                    )
                )
        
        user_data.update(
                migrate_to=unicode(
                    flask.requst.form['migrate-to']
                    )
                )

        return flask.render_template('index.html')

def run():
    app.run(host='0.0.0.0', port=8080, debug=True)
