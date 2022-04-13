import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings


warnings.filterwarnings('ignore')

# Excelファイルの読み込み
# ファイルはこのnotebookと同じディレクトリに配置
df = pd.read_excel('datasets/dataset.xlsx')

# DataFrameから最高気温の列だけを取り出す
# locメソッドで列を指定できます
df.loc[:, ['MAX_TEMP']].head()

# 最高気温のデータをarrayに変換
X = np.array(df.loc[:, ['MAX_TEMP']])


# 売上個数のデータをarray型に変換
y = np.array(df.loc[:, ['N_COFFEE']])


# ==================================
# データの観察

# 散布図を出力
# 直線的な関係が確認できる

# 散布図を表示
plt.scatter(X, y)
# タイトルを表示
plt.title('n_coffee vs max_temp')
# x軸のラベルを表示
plt.xlabel('max_temp')
# y軸のラベルを表示
plt.ylabel('n_coffee')
# 指定した内容でグラフを出力
plt.show()
