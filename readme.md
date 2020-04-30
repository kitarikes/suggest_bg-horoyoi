<h2>🎈about</h2>
        <p>ボードゲームとほろよいを１つずつ勧めてくれるwebアプリです。本当に暇なときに使ってみてください！<br>※このwebアプリは全てpythonで作成しました。<br>（バックエンド: Flask, インフラ: heroku, webサイトからのデータ収集: beautifulsoap, 画像分析: numpy, pandas, scikitlearnなど）</p>
        <h2>🎲ボードゲーム</h2>
        <p>全てのボードゲームは<a href="https://boardgamearena.com/">ボードゲームアリーナ</a>という、オンラインでかつ無料で登録できるサイトから取得しました。なので、お家で友人とお酒を飲みながらプレイすることが可能です。自粛にピッタリですね。</p>
        <h2>🍸ほろよい</h2>
        <p>ボードゲームの画像、ほろよいの画像のそれぞれから代表色を抽出し、ボードゲーム毎に、r,g,b値の差の絶対値が最も少ないようなほろよいの味を登録してあります。<br>具体的な手法としては、まず画像を画素ごとにr,g,b値に変換し、k-平均法という手法を使い５色に分類します。その後、選ばれた５色の中で最も、サンプル数が多い色を１つ選び、それを代表色としました。
          詳しくは<a href="https://github.com/kitarikes/suggest_bg-horoyoi/blob/master/analyze_image/example_get_main_color.ipynb">こちら</a>

## 参考
- [Pythonで画像からメインカラーを抽出する](https://qiita.com/simonritchie/items/396112fb8a10702a3644)
- [Python OpenCV の cv2.imread 及び cv2.imwrite で日本語を含むファイルパスを取り扱う際の問題への対処について](https://qiita.com/SKYS/items/cbde3775e2143cad7455)
- [OpenCV - k 平均法 (k-means) を使い、画像の代表色を取得する方法](https://www.pynote.info/entry/opencv-kmeans#k-%E5%B9%B3%E5%9D%87%E6%B3%95%E3%81%A7%E4%BB%A3%E8%A1%A8%E8%89%B2%E3%82%92%E8%A8%88%E7%AE%97%E3%81%99%E3%82%8B)
- [【Scikit-learn】K-means法でクラスタ毎のサンプル数を表示](https://algorithm.joho.info/machine-learning/python-scikit-learn-clustering-kmean-sample-number/)

## 改善点

![image](https://user-images.githubusercontent.com/52794486/80694500-8deb4d80-8b0f-11ea-95d5-a7384b9ed29c.png)

- コーラサワーが圧倒的に多すぎる点

  