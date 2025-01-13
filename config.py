import os

basedir = os.path.abspath(os.path.dirname(__file__))

# this SECRET_KEY will help with configuration item for Flask applications.
# generates tokens, I think it's good for privacy

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # configuration for Flask-SQLAlchemy etnension
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
