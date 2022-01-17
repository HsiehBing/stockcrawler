import yfinance as yf
import matplotlib.pyplot as plt

stock = yf. download("GooG", "2020-09-15", "2020-09-25")
stock.head()

#stock.to_csv("stock.csv")
fig =plt.figure(figsize = (10,5))
plt.plot(stock["Open"], color = "red")
plt.plot(stock["Close"], '--', color = "green")
plt.ylabel("price", size= 20 )
plt.xlabel("date", size= 20)
plt.grid(True)
plt.title("Google open price", size= 25)
plt.legend(['Open', 'Close'])
plt.show()