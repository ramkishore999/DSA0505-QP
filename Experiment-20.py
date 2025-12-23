import pandas as pd

data = {
    'Year': [1986, 1986, 1985, 1986, 1987],
    'WHO region': ['Western Pacific', 'Americas', 'Africa', 'Americas', 'Americas'],
    'Country': ['Viet Nam', 'Uruguay', "Cote d'Ivoire", 'Colombia', 'Saint Kitts and Nevis']
}

df = pd.DataFrame(data)

# Finding the index of substring 'ia' in the 'Country' column
# Returns -1 if not found
df['Index_of_ia'] = df['Country'].str.find('ia')

print(df[['Country', 'Index_of_ia']])