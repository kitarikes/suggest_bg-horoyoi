import numpy as np
import pandas as pd
import os
from flask_app.database import db
from flask_app.models import Game, Horoyoi

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