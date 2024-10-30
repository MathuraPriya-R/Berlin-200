import pandas as pd

# Load data from CSV
df = pd.read_csv("users.csv")  # Replace with your CSV file path

# correlation_matrix = df.corr()
# print(correlation_matrix)

# To get the correlation between two specific columns, say 'column1' and 'column2':
correlation = df['public_repos'].corr(df['followers'])
print(f"Correlation between column1 and column2: {correlation}")



# To get the correlation between two specific columns, say 'column1' and 'column2':
correlation = df['hireable'].corr(df['followers'])
print(f"Correlation between column1 and column2: {correlation}")
