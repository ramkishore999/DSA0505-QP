import pandas as pd
import matplotlib.pyplot as plt

dates = ["2023-01-01","2023-01-02","2023-01-03"]
prices = [100, 102, 105]

plt.plot(dates, prices)
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Alphabet Stock Prices")
plt.show()
