# Define dictionary of stocks
stocks = {
    'BAC': 29.50,
    'JPM': 138.73,
    'F': 12.52,
    'C': 49.56,
    'SCHW': 50.77,
    'T': 542.95,
    'FRC': 13.12,
    'CCL' : 9.60,
    'CTLT': 46.32,
    'TRGP': 77.91
}

# Ask user for ticker symbol input
ticker = input("Enter a ticker symbol: ").upper()

# Search dictionary for ticker symbol
if ticker in stocks:
    print("Ticker symbol:", ticker)
    print("Stock price:", stocks[ticker])
else:
    print("Ticker symbol not found.")