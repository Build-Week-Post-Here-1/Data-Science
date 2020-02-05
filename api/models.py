from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Post(DB.Model)