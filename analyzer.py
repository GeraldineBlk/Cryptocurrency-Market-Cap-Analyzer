import requests
import pandas as pd
import matplotlib.pyplot as plt

class MarketCapAnalyzer:
    def __init__(self, api_url):
        self.api_url = api_url
        self.data = None

    def fetch_market_cap_data(self):
        # Fetch market capitalization data from the cryptocurrency API
        response = requests.get(self.api_url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Error fetching market cap data from the API.")

    def analyze_market_cap_data(self):
        # Convert data to pandas DataFrame for analysis
        df = pd.DataFrame(self.data)

        # Perform data manipulation and analysis using pandas

        # Calculate market share:
        df['market_share'] = df['market_cap'] / df['total_market_cap'] * 100

        # Sort by market cap in descending order
        df = df.sort_values('market_cap', ascending=False)

        # Generate visualizations
        self.generate_top_n_chart(df, 10)
        self.generate_market_share_pie_chart(df)

    def generate_top_n_chart(self, df, n):
        # Generate a bar chart showing the top N cryptocurrencies by market cap:
        top_n_df = df.head(n)
        labels = top_n_df['symbol']
        market_caps = top_n_df['market_cap']

        plt.figure(figsize=(12, 6))
        plt.bar(labels, market_caps)
        plt.title(f"Top {n} Cryptocurrencies by Market Cap")
        plt.xlabel("Cryptocurrency Symbol")
        plt.ylabel("Market Cap (USD)")
        plt.xticks(rotation=45)
        plt.show()

    def generate_market_share_pie_chart(self, df):
        # Generate a pie chart showing the market share of cryptocurrencies
        labels = df['symbol']
        market_shares = df['market_share']

        plt.figure(figsize=(8, 8))
        plt.pie(market_shares, labels=labels, autopct='%1.1f%%')
        plt.title("Cryptocurrency Market Share")
        plt.show()

# Example usage:

# Define API URL
api_url = "https://api.example.com/market-cap"

# Create an instance of MarketCapAnalyzer
analyzer = MarketCapAnalyzer(api_url)

# Fetch market capitalization data
analyzer.fetch_market_cap_data()

# Analyze and visualize market cap data
analyzer.analyze_market_cap_data()
