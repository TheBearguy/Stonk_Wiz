import pandas as pd
data = pd.read_csv("BSE_Equity.csv")
data.set_index('Security Code', inplace=True)
s = data['Issuer Name'].to_dict()
print(s)
