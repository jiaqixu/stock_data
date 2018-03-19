import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

yf.pdr_override() # <== that's all it takes :-)

# download dataframe
#data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")

# download Panel
#data = pdr.get_data_yahoo(["SPY", "IWM"], start="2017-01-01", end="2017-04-30")
'''
style.use('ggplot')
start=dt.datetime(2000,1,1)
end=dt.datetime(2016,12,31)

df=pdr.get_data_yahoo('TSLA',start,end)
print(df.head(100))
df.to_csv('tsla.csv')
'''
df=pd.read_csv('tsla.csv',parse_dates=True,index_col=0)
#print(df.head())
#df['Adj Close'].plot()
#plt.show()
#print(df[['Open','High']].head())
df['100ma']=df['Adj Close'].rolling(window=100,min_periods=0).mean()
#df.dropna(inplace=True)
print(df.head())

ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)

ax1.plot(df.index,df['Adj Close'])
ax2.plot(df.index,df['100ma'])
ax2.bar(df.index,df['Volume'])

plt.show()