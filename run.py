# Run a test server.

from app.service import app
from config import SQLALCHEMY_DATABASE_URI
from app.db import Database

if __name__  == '__main__':
    Database(database=SQLALCHEMY_DATABASE_URI, verbose=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
