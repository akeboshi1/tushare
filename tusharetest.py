import tushare as ts
df = ts.get_tick_data('600036',date='2023-8-1')
print(df)
# df.head(10)