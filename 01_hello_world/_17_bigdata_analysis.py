#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 获取股票数据
symbol = "600519.SS"
start_date = "2023-01-01 00:00:00"
end_date = "2024-01-01 00:00:00"

data = yf.download(symbol, start=start_date, end=end_date)
# 简单的数据分析
print(data.describe())

# 绘制股价走势图
data['Close'].plot(figsize=(10, 6), label=symbol)
plt.title(f"{symbol} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()