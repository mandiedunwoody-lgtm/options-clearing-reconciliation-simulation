import pandas as pd

positions = pd.read_csv("data/positions_expected.csv")
exp = pd.read_csv("data/expirations.csv")

merged = positions.merge(exp, on="option_id")

print("Expiration status:")
print(merged)

