# VAR-value-at-risk

Value at Risk (VaR) is a risk management tool used to estimate the potential loss of an investment portfolio over a specified time horizon and confidence level. The basic idea behind VaR is to provide a single number that summarizes the potential downside risk of an investment portfolio. The VaR is calculated by modeling the distribution of returns for a portfolio and then determining the level of loss that is exceeded with a given degree of confidence.

For example, if the VaR of a portfolio is $10 million with a 95% confidence level, it means that there is a 5% chance that the portfolio will lose more than $10 million over the specified time horizon. VaR is widely used in the finance industry to measure and manage market risk.

There are several methods to calculate VaR, including the Variance-Covariance Method, the Historical Simulation Method, and the Monte Carlo Simulation Method. The choice of method depends on the characteristics of the portfolio and the goals of the risk management exercise.

```python
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
```

This code first loads stock price data from a CSV file into a Pandas DataFrame. The returns for the stock are calculated as the percentage change in the adjusted close price. The ```np.percentile``` function is used to calculate the VaR for a specified confidence level (in this case, 5%). The VaR is calculated as the quantile that corresponds to the specified confidence level. Finally, a histogram of the returns is plotted, and the VaR is indicated with a red vertical line.
