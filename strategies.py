import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def SMAxtoy(symbol, x, y, detail):
    df = yf.download(symbol, start='2022-09-01')

    df['MA20'] = df['Adj Close'].rolling(x).mean()
    df['MA50'] = df['Adj Close'].rolling(y).mean()
    df=df.dropna()
    df = df[['Adj Close', 'MA20', 'MA50']]

    Buy = []
    Sell = []

    for i in range(len(df)):
        # BUY If SMA20 is above SMA50 today, and wasn't yesterday(cross)
        if df.MA20.iloc[i] > df.MA50.iloc[i] and df.MA20.iloc[i-1] < df.MA50.iloc[i-1]: 
            Buy.append(i)
        elif df.MA20.iloc[i] < df.MA50.iloc[i] and df.MA20.iloc[i-1] > df.MA50.iloc[i-1]:
            Sell.append(i)  

    plt.figure(figsize=(20, 10)) # Plot the dataframe
    plt.plot(df['Adj Close'], label='Cena', c='blue', alpha=0.5)
    plt.plot(df['MA20'], label='MA'+str(x), c='k', alpha=0.9)
    plt.plot(df['MA50'], label='MA'+str(y), c='magenta', alpha=0.9)
    plt.scatter(df.iloc[Buy].index, df.iloc[Buy]['Adj Close'], marker='o', color='g', s=80)
    plt.scatter(df.iloc[Sell].index, df.iloc[Sell]['Adj Close'], marker='o', color='r', s=80)

    for index in Buy: # Add prices
        x = df.iloc[index].name
        y = df.iloc[index]['Adj Close']
        plt.scatter(x, y, marker='o', color='g', s=80)
        plt.text(x, y+detail, f'{y:.2f}', color='g', fontsize=9, va='bottom', ha='right')

    for index in Sell:
        x = df.iloc[index].name
        y = df.iloc[index]['Adj Close']
        plt.scatter(x, y, marker='o', color='r', s=80)
        plt.text(x, y-detail, f'{y:.2f}', color='r', fontsize=9, va='bottom', ha='right')

    plt.title(symbol)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xlabel('Data')
    plt.ylabel('Cena [$]')
    plt.gca().set_facecolor('#e0f0ff') 
    plt.grid(color='white')
    plt.show()

def BoillingBands(symbol, detail):
    df = yf.download(symbol, start='2022-09-01')
    df['SMA'] = df.Close.rolling(window=20).mean() # SMA calculation
    df['stddev'] = df.Close.rolling(window=20).std()
    df['Upper'] = df.SMA + 2*df.stddev
    df['Lower'] = df.SMA - 2*df.stddev
    df['Buy_signal'] = np.where(df.Lower > df.Close, True, False)
    df['Sell_signal'] = np.where(df.Upper < df.Close, True, False)
    df = df.dropna()

    buys = [] 
    sells = []
    open_pos = False
    for i in range(len(df)):
        if df. Lower[i] > df.Close[i]: 
            if open_pos == False:
                buys.append(i)
                open_pos = True
        elif df.Upper[i] < df.Close[i]:
            if open_pos:
                sells.append(i)
                open_pos = False

    plt.figure(figsize=(20, 10)) # Plot the dataframe
    plt.gca().set_facecolor('#e0f0ff') 
    plt.grid(color='white')
    plt.plot(df[['Close']], label='Cena', color='b', alpha=0.5)
    plt.plot(df[['SMA']], label='MA20', color='orange')
    plt.plot(df[['Upper']], label='Górna granica', color='green')
    plt.plot(df[['Lower']], label='Dolna granica', color='red')
    plt.scatter(df.iloc[buys].index, df.iloc[buys].Close, marker='o', color='g')
    plt.scatter(df.iloc[sells].index, df.iloc[sells].Close, marker='o', color='r')
    plt.fill_between(df.index, df.Upper, df.Lower, color='blue', alpha=0.1)

    for index in buys: # Add prices
        x = df.iloc[index].name
        y = df.iloc[index]['Adj Close']
        plt.scatter(x, y, marker='o', color='g', s=80)
        plt.text(x, y-detail, f'{y:.2f}', color='g', fontsize=9, va='bottom', ha='right')

    for index in sells:
        x = df.iloc[index].name
        y = df.iloc[index]['Adj Close']
        plt.scatter(x, y, marker='o', color='r', s=80)
        plt.text(x, y+detail, f'{y:.2f}', color='r', fontsize=9, va='bottom', ha='right')

    plt.xlabel('Data')
    plt.ylabel('Cena [$]')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.title(symbol)
    plt.gca().set_facecolor('#e0f0ff') 
    plt.grid(color='white')
    plt.show()

def RSI(symbol, detail):
    df = yf.download(symbol, start='2022-03-01')
    df['MA200'] = df['Adj Close'].rolling(window=200).mean()
    df['price change'] = df['Adj Close'].pct_change()
    df['Upmove'] = df['price change'].apply(lambda x: x if x > 0 else 0)
    df['Downmove'] = df['price change'].apply(lambda x: abs(x) if x < 0 else 0)
    df['avg Up'] = df['Upmove'].ewm(span=19).mean()
    df['avg Down'] = df['Downmove'].ewm(span=19).mean()
    df = df.dropna()
    df['RS'] = df['avg Up']/df['avg Down']
    df['RSI'] = df['RS'].apply(lambda x: 100-(100/(x+1)))
    df.loc[(df['Adj Close'] > df['MA200']) & (df['RSI'] < 30), 'Buy'] = 'Yes'
    df.loc[(df['Adj Close'] < df['MA200']) | (df['RSI'] > 30), 'Buy'] = 'No'

    buys = []
    sells = []
    in_position = False  # Track the last signal

    for i in range(len(df)):
        if not in_position:
            if df['Adj Close'].iloc[i] > df['MA200'].iloc[i] and df['RSI'].iloc[i] < 30:
                buys.append(df.index[i])
                in_position = True
        else:
            if df['RSI'].iloc[i] > 40:
                sells.append(df.index[i])
                in_position = False

    plt.figure(figsize=(20, 10))
    plt.scatter(df.loc[buys].index, df.loc[buys]['Adj Close'], c='g')
    plt.scatter(df.loc[sells].index, df.loc[sells]['Adj Close'], c='r')
    plt.plot(df['Adj Close'], label='Cena', alpha=0.7)

    for buy in buys:
        plt.scatter(buy, df.loc[buy, 'Adj Close'], c='g', label='Buy Signal' if buy == buys[0] else "", marker='^')
        plt.annotate(f"{df.loc[buy, 'Adj Close']:.2f}", 
                     (buy, df.loc[buy, 'Adj Close']),
                     textcoords="offset points", 
                     xytext=(0,detail), 
                     ha='center', 
                     color='green')

    for sell in sells:
        plt.scatter(sell, df.loc[sell, 'Adj Close'], c='r', label='Sell Signal' if sell == sells[0] else "", marker='v')
        plt.annotate(f"{df.loc[sell, 'Adj Close']:.2f}", 
                     (sell, df.loc[sell, 'Adj Close']),
                     textcoords="offset points", 
                     xytext=(0,-detail), 
                     ha='center', 
                     color='red')

    plt.title(symbol)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xlabel('Data')
    plt.ylabel('Cena [$]')
    plt.gca().set_facecolor('#e0f0ff') 
    plt.grid(color='white')
    plt.show()