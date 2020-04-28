from bs4 import BeautifulSoup
import urllib
import requests
import numpy as np
import pandas as pd


def get_game_info():
  """BGAからゲームの種類を取得する関数です。 dict型を返します。"""

  dict_ = {"name": [], 
           "img": [],
           "link": []
           }
  url = "https://ja.boardgamearena.com/gamelist?section=all"

  request = urllib.request.Request(url)
  html = urllib.request.urlopen(request)
  r = requests.get(url)
  soup = BeautifulSoup(html, 'html.parser')
  game_list = soup.select("#gamelist_itemrow_inner_all div[class='gamelist_item']")

  for game in game_list:
    name = str(game.select("a div[class='gameitem_baseline gamename']")[0].text).replace(" ", "")
    img = game.select("a div[class='game_box_image_wrap'] img")[0].attrs["bga_lazyload"]
    link = "https://ja.boardgamearena.com" + game.select("a")[0].attrs["href"]

    dict_["name"].append(name)
    dict_["img"].append(img)
    dict_["link"].append(link)

  return dict_


data = get_game_info()

df = pd.DataFrame(data)

df.to_csv("game_list.csv", index=False)


