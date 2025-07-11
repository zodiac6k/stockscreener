import yfinance as yf
import pandas as pd

# Add all stocks from your screenshots here
stocks = [
    {"name": "PI INDUSTRIES LIMITED", "isin": "INE603J01030", "quantity": 54, "sector": "Agrochemicals"},
    {"name": "RELIANCE INDUSTRIES LIMITED", "isin": "INE002A01018", "quantity": 204, "sector": "Conglomerate"},
    {"name": "RITES LIMITED", "isin": "INE320J01015", "quantity": 110, "sector": "Engineering"},
    {"name": "SANGHVI MOVERS LIMITED", "isin": "INE989A01032", "quantity": 230, "sector": "Logistics"},
    {"name": "STATE BANK OF INDIA", "isin": "INE062A01020", "quantity": 20, "sector": "Banking"},
    {"name": "SBI CARDS & PAYMENT SERVICES LIMITED", "isin": "INE018E01016", "quantity": 19, "sector": "Financial Services"},
    {"name": "TATA COMMUNICATIONS LIMITED", "isin": "INE151A01013", "quantity": 25, "sector": "Telecom"},
    {"name": "TATA CHEMICALS LIMITED", "isin": "INE092A01019", "quantity": 25, "sector": "Chemicals"},
    {"name": "AARTI INDUSTRIES LIMITED", "isin": "INE769A01020", "quantity": 40, "sector": "Chemicals"},
    {"name": "BRITANNIA INDUSTRIES LIMITED", "isin": "INE216A01030", "quantity": 50, "sector": "FMCG"},
    {"name": "CENTRAL DEPOSITORY SERVICES (INDIA) LIMITED", "isin": "INE736A01011", "quantity": 160, "sector": "Financial Services"},
    {"name": "COMPUTER AGE MANAGEMENT SERVICES LIMITED", "isin": "INE596I01012", "quantity": 62, "sector": "Financial Services"},
    {"name": "GLOBAL HEALTH LIMITED", "isin": "INE474O01031", "quantity": 44, "sector": "Healthcare"},
    {"name": "GODREJ CONSUMER PRODUCTS LIMITED", "isin": "INE102D01028", "quantity": 142, "sector": "FMCG"},
    {"name": "HINDUSTAN COPPER LIMITED", "isin": "INE531E01026", "quantity": 250, "sector": "Metals"},
    {"name": "HINDUSTAN UNILEVER LIMITED", "isin": "INE030A01027", "quantity": 42, "sector": "FMCG"},
    {"name": "INDIAN RAILWAY CATERING AND TOURISM CORPORATION LIMITED", "isin": "INE335Y01020", "quantity": 200, "sector": "Railways"},
    {"name": "KFIN TECHNOLOGIES LIMITED", "isin": "INE138Y01010", "quantity": 2, "sector": "Financial Services"},
    {"name": "LIFE INSURANCE CORPORATION OF INDIA", "isin": "INE0J1Y01017", "quantity": 44, "sector": "Insurance"},
    # Add more as needed
]

# Map ISIN to Yahoo ticker (fill in all tickers)
isin_to_ticker = {
    "INE603J01030": "PIIND.NS",
    "INE002A01018": "RELIANCE.NS",
    "INE320J01015": "RITES.NS",
    "INE989A01032": "SANGHVIMOV.NS",
    "INE062A01020": "SBIN.NS",
    "INE018E01016": "SBICARD.NS",
    "INE151A01013": "TATACOMM.NS",
    "INE092A01019": "TATACHEM.NS",
    "INE769A01020": "AARTIIND.NS",
    "INE216A01030": "BRITANNIA.NS",
    "INE736A01011": "CDSL.NS",
    "INE596I01012": "CAMS.NS",
    "INE474O01031": "MEDANTA.NS",
    "INE102D01028": "GODREJCP.NS",
    "INE531E01026": "HINDCOPPER.NS",
    "INE030A01027": "HINDUNILVR.NS",
    "INE335Y01020": "IRCTC.NS",
    "INE138Y01010": "KFINTECH.NS",
    "INE0J1Y01017": "LICI.NS",
    # Add more mappings as needed
}

def get_recommendation(pe):
    if pe is None:
        return "No Data"
    if pe < 25:
        return "Buy"
    elif pe <= 50:
        return "Hold"
    else:
        return "Sell"

results = []
for stock in stocks:
    ticker = isin_to_ticker.get(stock["isin"])
    if ticker:
        try:
            yf_stock = yf.Ticker(ticker)
            info = yf_stock.info
            price = info.get("currentPrice") or info.get("regularMarketPrice")
            pe = info.get("trailingPE")
        except Exception as e:
            price = pe = None
    else:
        price = pe = None
    value = stock["quantity"] * price if price is not None else None
    recommendation = get_recommendation(pe)
    results.append({
        "name": stock["name"],
        "isin": stock["isin"],
        "ticker": ticker,
        "sector": stock["sector"],
        "quantity": stock["quantity"],
        "price": price,
        "value": value,
        "pe_ratio": pe,
        "recommendation": recommendation
    })

df = pd.DataFrame(results)
total_value = df["value"].sum()
df["asset_weight"] = df["value"] / total_value * 100

print(df)
df.to_excel(r"C:\Py Test\Equity Research\stock_analysis.xlsx", index=False)