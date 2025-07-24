import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
# In my case it is, "F:\DataScience_Ai\hobby_projects\mvc_project\src"
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///simple-shop.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False