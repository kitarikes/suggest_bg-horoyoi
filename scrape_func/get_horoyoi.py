from bs4 import BeautifulSoup
import urllib
import requests
import numpy as np
import pandas as pd

def get_horoyoi_info():
  """ほろよい公式サイトからほろよいの種類と画像を取得する関数です。 dict型を返します。"""
  
  dict_ = {"name": [],
           "img": []
           }

  url = "https://www.suntory.co.jp/rtd/horoyoi/"
  request = urllib.request.Request(url)
  html = urllib.request.urlopen(request)
  r = requests.get(url)
  soup = BeautifulSoup(html, 'html.parser')

  horoyoi_img_tags = soup.select('div[class="products"] div[class="thumb"] img')

  for tag in horoyoi_img_tags:
    name = tag.attrs["alt"]
    img = url + tag.attrs["src"]

    dict_["name"].append(name)
    dict_["img"].append(img)

  return dict_

data = get_horoyoi_info()

df = pd.DataFrame(data)

df.to_csv("horoyoi_list.csv", index=False)



  




