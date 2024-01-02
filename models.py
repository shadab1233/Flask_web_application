from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class StudentModel(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    gender = db.Column(db.String())

    def __init__(self, name, email, gender) -> None:
        self.name = name
        self.email = email
        self.gender = gender

    def __repr__(self) -> str:
        return f'{self.name}'