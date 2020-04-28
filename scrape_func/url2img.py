import numpy as np
import pandas as pd
import os
import requests

os.chdir(os.path.dirname(os.path.abspath(__file__)))



def download_img(url, file_name, storage_path):

  r = requests.get(url, stream=True)
  if r.status_code == 200:
    try:
      with open(storage_path + file_name, 'wb') as f:
      
        f.write(r.content)
    except Exception as e:
        print(e)
        print(url, file_name)



def toImgfile (df, ishoroyoi):
  """DataFrameの画像URLをダウンロードする関数"""
  for df_idx in range(len(df)):
    url_tmp = df.iloc[df_idx, 1]
    file_name_tmp = str(df.iloc[df_idx, 0]).replace("\n", "") + ".png"
    
    if ishoroyoi:
      download_img(url_tmp, file_name_tmp, storage_path="images/horoyoi/")

    else:
      download_img(url_tmp, file_name_tmp, storage_path="images/game/")


game_data = pd.read_csv("data/game_list.csv")
horoyoi_data = pd.read_csv("data/horoyoi_list.csv")

# FIXME:ファイル名に「：」が含まれるものはエラーが発生した。 それらについては手動で保存。
toImgfile(game_data, ishoroyoi=False)
toImgfile(horoyoi_data, ishoroyoi=True)

