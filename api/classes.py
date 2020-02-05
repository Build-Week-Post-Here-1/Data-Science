from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Post(DB.Model):
    '''stores potential reddit posts'''
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(1000))
    embedding = DB.Column(DB.PickleType, nullable=False)

    def __repr__(self):
        return '<Post: "{}">'.format(self.text)
   