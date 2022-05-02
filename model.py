from flask import Flask, json,jsonify,request
from flask_sqlalchemy import SQLAlchemy
#from marshmallow import Schema,fields

from flask_migrate import Migrate


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://postgres:sena@localhost/quizz_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


db=SQLAlchemy(app)
migrate = Migrate(app, db)

class Quizz(db.Model):
    __tablename__ = 'quizz'

    id = db.Column(db.Integer(),primary_key=True)
    question_id = db.Column(db.Integer())
    answer = db.Column(db.String(100),nullable=False)
    question = db.Column(db.Text(),nullable=False)
    date = db.Column(db.String(100),nullable=False)

    def __init__(self, question_id, answer, question, date):
        self.question_id = question_id
        self.answer = answer
        self.question = question
        self.date = date


    def __repr__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)