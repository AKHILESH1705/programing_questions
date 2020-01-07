import pandas as pd
df = pd.read_csv('C:\Program Files (x86).Aadhar.csv')
print(df[df['state'].str.contains('aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|mm|nn|oo|pp|qq|rr')])