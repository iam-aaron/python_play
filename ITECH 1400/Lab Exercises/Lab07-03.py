from matplotlib.pyplot import plot, show, title, xlabel, ylabel, legend, grid, ylim

msft_share_prices = [62.14, 64.65, 63.98, 65.65, 68.46, 69.84, 68.17, 72.58, 74.77, 83.18, 84.17, 85.54]
aapl_share_prices = [136.99, 143.66, 143.65, 152.76, 144.02, 148.73, 164.00, 154.12, 169.04, 171.85, 169.23, 167.43]

months = range(1,13)

title("Microsoft Vs. Apple Share Prices 2017")
xlabel("Month Number")
ylabel("Price (USD)")
plot(months, aapl_share_prices,label="AAPL", marker="o")
plot(months, msft_share_prices, label="MSFT", marker="x")

msft_min = min(msft_share_prices) # Get minimum Microsoft share price
aapl_min = min(aapl_share_prices) # Get minimum Apple share price
grid_min = min(msft_min, aapl_min) # Get minimum of both of these values
grid_min -= grid_min % 10 # Round down to nearest 10 dollars

ylim(ymin = grid_min) # Apply ymin value to grid y-axis
grid() # Display grid
legend() # Display legend
show() # Display plot