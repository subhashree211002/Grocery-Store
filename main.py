import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db

app = None


def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv("ENV', “development") == "production":
        raise Exception("Currently no production config is setup.")
    else:
        print ("_____staring Local Development______") 
        app.config.from_object(LocalDevelopmentConfig)
        print(app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)
    app.app_context().push()
    return app

 

app = create_app()

# Import all the controllers so they are loaded
from application.controllers import *
if __name__ == "__main__":
    #Run the flask app
    app.run(host='0.0.0.0', port=8080)