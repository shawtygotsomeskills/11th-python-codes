import pandas as pd

data = {
    'Name': ['Amit', 'Bhaum', 'Chetan'],
    'Marks': [90, 85, 92],
    'City': ['Delhi', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data, index=['R1', 'R2', 'R3'])

print("Original DataFrame:")
print(df)

print("\n")

df = df.drop('R2')

print("DataFrame after deleting R2:")
print(df)
