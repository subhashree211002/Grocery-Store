import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
#from flask_migrate import Migrate

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
    
    """migrate = Migrate(app, db)  # Initialize Flask-Migrate

    # Import all the models so they are loaded before creating tables
    from application.models import Category, Product, Users, Managers, Orders_Desc, Order_Details
    
    with app.app_context():
        db.create_all()"""
        
    app.app_context().push()
    return app

 

app = create_app()

# Import all the controllers so they are loaded
from application.controllers import *
if __name__ == "__main__":
    #Run the flask app
    app.run(host='0.0.0.0', port=8080)