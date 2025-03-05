# Stock price prediction using ML algorithms, technical analysis & live trading

## Overview
This project applies **Machine Learning (ML)** techniques for stock price prediction, integrates **technical analysis indicators**, and supports **live trading** decisions. The system is designed to analyze historical stock market data, extract meaningful insights using technical indicators, train predictive models, and execute trades based on the predictions.

## Sample results
- succesful simulation of [live trading](https://github.com/wasikjakub/trading-bot-ml/blob/main/live-trading/simulations/live-profit-simulation.TXT) +16,7% on ETH
- confusion matrix of logistic regression model with 85 % accuracy on Apple stock.
![Screenshot 2025-03-05 at 12 52 13](https://github.com/user-attachments/assets/c5bbc212-68e1-4963-90c9-85a0631c6689)
- profitable result for 2022 ETH technical analysis BB strategy.
![Screenshot 2025-03-05 at 12 54 40](https://github.com/user-attachments/assets/5a3991e5-5f16-4b14-8aa0-b0505b894a0b)
- result for 2022 Apple stock using SMA.
![Screenshot 2025-03-05 at 12 57 41](https://github.com/user-attachments/assets/7876c3fc-d0a1-43d0-a8ca-da91904eedc0)

for further ml algorithms results: [here](https://github.com/wasikjakub/trading-bot-ml/tree/main/ml-predictions)
for further technical analysis: [here](https://github.com/wasikjakub/trading-bot-ml/blob/main/trading.ipynb)
for further live trading: [here](https://github.com/wasikjakub/trading-bot-ml/tree/main/live-trading)

## Features
- **Data Collection**: Fetches real-time and historical stock price data from **Yahoo Finance**.
- **Technical Analysis**: Computes indicators such as **Moving Averages (SMA, EMA), RSI, MACD, Bollinger Bands**,
- **Machine Learning Model**: Implements **Random Forest Classifier** & **Logistic Regression** to predict stock price movement (e.g., up/down trends).
- **Live Trading**: Connects to a Binance API to execute real trades.
- **Visualization**: Uses Matplotlib/Seaborn to generate **confusion matrices** and strategy perforamnce over the year 2022.

## Technologies Used
- **Python**
- **Pandas, NumPy** (Data processing & analysis)
- **Scikit-Learn** (ML model training & evaluation)
- **Yahoo Finance API** (Market data retrieval)
- **Matplotlib, Seaborn** (Data visualization)
- **Binance API** (Live trading)
- 
## Author
Jakub Wasik

