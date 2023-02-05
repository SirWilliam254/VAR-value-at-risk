# VAR-value-at-risk

Value at Risk (VaR) is a risk management tool used to estimate the potential loss of an investment portfolio over a specified time horizon and confidence level. The basic idea behind VaR is to provide a single number that summarizes the potential downside risk of an investment portfolio. The VaR is calculated by modeling the distribution of returns for a portfolio and then determining the level of loss that is exceeded with a given degree of confidence.

For example, if the VaR of a portfolio is $10 million with a 95% confidence level, it means that there is a 5% chance that the portfolio will lose more than $10 million over the specified time horizon. VaR is widely used in the finance industry to measure and manage market risk.

There are several methods to calculate VaR, including the Variance-Covariance Method, the Historical Simulation Method, and the Monte Carlo Simulation Method. The choice of method depends on the characteristics of the portfolio and the goals of the risk management exercise.

## Methodologies

```Historical simulation:``` This method uses historical data to simulate future returns and calculates the VaR based on the worst losses over the specified time horizon and confidence level.

```Variance-covariance method:``` This method assumes a normal distribution of returns and calculates VaR based on the portfolio's mean and standard deviation.

```Monte Carlo simulation:``` This method uses statistical simulations to generate random future returns based on historical data and calculates the VaR based on the worst losses over the specified time horizon and confidence level.

```Extreme value theory:``` This method assumes that the distribution of returns is not normal and uses statistical models to estimate the likelihood of extreme losses.

```Parametric methods:``` These methods assume a specific distribution of returns and use that distribution to estimate VaR. For example, the variance-covariance method assumes a normal distribution, while the historical simulation method does not make any assumptions about the distribution of returns.

```Modified VaR (CVaR):``` This method is a variation of VaR that takes into account the expected loss in addition to the potential loss. CVaR provides a more comprehensive estimate of portfolio risk than VaR alone.
Filtered Historical Simulation (FHS): This method combines the benefits of historical simulation and Monte Carlo simulation, by using a historical dataset to estimate the distribution of returns and then generating simulations based on that distribution.

```Exponentially Weighted Moving Average (EWMA):``` This method uses a weighted average of past returns to estimate the mean and volatility of returns, which are then used to calculate VaR.

```Implied Volatility Method:``` This method uses option prices to estimate the implied volatility of the underlying assets and then uses that information to calculate VaR.

```Kernel Density Estimation (KDE):``` This method uses a non-parametric approach to estimate the distribution of returns and calculate VaR based on that distribution.

```Backtesting:``` This method uses historical data to validate the accuracy of VaR calculations by comparing the estimated VaR with actual losses.

```Incremental VaR (IVaR):``` This method calculates VaR incrementally, by considering the impact of each trade on the portfolio's VaR.

```Hybrid methods:``` These methods combine two or more of the above methodologies to estimate VaR.

## Demonstration in Python

```python
# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import arch.data.sp500
from arch import arch_model
plt.style.use('ggplot') 


# data
data = arch.data.sp500.load()
market = data["Adj Close"]
returns = 100 * market.pct_change().dropna()


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

This code first loads stock price data from arch package to a Pandas DataFrame. The returns for the stock are calculated as the percentage change in the adjusted close price. The ```np.percentile``` function is used to calculate the VaR for a specified confidence level (in this case, 5%). The VaR is calculated as the quantile that corresponds to the specified confidence level. Finally, a histogram of the returns is plotted, and the VaR is indicated with a red vertical line.



## Parametric VAR

A parametric Value at Risk (VaR) plot is a graphical representation of the VaR of a portfolio over a specified time horizon and confidence level. By examining a parametric VaR plot, you can impute various characteristics about the risk profile of a portfolio, such as:

```Volatility:``` The width of the VaR distribution can provide information about the volatility of the portfolio. A wider distribution indicates higher volatility, while a narrower distribution indicates lower volatility.

```Skewness:``` The shape of the VaR distribution can indicate the skewness of the portfolio's returns. A symmetrical distribution indicates a balanced portfolio, while a skewed distribution indicates an imbalanced portfolio.

```Confidence level:``` The height of the VaR distribution represents the confidence level. The higher the confidence level, the higher the VaR.

```Tail risk:``` The tails of the VaR distribution can provide information about the tail risk of the portfolio. A long right tail indicates a high likelihood of large losses, while a long left tail indicates a high likelihood of large gains.

```Concentration risk:``` The concentration of the portfolio's holdings can be revealed by examining the VaR distribution. A concentration of holdings in a single stock or sector can lead to higher portfolio risk.

