import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data for a stock price
data = pd.read_csv('stock_prices.csv')
returns = data['Adj Close'].pct_change().dropna()

# Define the confidence level
confidence_level = 0.05

# Calculate VaR using the quantile method
var = -np.percentile(returns, 100 * confidence_level)
print('Value at Risk:', var)

# Plot the returns distribution
plt.hist(returns, bins=50, density=True, label='Returns')
plt.axvline(x=var, color='red', label='VaR')
plt.legend()
plt.show()
