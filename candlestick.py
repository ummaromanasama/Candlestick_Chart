#Importing Libraries
import requests
import pandas as pd
import datetime
from bokeh.plotting import figure, show, output_file
from math import pi

#Request ticker symbol
API_KEY = 'DJDC70DZV667MOEM'
symbol = input('Enter ticker symbol: ')
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + symbol + '&apikey=' + API_KEY)
print(r.status_code)
result = r.json()
dataForAllDays = result['Time Series (Daily)']

#convert to dataframe
df = pd.DataFrame.from_dict(dataForAllDays, orient='index') 
df = df.reset_index()

#rename columns
df = df.rename(index=str, columns={"index": "date", "1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close","5. volume":"volume"})

#Changing to datetime
df['date'] = pd.to_datetime(df['date'])

#Sort according to date
df = df.sort_values(by=['date'])

#Changing the datatype 
df.open = df.open.astype(float)
df.close = df.close.astype(float)
df.high = df.high.astype(float)
df.low = df.low.astype(float)
df.volume = df.volume.astype(int)

#check the data
df.head()

#Check the datatype
df.info()
inc = df.close > df.open
dec = df.open > df.close
w = 12*60*60*1000 # half day in ms
TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
title = symbol + ' Chart'
p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = title)
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3
p.segment(df.date, df.high, df.date, df.low, color="black")
p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")

#Store as a HTML file
output_file("stock_information.html", title="candlestick.py")

# Display in browser
show(p)
