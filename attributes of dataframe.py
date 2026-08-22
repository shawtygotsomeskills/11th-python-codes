import pandas as pd

data = {
    'Name': ['Ankit', 'Rahul', 'Karan'],
    'Age': [18, 19, 17],
    'Salary': [5000, 6000, 4500]
}

df = pd.DataFrame(data)

print("Index:", df.index)
print("Columns:", df.columns)
print("Axes:", df.axes)
print("Data Types:", df.dtypes)
print("Size:", df.size)
print("Shape is:", df.shape)
print("Empty:", df.empty)
print("Heading 2 rows are:")
print(df.head(n=2))
print("Last 2 rows are:")
print(df.tail(n=2))
