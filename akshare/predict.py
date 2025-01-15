#!python
# predict
"""
This program predicts the next 30 day's price of share.
"""
import sys
import akshare as ak
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def predict_share_price(code):
  '''
  预测股票价格
  code: 股票代码
  '''
  if not isinstance(code, str):
    raise TypeError('Expect code type str! Got: %s' % type(code))
  # 获取股票日线行情数据
  stock_data = ak.stock_zh_a_daily(symbol=code, start_date="2020-01-01", end_date="2021-12-31")

  # 选择用于预测的特征（以日期为基础进行编码）
  stock_data["date"] = pd.to_datetime(stock_data['date'])
  stock_data["day_of_year"] = stock_data['date'].dt.dayofyear
  X = stock_data[["day_of_year"]].values
  y = stock_data["close"].values

  # 训练线性回归模型
  model = LinearRegression()
  model.fit(X, y)

  # 预测未来30天的收盘价
  future_dates = pd.date_range(start="2023-01-01", periods=30, inclusive="right")
  future_days_of_year = future_dates.dayofyear.values.reshape(-1, 1)
  future_predictions = model.predict(future_days_of_year)
  print(future_days_of_year)
  print(future_predictions)

  # 绘制股价预测图
  plt.figure(figsize=(12, 6))
  plt.plot(stock_data["date"], stock_data["close"], label="历史股价")
  plt.plot(future_dates, future_predictions, label="预测股价", linestyle="--")
  plt.xlabel("Date")
  plt.ylabel("Close Price")
  plt.title("Stock Price Prediction")
  plt.legend()
  plt.show()

if __name__ == '__main__':
  if len(sys.argv) < 2:
    raise SystemExit(f'Usage: {sys.argv[0]}' ' [code]')
  code = sys.argv[1]
  predict_share_price(code)