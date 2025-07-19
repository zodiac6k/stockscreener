import pandas as pd

# Source Axis statement
file_path = r"C:\Users\zodia\OneDrive\Documents\Axis Statement.xlsx"

# Output path for the new workbook
output_path = r"C:\Users\zodia\OneDrive\Documents\Axis_All_Debits_NewWorkbook.xlsx"

# Load all sheet names
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names

# Container for debit records
all_debits = []

# Process every sheet
for sheet in sheet_names:
    print(f"⏳ Reading sheet: {sheet}")
    
    try:
        df = pd.read_excel(file_path, sheet_name=sheet, skiprows=17)
        df.columns = [str(col).strip().upper() for col in df.columns]

        # Check required columns exist
        expected = ["SRL NO", "TRAN DATE", "CHQNO", "PARTICULARS", "DR"]
        if not all(col in df.columns for col in expected):
            print(f"⚠️ Skipping sheet '{sheet}' — missing required columns.")
            continue

        # Filter debit-only rows
        debit_df = df[df["DR"].notna()][expected].copy()
        debit_df.rename(columns={
            "SRL NO": "Sl_Number",
            "TRAN DATE": "Date",
            "CHQNO": "Reference",
            "PARTICULARS": "Name",
            "DR": "Amount_Paid"
        }, inplace=True)

        debit_df["Sheet"] = sheet  # Optional: to track origin
        all_debits.append(debit_df)

    except Exception as e:
        print(f"❌ Error processing sheet '{sheet}': {e}")

# Combine and save
if all_debits:
    final_df = pd.concat(all_debits, ignore_index=True)
    final_df.to_excel(output_path, index=False)
    print(f"\n✅ All debit transactions saved to new workbook:\n{output_path}")
else:
    print("❌ No debit data found in any sheet.")
