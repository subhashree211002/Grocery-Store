import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
    SOLITE_DB_DIR = os.path.join(basedir, "..\db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SOLITE_DB_DIR, "grocery_store.db")
    #print("+++++++++"+SQLALCHEMY_DATABASE_URI)
    DEBUG = True

 

class ProductionConfig(Config):
    SOLITE_DB_DIR = os.path.join(basedir, "..\db_directory")
    SOLALCHEMY_DATABASE_URI = "sqlite: ///" + os.path.join(SOLITE_DB_DIR, "proddb.db")
    DEBUG = False