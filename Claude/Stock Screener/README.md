# Stock Screener - Streamlit App

A simple stock screening application built with Streamlit that allows users to:
- Select stocks from a predefined list
- Filter stocks by P/E ratio
- View stock information including market cap and current price
- Download filtered results as CSV
- View price charts for selected stocks

## Features
- Interactive stock selection with multiselect
- P/E ratio filtering
- Real-time stock data from Yahoo Finance
- Downloadable results
- Price chart visualization

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
streamlit run "Sample Quant Trading.py"
```

## Dependencies
- yfinance
- pandas
- streamlit
- plotly

## Files
- `Sample Quant Trading.py` - Main application file
- `tickers.csv` - List of stock tickers
- `requirements.txt` - Python dependencies 