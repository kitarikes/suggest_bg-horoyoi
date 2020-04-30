from flask_app.database import db

class Game(db.Model):
  __tablename__ = 'games'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  img = db.Column(db.String(255))
  link = db.Column(db.String(255))
  color = db.Column(db.String(255))
  horoname = db.Column(db.String(255))


class Horoyoi(db.Model):
  __tablename__ = 'horoyois'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  img = db.Column(db.String(255))
  color = db.Column(db.String(255))

