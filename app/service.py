# -*- coding: utf-8 -*-

import flask
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from models import Walker, Migration
import gdm

app = Flask(__name__)
db = SQLAlchemy(app)

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

        walker = Walker()
        walker.from_address = migrate_from
        walker.client_id = client_id
        walker.client_secret = client_secret

        db.session.add(walker)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()

        print user_data

    return flask.render_template('index.html')
