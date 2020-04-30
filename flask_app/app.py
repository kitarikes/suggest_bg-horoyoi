from flask import Flask, render_template, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from flask_app.database import init_db
from flask_app.models import Game, Horoyoi

# import numpy as np
# import pandas as pd
import random


def create_app():
  app = Flask(__name__)

  app.config.from_object('flask_app.config.Config')
  init_db(app)

  return app

app = create_app()
app.secret_key = os.environ.get("SECRET_KEY") or 'aaa'
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    game = db.session.query(Game).get(random.randint(1, 175))

    horo = db.session.query(Horoyoi).filter(Horoyoi.name == game.horoname)[0]
    # print('game = ' + str(game))
    return render_template('result.html', game=game, horo=horo)

@app.route('/test')
def test():
  return render_template('test.html')
"""
@app.route('/push_data')
def push_data():
  os.chdir(os.path.dirname(os.path.abspath(__file__)))

  games = pd.read_csv('games.csv')
  horo = pd.read_csv('horoyois.csv')

  for i in range(len(games['name'])):
    dict_ = {
      'name': games['name'][i],
      'img': games['img'][i],
      'link': games['link'][i],
      'color': games['color'][i],
      'horoname': games['horo_names'][i]
    }

    db.session.add(Game(**dict_))

  db.session.commit()

  for i in range(len(horo['name'])):
    dict_ = {
      'name': horo['name'][i],
      'img': horo['img'][i],
      'color': horo['color'][i],
    }

    db.session.add(Horoyoi(**dict_))

  db.session.commit()

  return 'success!!'
"""