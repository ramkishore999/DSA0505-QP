import pandas as pd

data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cote d'Ivoire", 'Colombia', 'Saint Kitts and Nevis']
}

df = pd.DataFrame(data)

# Swapping cases in the 'WHO region' column
df['WHO region'] = df['WHO region'].str.swapcase()

print(df)