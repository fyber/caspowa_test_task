CSRF_ENABLED = True
SECRET_KEY = 'p4$$w0rd'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static')

