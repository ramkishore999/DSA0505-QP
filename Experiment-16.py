import pandas as pd

data = {
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
}

df = pd.DataFrame(data, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

# Group by school code
grouped_data = df.groupby('school_code')

# Display groups and object type
print("Groups based on school code:")
for name, group in grouped_data:
    print(f"\nGroup: {name}")
    print(group)

print("\nType of GroupBy object:")
print(type(grouped_data))