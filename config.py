import os

# this SECRET_KEY will help with configuration item for Flask applications.
# generates tokens, I think it's good for privacy

class Config: 
    SECRET_KEY = os.environ,get('SECRET_KEY') or 'you-will-never-guess'
