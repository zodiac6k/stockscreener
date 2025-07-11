import pandas as pd
import yfinance as yf
from openpyxl import load_workbook

# Load the existing Excel file
file_path = "AK Pft March 2022.xlsx"
sheet_name = "Sheet1"  # Change if your sheet has a different name

# Read the sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Clean up stock names and map to Yahoo tickers (manual mapping might be needed)
stock_to_ticker = {
    "Ajanta Pharma": "AJANTPHARM.NS",
    "Alkem Lab": "ALKEM.NS",
    "Amrutanjan Healt": "AMRUTANJAN.NS",
    "Apollo Hospitals": "APOLLOHOSP.NS",
    "Asian Paints": "ASIANPAINT.NS",
    "Bandhan Bank": "BANDHANBNK.NS",
    "BASF India": "BASF.NS",
    "BSE": "BSE.NS",
    "C D S L": "CDSL.NS",
    "Caplin Point Lab": "CAPLIPOINT.NS",
    "City Union Bank": "CUB.NS",
    "CPSE ETF*": "CPSEETF.NS",
    "Divi's Lab.": "DIVISLAB.NS",
    "Godrej Consumer": "GODREJCP.NS",
    "Havells India": "HAVELLS.NS",
    "HCL Technologies": "HCLTECH.NS",
    "HDFC Life Insur.": "HDFCLIFE.NS",
    "Hinduja Global": "HGS.NS",
    "Igarashi Motors": "IGARASHI.NS",
    "Indiamart Inter.": "INDIAMART.NS",
    "IndusInd Bank": "INDUSINDBK.NS",
    "Info Edg.(India)": "NAUKRI.NS",
    "Infosys": "INFY.NS",
    "Jamna Auto Inds.": "JAMNAAUTO.NS",
    "Jubilant Ingrev.": "JUBLINGREA.NS",
    "K C P": "KCP.NS",
    "Kotak Mah. Bank": "KOTAKBANK.NS",
    "L & T Infotech": "LTI.NS",
    "L&T Technology": "LTTS.NS",
    "Laurus Labs": "LAURUSLABS.NS",
    pip install jinja2    "Manappuram Fin.": "MANAPPURAM.NS",
    "Maruti Suzuki": "MARUTI.NS",
    "Mayur Uniquoters": "MAYURUNIQ.NS",
    "Metropolis Healt": "METROPOLIS.NS",
    "Mold-Tek Pack.": "MOLDTKPAC.NS",
    "Mphasis": "MPHASIS.NS",
    "P I Industries": "PIIND.NS",
    "Persistent Sys": "PERSISTENT.NS",
    "Pidilite Inds.": "PIDILITIND.NS",
    "Reliance Industr": "RELIANCE.NS",
    "SBI Life Insuran": "SBILIFE.NS",
    "Strides Pharma": "STAR.NS",
    "Sundaram Finance": "SUNDARMFIN.NS",
    "Syngene Intl.": "SYNGENE.NS",
    "Tasty Bite Eat.": "TASTYBITE.NS",
    "Tata Comm": "TATACOMM.NS",
    "Tata Elxsi": "TATAELXSI.NS",
    "TCS": "TCS.NS",
    "Tech Mahindra": "TECHM.NS",
    "Thyrocare Tech.": "THYROCARE.NS",
    "Vaibhav Global": "VAIBHAVGBL.NS",
    "VRL Logistics": "VRLLOG.NS",
    "Wockhardt": "WOCKPHARMA.NS"
}

# Add columns for current price and PE ratio
current_prices = []
pe_ratios = []

for name in df['Stock Name']:
    if isinstance(name, str):
        ticker = stock_to_ticker.get(name.strip(), None)
    else:
        ticker = None
    if ticker:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            price = info.get("currentPrice") or info.get("regularMarketPrice")
            pe = info.get("trailingPE")
        except Exception:
            price = pe = "Error"
    else:
        price = pe = "Not Found"
    
    current_prices.append(price)
    pe_ratios.append(pe)

# Append new data to DataFrame
df["Live Price"] = current_prices
df["PE Ratio"] = pe_ratios
df["Price Timestamp"] = pd.Timestamp.now()
df["Market Value"] = df["Open Qty"] * df["Live Price"]
total_mv = df["Market Value"].sum()
df["Pft Weight (%)"] = (df["Market Value"] / total_mv) * 100

def pe_color(val):
    try:
        v = float(val)
        if v < 20:
            color = 'background-color: #c6efce'  # light green
        elif v > 70:
            color = 'background-color: #ffc7ce'  # light red
        else:
            color = 'background-color: #fff2cc'  # light yellow
    except:
        color = ''
    return color

styled_df = df.style.applymap(pe_color, subset=["PE Ratio"])

output_file = r"C:\Users\zodia\OneDrive\AK Pft March 2022 UPDATED.xlsx"
styled_df.to_excel(output_file, index=False, sheet_name=sheet_name, engine='openpyxl')

print(f"✅ Updated Excel file '{output_file}' with live prices, PE ratios, and PE highlighting.")
