import pandas as pd

expected = pd.read_csv("data/positions_expected.csv")
actual = pd.read_csv("data/positions_actual.csv")

merged = expected.merge(actual, on="option_id", suffixes=("_expected", "_actual"))
merged["break_amount"] = merged["quantity_actual"] - merged["quantity_expected"]

breaks = merged[merged["break_amount"] != 0]

print("Breaks found:")
print(breaks)
