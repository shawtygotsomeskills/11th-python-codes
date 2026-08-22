import pandas as pd

data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 35, "Paris"]
]

df = pd.DataFrame(data, columns=["Name", "Age", "City"])
print(df)
