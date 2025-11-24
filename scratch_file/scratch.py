import pandas as pd

data = {'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Apply a single function (e.g., 'sum')
sum_result = df.agg('sum')
print(f"Sum of each column:\n{sum_result}\n")

# Apply multiple functions (e.g., 'mean', 'max')
multi_agg_result = df.agg(['mean', 'max'])
print(f"Mean and Max of each column:\n{multi_agg_result}\n")